#!/usr/bin/env python
#coding=utf-8
# -*- coding: utf-8 -*-

import gtk
import pango
from genericlistview import GenericListView

class StockView(GenericListView):
    """
    This class represents a Articlesview for bills.
    """
    
    def id_cell_data_function(self, column, cell, model, iter):
            id = model.get_value (iter, 0)
            cell.set_property('text', id)
            #column.set_visible(False)
    
    def familia_cell_data_function(self, column, cell, model, iter):
        familia = model.get_value (iter, 1)
        cell.set_property('text', familia)
        #cell.set_property('markup', '<b>%s</b>' % pagado)
        #cell.set_property('xalign', 0.0)
#        column.set_sizing(gtk.TREE_VIEW_COLUMN_FIXED)
#        column.set_fixed_width(100)        
    
    def descripcion_cell_data_function(self, column, cell, model, iter):
        descripcion = model.get_value (iter, 2)
        cell.set_property('text', descripcion)
        #cell.set_property('markup', '<b>%s</b>' % pagado)
        cell.set_property('xalign', 0.0)
#        column.set_sizing(gtk.TREE_VIEW_COLUMN_FIXED)
#        column.set_fixed_width(100)                
    

    def stock_cell_data_function(self, column, cell, model, iter):
        stock = model.get_value (iter, 3)
        cell.set_property('text', stock)
        #cell.set_property('markup', '<b>%s</b>' % pagado)
        cell.set_property('xalign', 0.0)
             
#        column.set_sizing(gtk.TREE_VIEW_COLUMN_FIXED)
#        column.set_fixed_width(100)        

    def stockminimo_cell_data_function(self, column, cell, model, iter):
        stockminimo = model.get_value (iter, 4)
        # Format the dueDate field
        cell.set_property('text', stockminimo)
#        cell.set_property('editable', True)
#        cell.connect( 'edited', self.callback, model) 
        cell.set_fixed_size(-1, 25)
        font = pango.FontDescription('helvetica 8')
        cell.set_property('font-desc', font)
                   
    def precioventa_cell_data_function(self, column, cell, model, iter):
        precioventa = model.get_value(iter, 5)
        cell.set_property('text', precioventa)
        cell.set_property('xalign', 0.0)
        cell.set_fixed_size(-1, 25)
        font = pango.FontDescription('helvetica 8')
        cell.set_property('font-desc', font)
        
    def imagen_cell_data_function(self, column, cell, model, iter):
        imagen = model.get_value(iter, 6)
        cell.set_property('text', imagen)
        cell.set_property('xalign', 0.0)
        cell.set_fixed_size(-1, 25)
        font = pango.FontDescription('helvetica 8')
        cell.set_property('font-desc', font)
        
    
    

    # This dictionary represents the columns displayed by the listview.
    # It is indexed by the order you want them to be displayed, followed
    # by the column title and cellrenderer type.
    columns = {
        0: ['ID', gtk.CellRendererText()],
        1: ['FAMILIA', gtk.CellRendererText()],
        2: ['DESCRIPCION', gtk.CellRendererText()],
        3: ['STOCK', gtk.CellRendererText()],
        4: ['STOCK MINIMO', gtk.CellRendererText()],
        5: ['PRECIO VENTA', gtk.CellRendererText()],
        6: ['IMAGEN', gtk.CellRendererText()]
        
        
        }
        
    def __init__(self):
        GenericListView.__init__(self, self.columns)
        # Set the following columns to invisible        
        id = self.get_column(0)
        id.set_cell_data_func(id.get_cell_renderers()[0], self.id_cell_data_function)
        
        familia = self.get_column(1)
        familia.set_cell_data_func(familia.get_cell_renderers()[0], self.familia_cell_data_function)        
        
        descripcion = self.get_column(2)
        descripcion.set_cell_data_func(descripcion.get_cell_renderers()[0], self.descripcion_cell_data_function)

        stock = self.get_column(3)
        stock.set_cell_data_func(stock.get_cell_renderers()[0], self.stock_cell_data_function)        
        
        stockminimo = self.get_column(4)
        stockminimo.set_cell_data_func(stockminimo.get_cell_renderers()[0], self.stockminimo_cell_data_function)

        precioventa = self.get_column(5)
        precioventa.set_cell_data_func(precioventa.get_cell_renderers()[0], self.precioventa_cell_data_function)
        
        imagen = self.get_column(6)
        imagen.set_cell_data_func(imagen.get_cell_renderers()[0], self.imagen_cell_data_function)
        