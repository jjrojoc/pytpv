#!/usr/bin/env python
#coding=utf-8
# -*- coding: utf-8 -*-

import gtk
import gobject
import pango

class TicketStore(gtk.ListStore):
    def __init__(self):
        # Store for sales
        gtk.ListStore.__init__(self, str, gtk.gdk.Pixbuf, gtk.gdk.Pixbuf, gtk.gdk.Pixbuf, str, str) 
    """
    This class represents a ListStore for Sales.
    """
        
        #self(str, gtk.gdk.Pixbuf, gtk.gdk.Pixbuf, gtk.gdk.Pixbuf, str, str)  # Id, Recogido, Credito, Servicio a Domicilio, Nombre, Direccion, Importe, Hora
#        print self    
        
class TicketView(gtk.TreeView):
    def __init__(self, TicketStore):
        # This class represent ticketview of ticketstore
        gtk.TreeView.__init__(self)    
    
        self.set_model(TicketStore)
        #self.cargaDatos(CONSULTA_BASE)
        self.get_selection().set_mode(gtk.SELECTION_MULTIPLE)
        self.set_rules_hint(True)

        columns = ['Recogido', 'Credito', 'S.D.', 'NOMBRE', 'DIRECCION']
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
            self.append_column(column)
#            column.set_sizing(gtk.TREE_VIEW_COLUMN_FIXED)
#            column.set_fixed_width(100)
            column.set_sort_column_id(i+1)
            renderer.connect('edited', self.editedCallback, i+1)
            
    def editedCallback(self, renderer, path, newText, column):
        iter = self.listStore.get_iter(path)
        self.listStore.set_value(iter, column, newText)
        self.actualizaBD(iter)
        

class TicketLineaStore(gtk.ListStore):
    def __init__(self):
        # Store for sales
        gtk.ListStore.__init__(self, int, str, str) 
    """
    This class represents a ListStore for Sales.
    """
        
        #self(str, gtk.gdk.Pixbuf, gtk.gdk.Pixbuf, gtk.gdk.Pixbuf, str, str)  # Id, Recogido, Credito, Servicio a Domicilio, Nombre, Direccion, Importe, Hora
#        print self    
        
class TicketLineaView(gtk.TreeView):
    def __init__(self, TicketLineaStore):
        # This class represent ticketview of ticketstore
        gtk.TreeView.__init__(self)    
    
        self.set_model(TicketLineaStore)
        #self.cargaDatos(CONSULTA_BASE)
        self.get_selection().set_mode(gtk.SELECTION_MULTIPLE)
        self.set_rules_hint(True)

        columnsticketview = ['UNI', 'DESCRIPCION', 'IMP']
                
        for j in range(len(columnsticketview)):
            render = gtk.CellRendererText()
            render.set_property('editable', True)
            render.connect('edited', self.editedcells, j+1)
            render.set_fixed_size(-1, 25)
            columna = gtk.TreeViewColumn(columnsticketview[j], render, text=(j+1))
            columna.set_resizable(True)
            self.append_column(columna)
            columna.set_sort_column_id(j+1)
            render.connect('edited', self.editedcells, j+1)
        
    def editedcells(self, render, path, newTex, columna):
        iter = self.ticketstore.get_iter(path)
        self.ticketstore.set_value(iter, columna, newTex)
        self.actualizaticketstore(iter)        