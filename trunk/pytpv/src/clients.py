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
import pytpv
import MySQLdb
import locale


CLIENTES_CONSULTA = 'select * from clientes'

# para las columnas del listView
(ID, NOMBRE, DIRECCION, FECHA_ALTA) = range(4)

db = MySQLdb.connect(db='pytpvdb', 
                                  user='root')
cursor = db.cursor()


def ticketrow (self, linea=None):
    self.cursor.execute('select id, descripcion, precio_venta from articulos where id = 1')
    for linea in self.cursor.fetchall():
        id, descripcion, precio = linea
#            a=7.25+2.67
#            b= locale.format("%.2f", a)
#            print b
        linea = [id] + [precio]
        id_ticket = self.insertalinea(linea)
#            print id_ticket
        linea = [id_ticket] + [1] + [descripcion] + [locale.format("%.2f", 1*precio)]
        print linea
        self.ticketstore.append(linea)
            
        
        
            
                        
def insertalinea (self, linea):
    self.cursor.execute('insert into ticket_linea (ticket_FK_id, cantidad, articulo_FK_id, precio_venta) values (1, 2, %s, %s)', linea)
    self.cursor.execute('SELECT last_insert_id(), cantidad, (select descripcion from articulos where id = 1),\
                         (cantidad*precio_venta) from ticket_linea where articulo_FK_id = %s and precio_venta = %s', linea)
    
    return int(self.cursor.fetchone()[0])




def buscaClientes(datos=None):
    listclientstore.clear()
    c = cursor
    #c.execute('select id, nombre, direccion, importe, hora from acreditaciones where nombre = %s', widgets.get_widget('entBusqueda').get_text())
    c.execute('select id, nombre, direccion, fecha_alta from clientes where nombre like %s', widgets.get_widget('entBusqueda').get_text()+'%')
    datos = c.fetchall()
        
    for dato in datos:
        id = dato[0]
        dato = [unicode(d, 'latin-1') for d in dato[1:]]
            
        listclientstore.append([id]+dato)    
        
        
def cargaClientes(clientes, ):
    c = cursor
    c.execute(clientes)
        
    for linea in c.fetchall():
        id, nombre, direccion, fecha_alta = linea
        linea = [id] + [nombre] + [direccion] + [fecha_alta] 
        listclientstore.append(linea)
        print linea
            
    
            
                   
                    
def nuevoCliente(boton, datos=None):
    dialog = widgets.get_widget('dlgNuevoAsistente')
    resultado = dialog.run()
    dialog.hide()
    if resultado == 1:
        datos = []
        for entry in ['entNombre', 'entApellidos', 'entEmail', 'entCiudad']:
            datos.append(widgets.get_widget(entry).get_text())
            
            # lo meto en la base de datos
        id = insertaBD(datos)
        datos = [id] + datos
        # lo meto en la interfaz
        listStore.prepend(datos)

        
    
                        
    
    
def quitaCliente(self, boton, datos=None):
    seleccion = []
    listView.get_selection().selected_foreach(
        lambda model, path, iter, sel = seleccion: sel.append(iter))
    for iter in seleccion:
        borraBD(iter)
        listStore.remove(iter)
            
    
                
    
def editaCliente(self, renderer, path, newText, column):
    iter = listStore.get_iter(path)
    listStore.set_value(iter, column, newText)
    actualizaBD(iter)
    
    
        
def insertaCliente(self, datos):
    tmp = []
    for d in datos:
        tmp.append(d.encode('latin-1'))
        cursor.execute('insert into acreditaciones (nombre, direccion, importe, hora) values (%s, %s, %s, %s)', 
                            tmp)
        cursor.execute('select id from acreditaciones where nombre=%s and direccion=%s and importe=%s and hora=%s', 
                            tmp)
        return int(cursor.fetchone()[0])

def borraCliente(self, iter):
    c = cursor
    c.execute('delete from acreditaciones where id = %s', 
              (listStore.get_value(iter, ID),))
        
                
def actualizaCliente(self, iter):
    c = cursor
    c.execute("""update acreditaciones set nombre = %s, direccion = %s,
    importe = %s, hora = %s 
    where id = %s""", (
        listStore.get_value(iter, NOMBRE).encode('latin-1'), 
        listStore.get_value(iter, DIRECCION).encode('latin-1'), 
        listStore.get_value(iter, IMPORTE).encode('latin-1'), 
        listStore.get_value(iter, HORA).encode('latin-1'), 
        listStore.get_value(iter, ID)
        ))

