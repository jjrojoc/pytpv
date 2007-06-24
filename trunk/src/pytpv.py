#!/usr/bin/env python
# -*- coding: utf-8 -*-
from encodings import utf_8

from codificacion import *



#from insertaarticulos import *

# PyTPV.py  Punto de venta para restaurants, bar, pizzeria, etc.
# Copyright (C) 2007 Juan José Rojo <jjrojoc@gmail.com>
# Este programa es software libre. Puede redistribuirlo y/o modificarlo bajo
# los terminos de la Licencia Publica General de GNU segun es publicada por la
# Free Software Foundation, bien de la version 2 de dicha Licencia o bien
# (segun su eleccion) de cualquier version posterior.
#
# Este programa se distribuye con la esperanza de que sea util, pero SIN
# NINGUNA GARANTIA, incluso sin la garantia MERCANTIL implicita o sin
# garantizar la CONVENIENCIA PARA UN PROPOSITO PARTICULAR. Veaase la Licencia
# Publica General de GNU para mas detalles.
#
# Deberia haber recibido una copia de la Licencia Publica General junto con
# este programa. Si no ha sido asi escriba a la Free Software Foundation,
# Inc., en 675 Mass Ave, Cambridge, MA 02139, EEUU. 
#
# Puede contactar con el autor mediante la direccion de correo electronico
# jjrojoc@gmail.com


# librerias para la interfaz grafica
import pygtk
pygtk.require('2.0')
import gtk
import gtk.glade
import gobject


from gazpacho.loader.loader import ObjectBuilder

# libreria para el manejo de fuentes
import pango
# librerias para generar los pdfs
import locale
# librerias para el acceso a base de datos
import MySQLdb

# librerias para ejecutar xpdf y para ver la linea de comandos
import os, os.path, sys
#import clients

# constantes

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

class PyTPV:
    """Clase principal de pytpv desde donde se cargan todos los modulos
    """
    def __init__(self):
        self.db = MySQLdb.connect(db='pytpvdb',
                                  user='root')
        self.cursor = self.db.cursor()
        
#        self.botonera = botonera()
        self.widgets = ObjectBuilder('pytpv.glade')
        #self.widgets = gtk.glade.XML('pytpv.glade')
        w = self.widgets.get_widget('window1')
        c = self.cursor
        c.execute('select (DATE_FORMAT(curdate(), "%d/%m/%Y"))')
        today = c.fetchone()[0]
        #today = datetime.date.today()
        w.set_title("PyTPV - %s" % today)
        w.maximize()
        

        icon = gtk.gdk.pixbuf_new_from_file("pixmaps/pytpv2.png")
        w.set_icon(icon)
        self.widgets.signal_autoconnect(self)
       
        
        self.listStore = gtk.ListStore(int, str, str)  # Id, Nombre, Direccion, Importe, Hora
        
        self.cargaDatos(CONSULTA_BASE)
        
        
        self.listView = self.widgets.get_widget('listView')
        self.listView.set_model(self.listStore)
        self.listView.get_selection().set_mode(gtk.SELECTION_MULTIPLE)
        
    
        columns = ['NOMBRE', 'DIRECCION']
        for i in range(len(columns)):
            renderer = gtk.CellRendererText()
            renderer.set_property('editable', True)
            renderer.connect('edited', self.editedCallback, i+1)
            renderer.set_fixed_size(-1, 25)
            column = gtk.TreeViewColumn(columns[i], renderer, text=(i+1))
            #column.set_resizable(True)
            column.set_spacing(10)
            column.set_alignment(0.5)
            font = pango.FontDescription('helvetica 8')
            renderer.set_property('font-desc', font)
            self.listView.append_column(column)
            column.set_sizing(gtk.TREE_VIEW_COLUMN_FIXED)
            column.set_fixed_width(100)
            column.set_sort_column_id(i+1)
            renderer.connect('edited', self.editedCallback, i+1)
            
        
        
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
        
        # unidades por pagina para la impresion
        self.upp = 1
        
    def buscar(self, datos=None):
        self.listStore.clear()
        c = self.cursor
        #c.execute('select id, nombre, direccion, importe, hora from acreditaciones where nombre = %s', self.widgets.get_widget('entBusqueda').get_text())
        c.execute('select id, nombre, direccion from clientes where nombre like %s', self.widgets.get_widget('entBusqueda').get_text()+'%')
        datos = c.fetchall()
        
        for dato in datos:
            id = dato[0]
            dato = [unicode(d, 'latin-1') for d in dato[1:]]
            
            self.listStore.append([id]+dato)    
        
        
    def cargaDatos(self, consulta):
        c = self.cursor
        c.execute(consulta)
        datos = c.fetchall()
        
        for dato in datos:
            id = dato[0]
            dato = [unicode(d, 'latin-1') for d in dato[1:]]
            
            self.listStore.append([id]+dato)
            
            
    def cargalineasticket(self, cargalineas):
        c = self.cursor
        c.execute(cargalineas)
        
        for linea in c.fetchall():
            id, cantidad, nombre, precio = linea
            
            linea = [id] + [cantidad] + [nombre] + [precio]
            
            self.ticketstore.append(linea)
            
    def cargaclientes(self, clientes):        
        c = self.cursor
        c.execute(clientes)
        
        for linea in c.fetchall():
            idcliente, nombrecliente, direccioncliente = linea
            
            linea = [idcliente] + [nombrecliente] + [direccioncliente]
            self.listacliente.append(linea)
            

    def cargaarticulos(self, articulos):        
        c = self.cursor
        c.execute(articulos)
        
        for linea in c.fetchall():
            idarticulo, familia, descripcion, stock, stock_minimo, precio_venta, imagen = linea
            
            linea = [idarticulo] + [familia] + [descripcion] + [stock] + [stock_minimo] + \
                    [precio_venta] + [imagen]
            self.listarticlestore.append(linea)
            
            
    def cargahistorico(self, historico):        
        c = self.cursor
        c.execute(historico)
        
        for linea in c.fetchall():
            idhistorico, cliente_FK_id, direccion_FK_id, caja_FK_id, fecha, hora, estado, metalico= linea
            
            linea = [idhistorico] + [cliente_FK_id] + [direccion_FK_id] + [caja_FK_id] + [fecha] + [hora] + \
                    [estado] + [metalico]
            self.historicostore.append(linea)        
    
            
    def on_listView_cursor_changed(self, datos=None):
        self.ticketstore.clear()
        self.cargalineasticket(LINEAS_TICKET)
        
        
    def on_listaclientes_cursor_changed(self, datos=None):
                
        selection = self.listaclienteview.get_selection()
        treemodel, iter = selection.get_selected()    
        id = treemodel.get_value(iter, 0)
        nombre = treemodel.get_value(iter, 1)
        direccion = treemodel.get_value(iter, 2)
        
                  
        self.widgets.get_widget('entNombre').set_text(nombre)
        self.widgets.get_widget('entDireccion').set_text(direccion)
        
        
                    
                    
    def nuevoAsistente(self, icon, datos=None):
        dialog = self.widgets.get_widget('dlgNuevoAsistente')
        resultado = dialog.run()
        dialog.hide()
        
        if resultado == 1:
            datos = []
            for entry in ['entNombre', 'entDireccion']:
                datos.append(self.widgets.get_widget(entry).get_text())
            
            # lo meto en la base de datos
            id = self.insertaBD(datos)
            datos = [id] + datos
            # lo meto en la interfaz
            self.listStore.prepend(datos)
            self.listacliente.prepend(datos)
            #self.listacliente.prepend(datos[0:-2])
            #self.listView.get_selection().select_path((0,))
            #scroll = self.widgets.get_widget('scrolledwindow3')
            
                
        
    def pollo_asado (self, linea=None):
        self.cursor.execute('select id, descripcion, precio_venta from articulos where id = 1')
        for linea in self.cursor.fetchall():
            id, descripcion, precio = linea
    #            a=7.25+2.67
    #            b= locale.format("%.2f", a)
    #            print b
            linea = [id] + [precio]
            id_ticket = self.insertalinea(linea)
            print id_ticket
            linea = [id_ticket] + [1] + [descripcion] + [precio]
            print linea
            
            self.ticketstore.append(linea)
                
            
    def insertalinea (self, linea):
        self.cursor.execute('insert into ticket_linea (ticket_FK_id, cantidad, articulo_FK_id, precio_venta) values (1, 1, %s, %s)', linea)
        self.cursor.execute('SELECT last_insert_id(), cantidad, (select descripcion from articulos where id = 1),\
                             (cantidad*precio_venta) from ticket_linea where articulo_FK_id = %s and precio_venta = %s', linea)
        
        return int(self.cursor.fetchone()[0])
    
    
    def medio_pollo(self, linea=None):
        
            self.cursor.execute('select id, descripcion, precio_venta from articulos where id = 2')
            for linea in self.cursor.fetchall():
                id, descripcion, precio = linea
    #            a=7.25+2.67
    #            b= locale.format("%.2f", a)
    #            print b
                linea = [id] + [precio]
                id_ticket = self.insertalinea1(linea)
    #            print id_ticket
                linea = [id_ticket] + [1] + [descripcion] + [precio]
                print linea
                self.ticketstore.append(linea)
                
                            
    def insertalinea1 (self, linea):
        self.cursor.execute('insert into ticket_linea (ticket_FK_id, cantidad, articulo_FK_id, precio_venta) values (1, 1, %s, %s)', linea)
        self.cursor.execute('select last_insert_id(), cantidad, (select descripcion from articulos where id = 2), precio_venta from ticket_linea where articulo_FK_id = %s and precio_venta = %s', linea)
        
        return int(self.cursor.fetchone()[0])
    
    def quitaAsistente(self, boton, datos=None):
        seleccion = []
        self.listView.get_selection().selected_foreach(
            lambda model, path, iter, sel = seleccion: sel.append(iter))
        for iter in seleccion:
            self.borraBD(iter)
            self.listStore.remove(iter)
            
    def quitalineaticket(self, boton, linea=None):
        seleccion = []
        self.treeview3.get_selection().selected_foreach(
            lambda model, path, iter, sel = seleccion: sel.append(iter))
        for iter in seleccion:
            print iter
            self.borralineaticket(iter)
            self.ticketstore.remove(iter)
                
    def run(self):
        gtk.main()

    def editedCallback(self, renderer, path, newText, column):
        iter = self.listStore.get_iter(path)
        self.listStore.set_value(iter, column, newText)
        self.actualizaBD(iter)
    
    def editedcells(self, render, path, newTex, columna):
        iter = self.ticketstore.get_iter(path)
        self.ticketstore.set_value(iter, columna, newTex)
        self.actualizaticketstore(iter)
        
    def insertaBD(self, datos):
        tmp = []
        for d in datos:
            tmp.append(d.encode('latin-1'))
        self.cursor.execute('insert into clientes (nombre, direccion) values (%s, %s)',
                            tmp)
        self.cursor.execute('select id from clientes where nombre=%s and direccion=%s',
                            tmp)
        return int(self.cursor.fetchone()[0])

    def borraBD(self, iter):
        c = self.cursor
        c.execute('delete from clientes where id = %s',
                  (self.listStore.get_value(iter, ID),))
        
    
    def borralineaticket(self, iter):
        c = self.cursor
        c.execute('delete from ticket_linea where id = %s',
                  (self.ticketstore.get_value(iter, IDTICKET),))
        
                
    def actualizaBD(self, iter):
        c = self.cursor
        c.execute("""update clientes set nombre = %s, direccion = %s 
        where id = %s""", (
            self.listStore.get_value(iter, NOMBRE).encode('latin-1'),
            self.listStore.get_value(iter, DIRECCION).encode('latin-1'),
            self.listStore.get_value(iter, ID)
            ))
        
    def actualizaticketstore(self, iter):
        c = self.cursor
        r = self.ticketstore.get_value(iter, UNI).encode('latin-1')
        s = self.ticketstore.get_value(iter, IMP).encode('latin-1')
        t = self.ticketstore.get_value(iter, IDTICKET)
        print r, s, t
        c.execute("""update ticket_linea set cantidad = %s, precio_venta = %s where id = %s""", (
            
#            self.ticketstore.get_value(iter, ARTICULO_FK_ID).encode('latin-1'),
          r, s, t  
            
            ))
        
        
    def salir(self, button, datos=None):
        dialog = self.widgets.get_widget('dlgSalida')
        resultado = dialog.run()
                
        if resultado == 1:
            gtk.main_quit()
            return False

        if resultado == 2:
            dialog.hide()
            return True
        

    def preferencias(self, boton, datos=None):
        dialog = self.widgets.get_widget('dlgPreferencias')
        resultado = dialog.run()
        dialog.hide()
        if resultado == gtk.RESPONSE_OK:
            self.upp = self.widgets.get_widget('sbtnUPP').get_value_as_int()
            
    def cargaClientes(self, clientes):
        c = self.cursor
        c.execute(clientes)
        
        for linea in c.fetchall():
            id, nombre, direccion, fecha_alta = linea
            linea = [id] + [nombre] + [direccion] + [fecha_alta] 
            self.listclientstore.append(linea)
    
    def acercade(self, button):
        dialog = self.widgets.get_widget('dlgacercade')
        resultado = dialog.run()
        
        if resultado == 1:
            dialog.hide()
    
                        
if __name__ == '__main__':
    a = PyTPV()
    a.run()