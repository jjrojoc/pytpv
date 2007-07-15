#!/usr/bin/env python
#coding=utf-8

# PyTPV, software point of sale for restaurant, bar and pizzeria.
# Copyright (C) 2007 Juan Jose Rojo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Can you contact with author by means of email: <jjrojoc@gmail.com> or the
# next postal address:
# Juan Jose Rojo. San Lazaro, 13. 30840 Alhama de Murcia. Murcia. Spain
# This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
# This is free software, and you are welcome to redistribute it
# under certain conditions; type `show c' for details.

import gtk
from toolbar import Toolbar
from tree import TicketView, TicketLineaView, ClientesView, ArticulosView,\
                 CreditoView, HistoricoView
from horizontalbuttonbox import HorizontalButtonBox
from botonera import botonera
class notebook(gtk.Notebook):
    def __init__(self):
        """
        Main Notebook of PyTPV application
        """
        
        gtk.Notebook.__init__(self)
        
        
        for n in 'TPV', 'STOCK', 'CLIENTES', 'ARTICULOS', 'CREDITO', 'HISTORICO':
            vbox = gtk.VBox()
                      
            label = gtk.Label(n)
            label.set_padding(15, 15)
            
            self.set_homogeneous_tabs(True)
            self.append_page(vbox, label)
            
        self.vbox = gtk.VBox()    
        self.hbox = gtk.HBox() 
        self.toolbar = Toolbar()
        
        self._populate_toolbar()   
        #self.ticketstore = TicketStore()
        self.ticketview = TicketView(self)
        #self.ticketlineastore = TicketLineaStore()
        self.ticketlineaview = TicketLineaView(self)
        self.clientesview = ClientesView(self)
        self.articulosview = ArticulosView(self)
        self.creditoview = CreditoView(self)
        self.historicoview = HistoricoView(self)
        
        self.scrolledwindow = gtk.ScrolledWindow()
        self.scrolledwindow.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_ALWAYS)
             
        self.get_nth_page(0).pack_start(self.toolbar, expand=False, fill=True, padding=0)
        
        self.get_nth_page(0).pack_start(self.hbox)
        
        self.hbox.pack_start(self.scrolledwindow, expand=True, fill=True, padding=0)
                
        self.scrolledwindow.add_with_viewport(self.ticketview)
        linea= ([None, gtk.STOCK_APPLY, gtk.STOCK_NO, gtk.STOCK_ABOUT, 'JUAN JOSE ROJO', 'DE LA NADA, 45 BAJO-B', '45.50', '13.45'])
        self.ticketview.add(linea)
        linea= ([None, gtk.STOCK_CANCEL, gtk.STOCK_OK, gtk.STOCK_HOME, 'LEANDRO TERRES', 'A DONDE SEA, 21', '15.20', '14.30'])
        self.ticketview.add(linea)
        self.scrolledwindow.set_size_request(360, 300)
        
        self.hbox.pack_start(self.vbox)
        
        self.scrolledwindow2 = gtk.ScrolledWindow()
        self.scrolledwindow2.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        
        self.vbox.pack_start(self.scrolledwindow2, expand=True, fill=True, padding=0)
               
        self.scrolledwindow2.add_with_viewport(self.ticketlineaview)
        
        linea = ([1, 1, 3, 'POLLO ASADO', 19.30], [1, 1, 2, '1/2 POLLO', 4.50], [1, 1, 2, '1/2 POLLO', 4.50], [1, 1, 2, '1/2 POLLO', 4.50], [1, 1, 2, '1/2 POLLO', 4.50], [1, 1, 2, '1/2 POLLO', 4.50], [1, 1, 2, '1/2 POLLO', 4.50], [1, 1, 2, '1/2 POLLO', 4.50], [1, 1, 2, '1/2 POLLO', 4.50], [1, 1, 2, '1/2 POLLO', 4.50], [1, 1, 2, '1/2 POLLO', 4.50], [1, 1, 2, '1/2 POLLO', 4.50])
        self.ticketlineaview.addList(linea)
        
        
        self.hbuttonbox = HorizontalButtonBox()
        self.get_nth_page(2).pack_start(self.hbuttonbox, expand=False, fill=False, padding=0)
        
        self.scrolledwindow3 = gtk.ScrolledWindow()
        self.scrolledwindow3.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_ALWAYS)
        self.get_nth_page(2).pack_start(self.scrolledwindow3, expand=True, fill=True, padding=0)   
        self.scrolledwindow3.add_with_viewport(self.clientesview)
        
        self.hbuttonbox = HorizontalButtonBox()
        self.get_nth_page(3).pack_start(self.hbuttonbox, expand=False, fill=False, padding=0)
                
        self.scrolledwindow4 = gtk.ScrolledWindow()
        self.scrolledwindow4.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_ALWAYS)
        self.get_nth_page(3).pack_start(self.scrolledwindow4, expand=True, fill=True, padding=0)   
        self.scrolledwindow4.add_with_viewport(self.articulosview)
                        
        self.hbuttonbox = HorizontalButtonBox()
        self.get_nth_page(4).pack_start(self.hbuttonbox, expand=False, fill=False, padding=0)
                        
        self.scrolledwindow5 = gtk.ScrolledWindow()
        self.scrolledwindow5.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_ALWAYS)
        self.get_nth_page(4).pack_start(self.scrolledwindow5, expand=True, fill=True, padding=0)   
        self.scrolledwindow5.add_with_viewport(self.creditoview)        
        
        self.hbuttonbox = HorizontalButtonBox()
        self.get_nth_page(5).pack_start(self.hbuttonbox, expand=False, fill=False, padding=0)
                
        self.scrolledwindow6 = gtk.ScrolledWindow()
        self.scrolledwindow6.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_ALWAYS)
        self.get_nth_page(5).pack_start(self.scrolledwindow6, expand=True, fill=True, padding=0)   
        self.scrolledwindow6.add_with_viewport(self.historicoview)        
        
        self.table = gtk.Table(3, 3)
        self.table.set_homogeneous(True)
        self.vbox.pack_start(self.table, expand=False, fill=True, padding=2)
        
        self.botonera = botonera()
        self.hbox.pack_start(self.botonera, expand=True, fill=True, padding=2)
        
        aopt = gtk.FILL|gtk.SHRINK
        c = 0
        r = 0        
        button = gtk.Button('pp')
        button.set_size_request(100, 80)
        self.table.attach(button, c, c+1, r, r+1, aopt, aopt, 0, 0)
       
        button = gtk.Button('pp')
        button.set_size_request(100, 80)
        self.table.attach(button, c+1, c+2, r, r+1, aopt, aopt, 0, 0)
               
        button = gtk.Button('pp')
        button.set_size_request(100, 80)
        button.show()
        self.table.attach(button, c+2, c+3, r, r+1, aopt, aopt, 0, 0)
        
        button = gtk.Button('pp')
        button.set_size_request(100, 80)
        self.table.attach(button, c, c+1, r+1, r+2, aopt, aopt, 0, 0)        
        
        button = gtk.Button('pp')
        button.set_size_request(100, 80)
        self.table.attach(button, c+1, c+2, r+1, r+2, aopt, aopt, 0, 0)
        
        button = gtk.Button('pp')
        button.set_size_request(100, 80)
        self.table.attach(button, c+2, c+3, r+1, r+2, aopt, aopt, 0, 0)
        
        button = gtk.Button('pp')
        button.set_size_request(100, 80)
        self.table.attach(button, c, c+1, r+2, r+3, aopt, aopt, 0, 0)
        
        button = gtk.Button('pp')
        button.set_size_request(100, 80)
        self.table.attach(button, c+1, c+2, r+2, r+3, aopt, aopt, 0, 0)
        
        button = gtk.Button('pp')
        button.set_size_request(100, 80)
        self.table.attach(button, c+2, c+3, r+2, r+3, aopt, aopt, 0, 0)
        
                 
    def _populate_toolbar(self):
#        self.toolbar.add_stock(gtk.STOCK_NEW, "Add a new record", self.on_mnuNew_clicked)
#        self.toolbar.add_stock(gtk.STOCK_EDIT, "Edit a record", self.on_mnuEdit_clicked)
#        self.toolbar.add_stock(gtk.STOCK_DELETE, "Delete selected record", self.on_mnuDelete_clicked)
#        self.toolbar.add_space()
#        self.toolbar.add_button(gtk.STOCK_APPLY, "Paid", "Mark as paid", self.on_mnuPaid_clicked)
#        self.toolbar.add_button(gtk.STOCK_UNDO, "Not Paid", "Mark as not paid", self.on_mnuNotPaid_clicked)
#        self.toolbar.add_space()
        self.toolbar.add_stock(gtk.STOCK_ABOUT, "About the application", self.borralinea)
#        self.toolbar.add_space()
        self.toolbar.add_stock(gtk.STOCK_CLOSE, "Quit the application", self.delete)

    def on_mnuAbout_clicked(self, button):
        pass
    def delete(self, widget, event=None):
        # Show the dialog for close application
        from kiwi.ui.dialogs import yesno
        from gtk import RESPONSE_YES
        from gtk import RESPONSE_NO
        
        resp = yesno('Desea cerrar PyTPV?')
        if resp == RESPONSE_YES:
            gtk.main_quit()
            return False
        if resp == RESPONSE_NO:
            return True
        
    def borralinea(self, iter):
        self.ticketview.remove()