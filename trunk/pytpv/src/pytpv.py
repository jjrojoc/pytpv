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
#import pango
# librerias para generar los pdfs

from gazpacho.loader.loader import ObjectBuilder

# librerias para el acceso a base de datos
import MySQLdb

# librerias para ejecutar xpdf y para ver la linea de comandos
import os, os.path, sys

# constantes


CONSULTA_BASE = 'select id, nombre, direccion, importe, hora from acreditaciones'
LINEAS_TICKET = 'select id_ticket, cantidad, id_articulo, importe from ventas'
# para las columnas del listView
(ID, NOMBRE, DIRECCION, IMPORTE, HORA) = range(5)
(ID_TICKET, UNI, DESCRIPCION, IMP) = range(4)

class PyTPV:
    def __init__(self):
        self.db = MySQLdb.connect(db='acreditaciones',
                                  user='root')
        self.cursor = self.db.cursor()
        
        self.widgets = ObjectBuilder('pytpv.glade')
        #self.widgets = gtk.glade.XML('pytpv.glade')
        self.widgets.signal_autoconnect(self)
        
        self.listStore = gtk.ListStore(int, str, str, str, str)  # Id, Nombre, Direccion, Importe, Hora
        
        self.cargaDatos(CONSULTA_BASE)
        
        
        self.listView = self.widgets.get_widget('listView')
        self.listView.set_model(self.listStore)
        self.listView.get_selection().set_mode(gtk.SELECTION_MULTIPLE)
        
    
        columns = ['NOMBRE', 'DIRECCION', 'IMP', 'HORA']
        for i in range(len(columns)):
            renderer = gtk.CellRendererText()
            renderer.set_property('editable', True)
            renderer.connect('edited', self.editedCallback, i+1)
            renderer.set_fixed_size(-1, 25)
            column = gtk.TreeViewColumn(columns[i], renderer, text=(i+1))
            #column.set_resizable(True)
            column.set_spacing(10)
            column.set_alignment(0.5)
            #font = pango.FontDescription('helvetica 8')
            #renderer.set_property('font-desc', font)
            self.listView.append_column(column)
            column.set_sizing(gtk.TREE_VIEW_COLUMN_FIXED)
            column.set_fixed_width(100)
            column.set_sort_column_id(i+1)
            renderer.connect('edited', self.editedCallback, i+1)
            
        
        
        self.ticketstore = gtk.ListStore(int, str, str, str)    # Id, Cantidad, Descripcion, importe   
        
        
        
        self.treeview3 = self.widgets.get_widget('treeview3')
        self.treeview3.set_model(self.ticketstore)
        self.treeview3.get_selection().set_mode(gtk.SELECTION_MULTIPLE)
        
        
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
        

        # unidades por pagina para la impresion
        self.upp = 1
        
    def buscar(self, datos=None):
        self.listStore.clear()
        c = self.cursor
        #c.execute('select id, nombre, direccion, importe, hora from acreditaciones where nombre = %s', self.widgets.get_widget('entBusqueda').get_text())
        c.execute('select id, nombre, direccion, importe, hora from acreditaciones where nombre like %s', self.widgets.get_widget('entBusqueda').get_text()+'%')
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
            id_tk, ud, nombre, precio = linea
            
            linea = [id_tk] + [ud] + [nombre] + [precio]
            self.ticketstore.append(linea)
            
            
    def on_listView_cursor_changed(self, datos=None):
        self.cargalineasticket(LINEAS_TICKET)
                
                    
    def nuevoAsistente(self, boton, datos=None):
        dialog = self.widgets.get_widget('dlgNuevoAsistente')
        resultado = dialog.run()
        dialog.hide()
        if resultado == 1:
            datos = []
            for entry in ['entNombre', 'entApellidos', 'entEmail', 'entCiudad']:
                datos.append(self.widgets.get_widget(entry).get_text())
            

            # lo meto en la base de datos
            id = self.insertaBD(datos)
            datos = [id] + datos
            # lo meto en la interfaz
            self.listStore.prepend(datos)

        
    def ticketrow (self, linea=None):
        self.cursor.execute('select unidades, descripcion, precio from articulosa where id = 1')
        for linea in self.cursor.fetchall():
            ud, nombre, precio = linea
            id_ticket = self.insertalinea(linea)
            linea = [id_ticket] + [ud] + [nombre] + [precio]
            self.ticketstore.append(linea)
            
                        
    def insertalinea (self, linea):
        self.cursor.execute('insert into acreditaciones.ventas (cantidad, id_articulo, importe) values (%s, %s, %s)', linea)
        self.cursor.execute('SELECT max(id_ticket) from ventas where ventas.cantidad =%s AND ventas.id_articulo = %s AND ventas.importe=%s', linea)
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
        self.cursor.execute('insert into acreditaciones (nombre, direccion, importe, hora) values (%s, %s, %s, %s)',
                            tmp)
        self.cursor.execute('select id from acreditaciones where nombre=%s and direccion=%s and importe=%s and hora=%s',
                            tmp)
        return int(self.cursor.fetchone()[0])

    def borraBD(self, iter):
        c = self.cursor
        c.execute('delete from acreditaciones where id = %s',
                  (self.listStore.get_value(iter, ID),))
        
    
    def borralineaticket(self, iter):
        c = self.cursor
        c.execute('delete from ventas where id_ticket = %s',
                  (self.ticketstore.get_value(iter, ID_TICKET),))
        
                
    def actualizaBD(self, iter):
        c = self.cursor
        c.execute("""update acreditaciones set nombre = %s, direccion = %s,
        importe = %s, hora = %s 
        where id = %s""", (
            self.listStore.get_value(iter, NOMBRE).encode('latin-1'),
            self.listStore.get_value(iter, DIRECCION).encode('latin-1'),
            self.listStore.get_value(iter, IMPORTE).encode('latin-1'),
            self.listStore.get_value(iter, HORA).encode('latin-1'),
            self.listStore.get_value(iter, ID)
            ))
        
    def actualizaticketstore(self, iter):
        c = self.cursor
        c.execute("""update ventas set cantidad = %s, id_articulo = %s, importe = %s
        where id_ticket = %s""", (
            self.ticketstore.get_value(iter, UNI).encode('latin-1'),
            self.ticketstore.get_value(iter, DESCRIPCION).encode('latin-1'),
            self.ticketstore.get_value(iter, IMP).encode('latin-1'),
            self.ticketstore.get_value(iter, ID_TICKET),
            ))

    def salir(self, boton, datos=None):
        dialog = self.widgets.get_widget('dlgSalida')
        resultado = dialog.run()
        dialog.hide()
        if resultado == 1:
            gtk.main_quit()

    def preferencias(self, boton, datos=None):
        dialog = self.widgets.get_widget('dlgPreferencias')
        resultado = dialog.run()
        dialog.hide()
        if resultado == gtk.RESPONSE_OK:
            self.upp = self.widgets.get_widget('sbtnUPP').get_value_as_int()
            
    def salir_sin_dialogo(self, datos=None):
        gtk.main_quit()
        
                        
if __name__ == '__main__':
    a = PyTPV()
    a.run()
