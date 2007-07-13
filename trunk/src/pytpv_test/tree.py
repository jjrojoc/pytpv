#!/usr/bin/env python
#coding=utf-8
# -*- coding: utf-8 -*-

import gtk
import gobject
import pango

       
class TicketView(gtk.TreeView):
    def __init__(self, ticketstore):
        # This class represent ticketview of ticketstore
        gtk.TreeView.__init__(self)    
    
        # Defines the TreeStore
        self.ticketstore = gtk.ListStore(str, str, str, str, str, str, str, str)
        # Associates the listStore to the ListView object
        self.set_model(self.ticketstore)        
        
        self.get_selection().set_mode(gtk.SELECTION_SINGLE)
        self.set_rules_hint(True)

        columns = ['ID', 'RC', 'CR', 'SD', 'NOMBRE', 'DIRECCION', 'IMP', 'HORA']
        for i in range(len(columns)):
            pixbuf = gtk.CellRendererPixbuf()
            renderer = gtk.CellRendererText()
            renderer.set_property('editable', True)
            renderer.connect('edited', self.editedCallback, i)
            renderer.set_fixed_size(-1, 25)
            if i == 0:
                column = gtk.TreeViewColumn(columns[i], renderer, text=(i))
                column.set_visible(False)
            elif i == 1:
                column = gtk.TreeViewColumn(columns[i], pixbuf, stock_id=(i))
            elif i == 2:
                column = gtk.TreeViewColumn(columns[i], pixbuf, stock_id=(i))
            elif i == 3:
                column = gtk.TreeViewColumn(columns[i], pixbuf, stock_id=(i))
            elif i == 4:
                column = gtk.TreeViewColumn(columns[i], renderer, text=(i))
            elif i == 5:
                column = gtk.TreeViewColumn(columns[i], renderer, text=(i))
            elif i == 6:
                column = gtk.TreeViewColumn(columns[i], renderer, text=(i))
            else:
                column = gtk.TreeViewColumn(columns[i], renderer, text=(i))
            
            #column.set_resizable(True)
            column.set_spacing(10)
            column.set_alignment(0.5)
            font = pango.FontDescription('helvetica 10')
            renderer.set_property('font-desc', font)
            self.append_column(column)
#            column.set_sizing(gtk.TREE_VIEW_COLUMN_FIXED)
#            column.set_fixed_width(100)
            column.set_sort_column_id(i+1)
            renderer.connect('edited', self.editedCallback, i)
            
    def editedCallback(self, renderer, path, newText, column):
        iter = self.ticketstore.get_iter(path)
        self.ticketstore.set_value(iter, column, newText)
        #self.actualizaBD(iter)
        
    def add(self, value):
        
        return self.ticketstore.append(value)    
    
    
    def remove(self):
        
        #http://eccentric.cx/misc/pygtk/pygtkfaq.html#13.8
        selection = self.get_selection() 
        model, iter = selection.get_selected()
        if iter:
          path = model.get_path(iter)
          model.remove(iter)
          
          selection.select_path(path)

          
          if not selection.path_is_selected(path):
             row = path[0]-1
             
             if row >= 0:
                selection.select_path((row,))

    def getSelectedRow(self):
        
        selection = self.get_selection()
        model, paths = selection.get_selected_rows()

        # Returns first selected row
        return paths[0]

    def getSelectedItem(self, index):
        
        selection = self.get_selection()
        model, iter, = selection.get_selected()
        return  self.ticketstore.get_value(iter, index)

    def getCount(self):
        

        return len(self.ticketstore)
    
    
    

        
class TicketLineaView(gtk.TreeView):
    def __init__(self, ticketlineastore):
        # This class represent ticketview of ticketstore
        gtk.TreeView.__init__(self)    
    
        self.ticketlineastore = gtk.ListStore(str, str, str, str, str)
        # Associates the listStore to the ListView object
        
        self.set_model(self.ticketlineastore)
        #self.cargaDatos(CONSULTA_BASE)
        self.get_selection().set_mode(gtk.SELECTION_MULTIPLE)
        self.set_rules_hint(True)

        columnsticketview = ['ID', 'TICKET_FK_ID', 'UNI', 'DESCRIPCION', 'IMP']
                
        for j in range(len(columnsticketview)):
            render = gtk.CellRendererText()
            render.set_property('editable', True)
            render.connect('edited', self.editedcells, j)
            render.set_fixed_size(-1, 25)
            columna = gtk.TreeViewColumn(columnsticketview[j], render, text=(j))
            columna.set_resizable(True)
            if j == 0:
                columna.set_visible(False)
            elif j == 1:
                columna.set_visible(False)
            self.append_column(columna)
            columna.set_sort_column_id(j)
            render.connect('edited', self.editedcells, j)
        
    def editedcells(self, render, path, newTex, columna):
        iter = self.ticketlineastore.get_iter(path)
        self.ticketlineastore.set_value(iter, columna, newTex)
        #self.actualizaticketstore(iter)
        
        
    def add(self, value):
            
        return self.ticketlineastore.append(value)    
    
    
    def addList(self, values):
        
        # Removes the model so the addition is quicker
        self.set_model(None)
        # Freezes list so to cancel refresh event
        self.freeze_child_notify()

        for value in values:
            self.ticketlineastore.append(value)

        # set model back
        self.set_model(self.ticketlineastore)
        # Unfreeze the list
        self.thaw_child_notify()
    
    
    
    def remove(self):
        
        #http://eccentric.cx/misc/pygtk/pygtkfaq.html#13.8
        selection = self.get_selection() 
        model, iter = selection.get_selected()
        if iter:
          path = model.get_path(iter)
          model.remove(iter)
          
          selection.select_path(path)

          
          if not selection.path_is_selected(path):
             row = path[0]-1
             
             if row >= 0:
                selection.select_path((row,))

    def getSelectedRow(self):
        
        selection = self.get_selection()
        model, paths = selection.get_selected_rows()

        # Returns first selected row
        return paths[0]

    def getSelectedItem(self, index):
        
        selection = self.get_selection()
        model, iter, = selection.get_selected()
        return  self.ticketlineastore.get_value(iter, index)

    def getCount(self):
        

        return len(self.ticketlineastore)
