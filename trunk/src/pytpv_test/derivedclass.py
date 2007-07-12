# -*- coding: utf-8 -*-

import gtk
from genericlistview1 import GenericListView1

class BillListView(GenericListView1):
    """
    This class represents a ListView for bills.
    """
    def payee_cell_data_function(self, column, cell, model, iter):
            payee = model.get_value (iter, 1)
            cell.set_property('text', payee)
            #cell.set_property('markup', '<b>%s</b>' % pagado)
            cell.set_property('xalign', 0.0)
            column.set_sizing(gtk.TREE_VIEW_COLUMN_FIXED)
            column.set_fixed_width(300)                      
    #        column.set_sizing(gtk.TREE_VIEW_COLUMN_FIXED)
    #        column.set_fixed_width(100)            
    # This dictionary represents the columns displayed by the listview.
    # It is indexed by the order you want them to be displayed, followed
    # by the column title and cellrenderer type.
    columns = {
        0: [None, gtk.CellRendererPixbuf()],
        1: ['Payee', gtk.CellRendererText()],
        2: ['Amount Due', gtk.CellRendererText()],
        3: ['Due Date', gtk.CellRendererText()]
        
        }
    def __init__(self):
        GenericListView1.__init__(self, self.columns)        
    
        payee = self.get_column(1)
        payee.set_cell_data_func(payee.get_cell_renderers()[0], self.payee_cell_data_function)            