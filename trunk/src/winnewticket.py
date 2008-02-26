#!/usr/bin/env python
#coding=utf-8

import gtk, gtk.glade
from wincalendar import dlgCalendar
from tree import ClientesView
from ddbb import DBAccess

class winNewTicket:

    def __init__(self):
        
        self.db = DBAccess()
        self.clients = self.db.table_clients()
        
        self.widget = gtk.glade.XML('pytpv.glade', 'winNewTicket')
        self.winnewticket= self.widget.get_widget('winNewTicket')
        self.winnewticket.show()
        self.widget.signal_autoconnect(self)
        
        self.clientesview = ClientesView(self)
        self.scrollednewticket = self.widget.get_widget('scrolledNewTicket')
        self.scrollednewticket.add(self.clientesview)
        self.clientesview.set_size_request(400, 250)
        
        for client in self.clients:
            self.clientesview.add(client)
        self.clientesview.show()
            
    def new(self):
        print 'A new %s has been created' % self.__class__.__name__
    
    
    def on_tglNameNewTicket_toggled(self, widget, args=[]):
        print 'on_tglNameNewTicket_toggled called with self.%s' % widget.get_name()
    
    
    def on_tglAddressNewTicket_toggled(self, widget, args=[]):
        print 'on_tglAddressNewTicket_toggled called with self.%s' % widget.get_name()
    
    
    def on_tglPhoneNewTicket_toggled(self, widget, args=[]):
        print 'on_tglPhoneNewTicket_toggled called with self.%s' % widget.get_name()
    
    
    def on_btnShowCalendar_clicked(self, widget):
        print 'on_btnShowCalendar_clicked called with self.%s' % widget.get_name()
        dlgcalendar = dlgCalendar(self).newDate(self)
        c2 = self.widget.get_widget('entDateNewTicket')
        c2.set_text(dlgcalendar)
    
    def on_btnAddNewTicket_clicked(self, widget, args=[]):
        print 'on_btnAddNewTicket_clicked called with self.%s' % widget.get_name()
        
        
    def on_btnAcceptNewTicket_clicked(self, widget, args=[]):
        print 'on_btnAcceptNewTicket_clicked called with self.%s' % widget.get_name()
    
    
    def on_btnCancelNewTicket_clicked(self, widget, args=[]):
        print 'on_btnCancelNewTicket_clicked called with self.%s' % widget.get_name()
        self.winnewticket.hide()