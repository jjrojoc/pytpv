#!/usr/bin/env python
#coding=utf-8

import gtk
from toolbar import Toolbar
from tree import TicketView
from tree import TicketLineaView
from botonera import botonera
class notebook(gtk.Notebook):
    def __init__(self):
        # Main Notebook of PyTPV application
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
        linea = ([1, 1, 3, 'POLLO ASADO', 19.30], [1, 1, 2, '1/2 POLLO', 4.50])
        self.ticketlineaview.addList(linea)
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