#!/usr/bin/env python
#coding=utf-8
# -*- coding: utf-8 -*-

import gtk
import pango
from genericlistview import GenericListView

class TreeView(GenericListView):
    """
    This class represents a ListView for bills.
    """
    
    def id_cell_data_function(self, column, cell, model, iter):
            id = model.get_value (iter, 0)
            cell.set_property('text', id)
            column.set_visible(False)
            
    def recogido_cell_data_function(self, column, cell, model, iter):
        recogido = model.get_value (iter, 1)
#        cell.set_property('pixbuf', recogido)
        cell.set_property('activatable', True)
        #cell.set_property( "active", 0 )
        #cell.set_property('markup', '<b>%s</b>' % pagado)
        #cell.set_property('xalign', 0.0)
#        column.set_sizing(gtk.TREE_VIEW_COLUMN_FIXED)
#        column.set_fixed_width(100)        
    
    def credito_cell_data_function(self, column, cell, model, iter):
        credito = model.get_value (iter, 2)
        cell.set_property('pixbuf', credito)
        #cell.set_property('markup', '<b>%s</b>' % pagado)
        cell.set_property('xalign', 0.0)
#        column.set_sizing(gtk.TREE_VIEW_COLUMN_FIXED)
#        column.set_fixed_width(100)                
    

    def servicioadomicilio_cell_data_function(self, column, cell, model, iter):
        servicioadomicilio = model.get_value (iter, 3)
        cell.set_property('pixbuf', servicioadomicilio)
        #cell.set_property('markup', '<b>%s</b>' % pagado)
        cell.set_property('xalign', 0.0)
             
#        column.set_sizing(gtk.TREE_VIEW_COLUMN_FIXED)
#        column.set_fixed_width(100)        

    def nombre_cell_data_function(self, column, cell, model, iter):
        nombre = model.get_value (iter, 4)
        # Format the dueDate field
        cell.set_property('text', nombre)
        cell.set_property('editable', True)
        cell.connect( 'edited', self.callback, model) 
        cell.set_fixed_size(-1, 25)
        font = pango.FontDescription('helvetica 8')
        cell.set_property('font-desc', font)
        column.set_sizing(gtk.TREE_VIEW_COLUMN_FIXED)
        column.set_fixed_width(300)                   
    def direccion_cell_data_function(self, column, cell, model, iter):
        direccion = model.get_value(iter, 5)
        cell.set_property('text', direccion)
        cell.set_property('xalign', 0.0)
        cell.set_fixed_size(-1, 25)
        font = pango.FontDescription('helvetica 8')
        cell.set_property('font-desc', font)
                   
    def callback(self, cell, path, new_text, model):
        """Called when a text cell is edited.  It puts the new text
           in the model so that it is displayed properly."""
        #print "Change '%s' to '%s'" % (model[path][4], new_text)
        model[path][4] = new_text
        return        
    

    # This dictionary represents the columns displayed by the listview.
    # It is indexed by the order you want them to be displayed, followed
    # by the column title and cellrenderer type.
    columns = {
        0: ['ID', gtk.CellRendererText()],
        1: ['RC', gtk.CellRendererToggle()],
        2: ['CR', gtk.CellRendererPixbuf()],
        3: ['S.D.', gtk.CellRendererPixbuf()],
        4: ['NOMBRE', gtk.CellRendererText()],
        5: ['DIRECCION', gtk.CellRendererText()]
        
        }
        
    def __init__(self):
        GenericListView.__init__(self, self.columns)
        # Set the following columns to invisible        
        id = self.get_column(0)
        id.set_cell_data_func(id.get_cell_renderers()[0], self.id_cell_data_function)
        
        recogido = self.get_column(1)
        recogido.set_cell_data_func(recogido.get_cell_renderers()[0], self.recogido_cell_data_function)        
        
        credito = self.get_column(2)
        credito.set_cell_data_func(credito.get_cell_renderers()[0], self.credito_cell_data_function)

        servicioadomicilio = self.get_column(3)
        servicioadomicilio.set_cell_data_func(servicioadomicilio.get_cell_renderers()[0], self.servicioadomicilio_cell_data_function)        
        
        nombre = self.get_column(4)
        nombre.set_cell_data_func(nombre.get_cell_renderers()[0], self.nombre_cell_data_function)

        direccion = self.get_column(5)
        direccion.set_cell_data_func(direccion.get_cell_renderers()[0], self.direccion_cell_data_function)
    