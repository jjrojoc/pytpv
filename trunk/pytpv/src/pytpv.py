#!/usr/bin/env python
# -*- coding: utf-8 -*-
from encodings import utf_8

from codificacion import *


#from insertaarticulos import *

# acredita.py  Generador de acreditaciones para congresos
# Copyright (C) 2003 Lorenzo Gil Sanchez <lgs@sicem.biz>
# Este programa es software libre. Puede redistribuirlo y/o modificarlo bajo
# los terminos de la Licencia Publica General de GNU segun es publicada por la
# Free Software Foundation, bien de la version 2 de dicha Licencia o bien
# (segun su eleccion) de cualquier version posterior.
#
# Este programa se distribuye con la esperanza de que sea util, pero SIN
# NINGUNA GARANTIA, incluso sin la garantia MERCANTIL impliￂﾭcita o sin
# garantizar la CONVENIENCIA PARA UN PROPOSITO PARTICULAR. Veaase la Licencia
# Publica General de GNU para mas detalles.
#
# Deberia haber recibido una copia de la Licencia Publica General junto con
# este programa. Si no ha sido asiￂﾭ, escriba a la Free Software Foundation,
# Inc., en 675 Mass Ave, Cambridge, MA 02139, EEUU. 
#
# Puede contactar con el autor mediante la direccion de correo electronico
# lgs@sicem.biz o a la siguiente direccion de correo postal:
# Lorenzo Gil Sanchez. Torre de las Cabezas 8. 18008 Granada. Espaￃﾱa


# librerias para la interfaz grafica
import pygtk
pygtk.require('2.0')
import gtk
import gtk.glade
import gobject
# librerias para generar los pdfs



# librerias para el acceso a base de datos
import MySQLdb

# librerias para ejecutar xpdf y para ver la linea de comandos
import os, os.path, sys

# constantes


CONSULTA_BASE = 'select id, nombre, direccion, importe, hora from acreditaciones'

# para las columnas del listView
ID, NOMBRE, DIRECCION, IMPORTE, HORA = range(5)
ID_TICKET, CANTIDAD, ID_ARTICULO, IMPORTE = range(4)

class Acredita:
    def __init__(self):
        self.db = MySQLdb.connect(db='acreditaciones',
                                  user='root')
        self.cursor = self.db.cursor()
        
        self.widgets = gtk.glade.XML('pytpv.glade')
        self.widgets.signal_autoconnect(self)

        self.listStore = gtk.ListStore(gobject.TYPE_INT,     # id
                                       gobject.TYPE_STRING,  # Nombre
                                       gobject.TYPE_STRING,  # Apellidos
                                       gobject.TYPE_STRING,  # Correo
                                       gobject.TYPE_STRING)  # Rol
    
        self.cargaDatos(CONSULTA_BASE)
        
        self.listView = self.widgets.get_widget('listView')
        self.listView.set_model(self.listStore)
        self.listView.get_selection().set_mode(gtk.SELECTION_MULTIPLE)
        
    
        columns = ['NOMBRE', 'DIRECCION', 'IMP', 'HORA']
        for i in range(len(columns)):
            renderer = gtk.CellRendererText()
            renderer.set_property('editable', True)
            renderer.connect('edited', self.editedCallback, i+1)
            column = gtk.TreeViewColumn(columns[i], renderer, text=(i+1))
            #column.set_resizable(True)
            column.set_spacing(10)
            column.set_alignment(0.5)
            #font = pango.FontDescription('courier bold 12')
            #renderer.set_property('font-desc', font)
            self.listView.append_column(column)
            column.set_sizing(gtk.TREE_VIEW_COLUMN_FIXED)
            column.set_fixed_width(100)
            column.set_sort_column_id(i+1)
            renderer.connect('edited', self.editedCallback, i+1)
            
        
        
        self.ticketstore = gtk.ListStore(gobject.TYPE_INT, #ID_TICKET
                                         gobject.TYPE_STRING, # CATIDAD
                                         gobject.TYPE_STRING,  #DESCRIPCION
                                         gobject.TYPE_STRING)    # Importe    
        
        
        self.treeview3 = self.widgets.get_widget('treeview3')
        self.treeview3.set_model(self.ticketstore)
        self.treeview3.get_selection().set_mode(gtk.SELECTION_MULTIPLE)
        
        
        columnsticketview = ['UNI.', 'DESCRIPCION', 'IMP']
        
        for j in range(len(columnsticketview)):
            render = gtk.CellRendererText()
            render.set_property('editable', True)
            render.connect('edited', self.editedcells, j)
            columna = gtk.TreeViewColumn(columnsticketview[j], render, text=(j))
            columna.set_resizable(True)
            self.treeview3.append_column(columna)
            columna.set_sort_column_id(j)
            render.connect('edited', self.editedcells, j)  
        
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

    def generaAcreditacion(self, canvas, iter, x, y):
        colores = {
            'Visitante': ((0.36, 0.36, 0.36), (0.89, 0.89, 0.89)),
            'Ponente'  : ((0.91, 0.19, 0.19), (0.92, 0.69, 0.69)),
            'Organizacion' : ((0, 0.48, 0.77), (0.45, 0.76, 0.93))
            }
        iconos = {
            'Visitante'    : 'icono-visitante.png',
            'Ponente'      : 'icono-ponente.png',
            'Organizacion' : 'icono-organizacion.png'
            }
        nombre = self.listStore.get_value(iter, NOMBRE)
        if nombre: nombre = nombre.encode('latin-1')
        apellidos = self.listStore.get_value(iter, DIRECCION)
        if apellidos: apellidos = apellidos.encode('latin-1')
        ciudad = self.listStore.get_value(iter, IMPORTE)
        if ciudad: ciudad = ciudad.encode('latin-1')
        if len(ciudad) > 15:
            ciudad = ciudad[:15] + '...'
        grupo = self.listStore.get_value(iter, ORGANIZACION)
        if grupo: grupo = grupo.encode('latin-1')
        if len(grupo) > 20:
            grupo = grupo[:20] + '...'
        rol = self.listStore.get_value(iter, ROL)
        if rol: rol = rol.encode('latin-1')

        icono = Image.open(iconos[rol])
        iconoAncho, iconoAlto = icono.size            
            
        canvas.translate(x, y)
        # dibujo los rectangulos de fondo
        color = colores[rol][0]
        canvas.setFillColorRGB(color[0], color[1], color[2])
        canvas.rect(0, 0, ANCHO, ALTO, stroke=1, fill=1)
        color = colores[rol][1]
        canvas.setFillColorRGB(color[0], color[1], color[2])
        canvas.rect(2*mm, 2*mm, ANCHO-4*mm, ALTO-6*mm-iconoAlto,
                    stroke=0, fill=1)
        
        # ahora el icono
        canvas.drawImage(icono, 2*mm, ALTO-2*mm-iconoAlto)
            
        # dibujo el texto comun
        canvas.setFillColorRGB(1, 1, 1)
        canvas.setFont('Helvetica', 16)
        canvas.drawString(10 + iconoAncho, ALTO-5*mm, 'III')
        canvas.drawString(10 + iconoAncho, ALTO-10*mm, 'jornadas')
        canvas.drawString(10 + iconoAncho, ALTO-15*mm, 'andaluzas')
        canvas.setFont('Helvetica', 12)
        canvas.drawString(10 + iconoAncho, ALTO-20*mm, 'de Software Libre')
        canvas.setFont('Helvetica', 10)
        canvas.setFillColorRGB(0, 0, 0)
        canvas.drawCentredString(ANCHO/2, ALTO-25*mm,
                            'Granada. 14 y 15 de Noviembre')

        canvas.setFont('Helvetica', 18)
        canvas.drawCentredString(ANCHO/2, 35*mm, nombre)
        canvas.drawCentredString(ANCHO/2, 28*mm, apellidos)
        canvas.line(5*mm, 26*mm, ANCHO-5*mm, 26*mm)
        canvas.drawCentredString(ANCHO/2, 20*mm, ciudad)
        if grupo != '' and grupo != None:
            canvas.setFont('Helvetica', 14)
            canvas.drawCentredString(ANCHO/2, 15*mm, grupo)
            
        canvas.setFont('Helvetica', 12)
        canvas.drawString(3*mm, 5*mm, rol)

        canvas.translate(-x, -y)

    def creaPDF(self):
        ancho, alto = A4
        c = canvas.Canvas(NOMBRE_FICHERO, pagesize=A4)
        seleccion = []
        self.listView.get_selection().selected_foreach(
            lambda model, path, iter, sel = seleccion: sel.append(iter))
        i = 0
        x = MARGEN
        y = alto - MARGEN - ALTO
        for iter in seleccion:
            self.generaAcreditacion(c, iter, x, y)
            i += 1
            if i >= self.upp:
                i = 0
                x = MARGEN
                y = alto - MARGEN - ALTO
                c.showPage()
                continue
            
            x += (ANCHO + 1*mm)
            if x + ANCHO > (ancho - MARGEN):
                x = MARGEN
                y -= (ALTO + 1*mm)

            if y < MARGEN:
                x = MARGEN
                y = alto - MARGEN - ALTO
                i = 0
                c.showPage()
                
        c.save()
        
    def vistaPrevia(self, boton, datos=None):
        self.creaPDF()
        os.system('xpdf %s' % NOMBRE_FICHERO)

    def imprimir(self, boton, datos=None):
        self.creaPDF()
        os.system('pdf2ps %s - | lpr' % NOMBRE_FICHERO)
        
    def nuevoAsistente(self, boton, datos=None):
        dialog = self.widgets.get_widget('dlgNuevoAsistente')
        resultado = dialog.run()
        dialog.hide()
        if resultado == gtk.RESPONSE_OK:
            datos = []
            for entry in ['entNombre', 'entApellidos', 'entEmail', 'entCiudad']:
                datos.append(self.widgets.get_widget(entry).get_text())
            

            # lo meto en la base de datos
            id = self.insertaBD(datos)
            datos = [id] + datos
            # lo meto en la interfaz
            self.listStore.prepend(datos)


#    def ticketrow(self, linea):
#        #print 'on_ticketrow_clicked'
#        datos = ['1', 'CALAMARES CON TOMATE Y PIMIENTO', '1.50']
#        
#        
#        self.ticketstore.append(datos)
        
    def ticketrow (self, data=None):
        data = 'select id, unidades, descripcion, precio from articulosa where id=1' 
        c = self.cursor
        c.execute(data)
        data = c.fetchall()
        #data = ["1.00", "2", "9.00"]
        #self.ticketstore.append(datos)
        tmp=[]
        for dato in data:
            ID_TICKET = dato[0]
            tmp.append(dato)
            
        
        data = self.insertalinea(tmp)
        
        data = [ID_TICKET] + data
        self.ticketstore.append(data)
        
            
    def insertalinea (self, data):
        print 'on_buclefor_clicked'
        tmp = []
        for d in data:
            tmp.append(d)
        self.cursor.execute('insert into acreditaciones.ventas (cantidad, id_articulo, importe) values (%s, %s, %s)', tmp)
            
        self.cursor.execute('SELECT id_ticket from ventas where ventas.cantidad =%s AND ventas.id_articulo = %s AND ventas.importe=%s', tmp)
        return int(self.cursor.fetchone()[0])
                
            
        
        
    
    def quitaAsistente(self, boton, datos=None):
        seleccion = []
        self.listView.get_selection().selected_foreach(
            lambda model, path, iter, sel = seleccion: sel.append(iter))
        for iter in seleccion:
            self.borraBD(iter)
            self.listStore.remove(iter)
            
    def run(self):
        gtk.main()

    def editedCallback(self, renderer, path, newText, column):
        iter = self.listStore.get_iter(path)
        self.listStore.set_value(iter, column, newText)
        self.actualizaBD(iter)
    
    def editedcells(self, render, path, newTex, columna):
        iter = self.ticketstore.get_iter(path)
        self.ticketstore.set_value(iter, columna, newTex)
    
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

    def salir(self, boton, datos=None):
        gtk.main_quit()

    def preferencias(self, boton, datos=None):
        dialog = self.widgets.get_widget('dlgPreferencias')
        resultado = dialog.run()
        dialog.hide()
        if resultado == gtk.RESPONSE_OK:
            self.upp = self.widgets.get_widget('sbtnUPP').get_value_as_int()
                
if __name__ == '__main__':
    a = Acredita()
    a.run()
