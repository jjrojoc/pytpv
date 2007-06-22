#!/usr/bin/env python
# -*- coding: utf-8 -*-
from encodings import utf_8
from gazpacho.loader.loader import ObjectBuilder
from codificacion import *
import gtk, pango
import MySQLdb
import cargadb

CONSULTA_BASE = 'select ticket.id, clientes.nombre, clientes.direccion\
                 from ticket inner join clientes on clientes.id = cliente_FK_id'
LINEAS_TICKET = 'select ticket_linea.id, ticket_linea.cantidad, articulos.descripcion,\
                 ticket_linea.precio_venta from ticket_linea inner join articulos on articulos.id = articulo_FK_id'
CLIENTES_BASE = 'select id, nombre, direccion from clientes'
CLIENTES_CONSULTA = 'select * from clientes'
ARTICULOS_CONSULTA = 'select articulos.id, familia.nombre, articulos.descripcion,\
                     articulos.stock, articulos.stock_minimo, articulos.precio_venta, articulos.imagen from articulos\
                     inner join familia on familia.id = familia_FK_id'
HISTORICO_CONSULTA = 'select ticket.id, clientes.nombre, clientes.direccion,\
                     ticket.caja_FK_id, ticket.fecha, ticket.hora, ticket.estado,\
                      ticket.metalico from ticket inner join clientes on clientes.id = cliente_FK_id'


# para las columnas del listView
(ID, NOMBRE, DIRECCION) = range(3)
# para las columnas del ticketstore
(IDTICKET, UNI, ARTICULO_FK_ID, IMP) = range(4)
# para las columnas del listaclientes
(IDCLIENTE, NOMBRECLIENTE, DIRECCIONCLIENTE) = range(3)
# para las columnas del listView
(ID, NOMBRE, DIRECCION, FECHA_ALTA) = range(4)
# para las columnas del listView
(ID, FAMILIA, DESCRIPCION, STOCK, STOCKMINIMO, PRECIOVENTA, IMAGEN) = range(7)
# para las columnas del listView
(ID, CLIENTE_FK_ID, CAJA_FK_ID, FECHA, HORA, ESTADO, METALICO) = range(7)


class listStore:
    
    db = MySQLdb.connect(db='pytpvdb',
                                  user='root')
    cursor = db.cursor()    
    
    listStore = gtk.ListStore(int, str, str)  # Id, Nombre, Direccion, Importe, Hora
    
    
#        cargaDatos(CONSULTA_BASE)
    
    
    listView = ObjectBuilder('pytpv.glade').get_widget('listView')
    listView.set_model(listStore)
    listView.get_selection().set_mode(gtk.SELECTION_MULTIPLE)
    

    columns = ['NOMBRE', 'DIRECCION']
    for i in range(len(columns)):
        renderer = gtk.CellRendererText()
        renderer.set_property('editable', True)
#        renderer.connect('edited', editedCallback, i+1)
        renderer.set_fixed_size(-1, 25)
        column = gtk.TreeViewColumn(columns[i], renderer, text=(i+1))
        #column.set_resizable(True)
        column.set_spacing(10)
        column.set_alignment(0.5)
        font = pango.FontDescription('helvetica 8')
        renderer.set_property('font-desc', font)
        listView.append_column(column)
        column.set_sizing(gtk.TREE_VIEW_COLUMN_FIXED)
        column.set_fixed_width(100)
        column.set_sort_column_id(i+1)
#        renderer.connect('edited', editedCallback, i+1)
        
    
    def ticketstore(self):
        self.ticketstore = gtk.ListStore(int, str, str, str)    # Id, Cantidad, Descripcion, importe   
        
        
        
        self.treeview3 = self.widgets.get_widget('treeview3')
        self.treeview3.set_model(self.ticketstore)
        #self.treeview3.get_selection().set_mode(gtk.SELECTION_MULTIPLE)
        
        
        columnsticketview = ['UNI', 'DESCRIPCION', 'IMP']
        
        for j in range(len(columnsticketview)):
            render = gtk.CellRendererText()
            render.set_property('editable', True)
            render.connect('edited', self.editedcells, j+1)
            render.set_fixed_size(-1, 25)
            columna = gtk.TreeViewColumn(columnsticketview[j], render, text=(j+1))
            columna.set_resizable(True)
            self.treeview3.append_column(columna)
            columna.set_sort_column_id(j+1)
            render.connect('edited', self.editedcells, j+1)  
        
        # retoque de la GUI que Glade no permite
        #treeview listaclientes del dialog Nueva persona
    def listacliente(self):
        self.listacliente = gtk.ListStore(int, str, str)  # Id, Nombre, Direccion
        
        self.listaclienteview = self.widgets.get_widget('listaclientes')
        self.listaclienteview.set_model(self.listacliente)
        #self.listaclienteview.get_selection().set_mode(gtk.SELECTION_MULTIPLE)
        
        self.cargaclientes(CLIENTES_BASE)
        cols = ['NOMBRE', 'DIRECCION']
        for i in range(len(cols)):
            rend = gtk.CellRendererText()
            #renderer.set_property('editable', True)
            #renderer.connect('edited', self.editedCallback, i+1)
            rend.set_fixed_size(-1, 25)
            col = gtk.TreeViewColumn(cols[i], rend, text=(i+1))
            #column.set_resizable(True)
            col.set_spacing(10)
            col.set_alignment(0.5)
            font = pango.FontDescription('helvetica 8')
            rend.set_property('font-desc', font)
            self.listaclienteview.append_column(col)
            col.set_sizing(gtk.TREE_VIEW_COLUMN_FIXED)
            col.set_fixed_width(100)
            col.set_sort_column_id(i+1)
            #rend.connect('edited', self.editedCallback, i+1)
         
         
    def listclientstore(self):    
        self.listclientstore = gtk.ListStore(int, str, str, str)  # Id, Nombre, Direccion, Fecha_alta
        
        self.cargaClientes(CLIENTES_CONSULTA)
        
        
        self.listclientsview = self.widgets.get_widget('listClients')
        self.listclientsview.set_model(self.listclientstore)
        self.listclientsview.get_selection().set_mode(gtk.SELECTION_MULTIPLE)
        
    
        columns1 = ['ID', 'NOMBRE', 'DIRECCION', 'FECHA_ALTA']
        for i in range(len(columns1)):
            renderer1 = gtk.CellRendererText()
            renderer1.set_property('editable', True)
            renderer1.connect('edited', self.editedCallback, i+1)
            column1 = gtk.TreeViewColumn(columns1[i], renderer1, text=(i))
            #column1.set_resizable(True)
            column1.set_spacing(10)
            column1.set_alignment(0.5)
            #font = pango.FontDescription('helvetica 8')
            #renderer.set_property('font-desc', font)
            self.listclientsview.append_column(column1)
    #            column1.set_sizing(gtk.TREE_VIEW_COLUMN_FIXED)
    #            column1.set_fixed_width(100)
            column1.set_sort_column_id(i+1)
            renderer1.connect('edited', self.editedCallback, i+1)
            
    def listarticlestore(self):
        self.listarticlestore = gtk.ListStore(int, str, str, str, str, str, str)  # Id, Nombre, Direccion, Fecha_alta
        
        self.cargaarticulos(ARTICULOS_CONSULTA)
        
        
        self.listarticleview = self.widgets.get_widget('listArticles')
        self.listarticleview.set_model(self.listarticlestore)
        self.listarticleview.get_selection().set_mode(gtk.SELECTION_MULTIPLE)
        
    
        columns2 = ['ID', 'FAMILIA', 'DESCRIPCION', 'STOCK', 'STOCK_MINIMO', 'PRECIO_VENTA', 'IMAGEN']
        for i in range(len(columns2)):
            renderer2 = gtk.CellRendererText()
            renderer2.set_property('editable', True)
            renderer2.connect('edited', self.editedCallback, i+1)
            column2 = gtk.TreeViewColumn(columns2[i], renderer2, text=(i))
            #column2.set_resizable(True)
            column2.set_spacing(10)
            column2.set_alignment(0.5)
            #font = pango.FontDescription('helvetica 8')
            #renderer2.set_property('font-desc', font)
            self.listarticleview.append_column(column2)
    #            column2.set_sizing(gtk.TREE_VIEW_COLUMN_FIXED)
    #            column2.set_fixed_width(100)
            column2.set_sort_column_id(i+1)
            renderer2.connect('edited', self.editedCallback, i+1)
            
    def historicostore(self):    
        self.historicostore = gtk.ListStore(int, str, str, str, str, str, str, str)  # Id, Nombre, Direccion, Fecha_alta
        
        self.cargahistorico(HISTORICO_CONSULTA)
        
        
        self.historicoview = self.widgets.get_widget('treeviewhistory')
        self.historicoview.set_model(self.historicostore)
        self.historicoview.get_selection().set_mode(gtk.SELECTION_MULTIPLE)
        
    
        columns3 = ['ID', 'CLIENTE', 'DIRECCION', 'CAJA', 'FECHA', 'HORA', 'ESTADO', 'METALICO']
        for i in range(len(columns3)):
            renderer3 = gtk.CellRendererText()
            renderer3.set_property('editable', True)
            renderer3.connect('edited', self.editedCallback, i+1)
            column3 = gtk.TreeViewColumn(columns3[i], renderer3, text=(i))
            #column2.set_resizable(True)
            column3.set_spacing(10)
            column3.set_alignment(0.5)
            #font = pango.FontDescription('helvetica 8')
            #renderer2.set_property('font-desc', font)
            self.historicoview.append_column(column3)
    #            column2.set_sizing(gtk.TREE_VIEW_COLUMN_FIXED)
    #            column2.set_fixed_width(100)
            column3.set_sort_column_id(i+1)
            renderer3.connect('edited', self.editedCallback, i+1)
            
    def cargaDatos(self, consulta):
        
        c = self.cursor
        c.execute(consulta)
        datos = c.fetchall()
        
        for dato in datos:
            id = dato[0]
            dato = [unicode(d, 'latin-1') for d in dato[1:]]
            
            self.listStore.append([id]+dato)
            
    def editedCallback(renderer, path, newText, column):
        index = listStore.get_index(path)
        listStore.set_value(index, column, newText)
        actualizaBD(index)
    
    
    def actualizaBD(index):
        c = cursor
        c.execute("""update clientes set nombre = %s, direccion = %s 
                where id = %s""", (
        listStore.get_value(index, NOMBRE).encode('latin-1'),
        listStore.get_value(index, DIRECCION).encode('latin-1'),
        listStore.get_value(index, ID)
        ))
    
    #        
    #        
    #def cargalineasticket(self, cargalineas):
    #    c = self.cursor
    #    c.execute(cargalineas)
    #    
    #    for linea in c.fetchall():
    #        id, cantidad, nombre, precio = linea
    #        
    #        linea = [id] + [cantidad] + [nombre] + [precio]
    #        
    #        self.ticketstore.append(linea)
    #        
    #def cargaclientes(self, clientes):        
    #    c = self.cursor
    #    c.execute(clientes)
    #    
    #    for linea in c.fetchall():
    #        idcliente, nombrecliente, direccioncliente = linea
    #        
    #        linea = [idcliente] + [nombrecliente] + [direccioncliente]
    #        self.listacliente.append(linea)
    #        
    #
    #def cargaarticulos(self, articulos):        
    #    c = self.cursor
    #    c.execute(articulos)
    #    
    #    for linea in c.fetchall():
    #        idarticulo, familia, descripcion, stock, stock_minimo, precio_venta, imagen = linea
    #        
    #        linea = [idarticulo] + [familia] + [descripcion] + [stock] + [stock_minimo] + \
    #                [precio_venta] + [imagen]
    #        self.listarticlestore.append(linea)
    #        
    #        
    #def cargahistorico(self, historico):        
    #    c = self.cursor
    #    c.execute(historico)
    #    
    #    for linea in c.fetchall():
    #        idhistorico, cliente_FK_id, direccion_FK_id, caja_FK_id, fecha, hora, estado, metalico= linea
    #        
    #        linea = [idhistorico] + [cliente_FK_id] + [direccion_FK_id] + [caja_FK_id] + [fecha] + [hora] + \
    #                [estado] + [metalico]
    #        self.historicostore.append(linea)
    #        
    #
    #def cargaClientes(self, clientes):
    #        c = self.cursor
    #        c.execute(clientes)
    #        
    #        for linea in c.fetchall():
    #            id, nombre, direccion, fecha_alta = linea
    #            linea = [id] + [nombre] + [direccion] + [fecha_alta] 
    #            self.listclientstore.append(linea)