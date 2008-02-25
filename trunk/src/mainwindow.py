#!/usr/bin/python
import pygtk
pygtk.require('2.0')

import gtk
import gtk.glade
from ddbb import DBAccess
from tree import (ClientesView, TicketView, TicketLineaView, ArticulosView, \
                  CreditoView, HistoricoView)
from dialogclients import dlgClients
from dialogarticles import dlgArticles
from aboutdialog import dlgAbout
from winnewticket import winNewTicket
from winfamilys import winFamilys
from buttonbox import buttonsBox
from botonera import Botonera
from utils import *
#from prueba_botonera import Buttons

#basic_rc =  """
#style "basic_style" {
#    GtkPaned::handle_size = 4
#    GtkRange::slider_width = 30
#    GtkTreeView::horizontal-separator = 0
#    GtkTreeView::vertical-separator = 0
#    }               
#class "GtkWidget" style "basic_style"
#"""
#gtk.rc_parse_string(basic_rc) 


class MainWindow:
    def __init__(self):
        self.widget = gtk.glade.XML('pytpv.glade')
        window = self.widget.get_widget('mainwindow')
        
        self.clientesview = ClientesView(self)
        self.ticketview = TicketView(self)
        self.ticketview.set_size_request(500, 309)
        self.ticketlineaview = TicketLineaView(self)
        self.ticketlineaview.set_size_request(300, -1)
        self.articlesview = ArticulosView(self)
        self.creditoview = CreditoView(self)
        self.historicoview = HistoricoView(self)
        
        self.scrolledticket = self.widget.get_widget('scrolledTicket')
        self.scrolledticketlinea = self.widget.get_widget('scrolledTicketLinea')
        self.scrolledarticles = self.widget.get_widget('scrolledArticles')
        self.scrolledclients = self.widget.get_widget('scrolledClients')
        self.scrolledhistory = self.widget.get_widget('scrolledHistory')
        self.scrolledcredit = self.widget.get_widget('scrolledCredit')
        
        self.scrolledticket.add(self.ticketview)
        self.scrolledticketlinea.add(self.ticketlineaview)
        self.scrolledarticles.add(self.articlesview)
        self.scrolledclients.add(self.clientesview)
        self.scrolledhistory.add(self.historicoview)
        self.scrolledcredit.add(self.creditoview)
        linea = (1, 1, 1, 'POLLO ASADO', 9.00)
        self.ticketlineaview.add(linea)
        linea = (1, 1, 1, 1, 'JUAN JOSE ROJO', ' SAUCE, 7', '13:30', 45)
        self.ticketview.add(linea)
        
        hbox = self.widget.get_widget('hbox1')
        self.buttonbox = buttonsBox()
        #self.buttonbox = Buttons()
        hbox.pack_start(self.buttonbox, False, False)
        
        window.show_all()
        
        self.db = DBAccess()
        self.clients = DBAccess().table_clients()
        self.dbclients = DBAccess().select(self.clients)
        #print self.dbclients
        if self.dbclients <> 0:
            for row in self.dbclients:
                self.clientesview.add(row)
            
        self.articles = DBAccess().table_articles()
        self.dbarticles = DBAccess().select(self.articles)
        self.family = self.db.table_family()
        
        if self.dbarticles <> 0:
            
            for row in self.dbarticles:
                print "%-5s %-5s %-5s" % (row[:-4])
                
                familyname = self.family.busqueda('familia', 'id=%s' % (row[1]))
                #print familyname[1]
                datos = row[0], familyname[1], row[2], ("%0.2f" %row[3]), \
                ("%0.2f" %row[4]), ("%0.2f" %row[5]), row[6]
                
                self.articlesview.add(datos)
                
        self.widget.signal_autoconnect(self)
        
             
    def on_mainwindow_destroy(self, widget, args=[]):
        print 'on_mainwindow_destroy called with self.%s' % widget.get_name()
        gtk.main_quit()
        print 'aplicacion destruida'
    
    
    def on_btnNewTicket_clicked(self, widget, args=[]):
        print 'on_btnNewTicket_clicked called with self.%s' % widget.get_name()
        winnewticket = winNewTicket()
        
    
    def on_btnEditTicket_clicked(self, widget, args=[]):
        print 'on_btnEditTicket_clicked called with self.%s' % widget.get_name()
    
    
    def on_btnDelTicket_clicked(self, widget, args=[]):
        print 'on_btnDelTicket_clicked called with self.%s' % widget.get_name()
    
    
    def on_btnOrder_clicked(self, widget, args=[]):
        print 'on_btnOrder_clicked called with self.%s' % widget.get_name()
    

    def on_btnDeselect_clicked(self, widget, args=[]):
        print 'on_btnDeselect_clicked called with self.%s' % widget.get_name()
    

    def on_btnDelivery_clicked(self, widget, args=[]):
        print 'on_btnDelivery_clicked called with self.%s' % widget.get_name()
    

    def on_btnCreditDelivery_clicked(self, widget, args=[]):
        print 'on_btnCreditDelivery_clicked called with self.%s' % widget.get_name()
    

    def on_btnHideOrder_clicked(self, widget, args=[]):
        print 'on_btnHideOrder_clicked called with self.%s' % widget.get_name()
    

    def on_btnHideDelivery_clicked(self, widget, args=[]):
        print 'on_btnHideDelivery_clicked called with self.%s' % widget.get_name()
   

    def on_btnHideHides_clicked(self, widget, args=[]):
        print 'on_btnHideHides_clicked called with self.%s' % widget.get_name()
    

    def on_btnShowHides_clicked(self, widget, args=[]):
        print 'on_btnShowHides_clicked called with self.%s' % widget.get_name()
   

    def on_btnShowAll_clicked(self, widget, args=[]):
        print 'on_btnShowAll_clicked called with self.%s' % widget.get_name()
    

    def on_btnCredit_clicked(self, widget, args=[]):
        print 'on_btnCredit_clicked called with self.%s' % widget.get_name()
   

    def on_entFilterTicket_changed(self, widget, args=[]):
        print 'on_entFilterTicket_changed called with self.%s' % widget.get_name()
    

    def on_btnCleanTicketFilter_clicked(self, widget, args=[]):
        print 'on_btnCleanTicketFilter_clicked called with self.%s' % widget.get_name()
        a = self.widget.get_widget('entFilterTicket')
        a.delete_text(0, -1)
   

    def on_button_CloseTicket_clicked(self, widget, args=[]):
        print 'on_button_CloseTicket_clicked called with self.%s' % widget.get_name()
   
    
    def on_button_Ticket_clicked(self, widget, args=[]):
        print 'on_button_Ticket_clicked called with self.%s' % widget.get_name()
    

    def on_button_Comanda_clicked(self, widget, args=[]):
        print 'on_button_Comanda_clicked called with self.%s' % widget.get_name()
    

    def on_button_ExecuteDeliverys_clicked(self, widget, args=[]):
        print 'on_button_ExecuteDeliverys_clicked called with self.%s' % widget.get_name()
    

    def on_button_CashRegister_clicked(self, widget, args=[]):
        print 'on_button_CashRegister_clicked called with self.%s' % widget.get_name()
    

    def on_button_ChangeCash_clicked(self, widget, args=[]):
        print 'on_button_ChangeCash_clicked called with self.%s' % widget.get_name()
    

    def on_btnAddArticle_clicked(self, widget, args=[]):
        print 'on_btnAddArticle_clicked called with self.%s' % widget.get_name()
        articulos = dlgArticles().NewArticle(self, widget)
        if articulos != None:
            self.articlesview.prepend(articulos)
            self.articlesview.scroll_to_cell(0)
            

    def on_btnEditArticle_clicked(self, widget, args=[]):
        print 'on_btnEditArticle_clicked called with self.%s' % widget.get_name()
        datos = []
        for item in range(7):
            it = self.articlesview.getSelectedItem(item)
            datos.append(it)
        editarticles = dlgArticles().EditArticle(datos)
        print editarticles
        
        if editarticles:
            a = 1
            b = 1
            for x in range(6):
                self.articlesview.update(iter, a, editarticles[b])
                a += 1
                b += 1
            print editarticles
    

    def on_btnDelArticle_clicked(self, widget, args=[]):
        print 'on_btnDelArticle_clicked called with self.%s' % widget.get_name()
        item = self.articlesview.getSelectedItem(0)
        DBAccess().remove(self.articles, item)
        self.articlesview.remove()
    

    def on_btnPrintArticles_clicked(self, widget, args=[]):
        print 'on_btnPrintArticles_clicked called with self.%s' % widget.get_name()
    

    def on_entFilterArticles_changed(self, widget, args=[]):
        print 'on_entFilterArticles_changed called with self.%s' % widget.get_name()
    

    def on_btnCleanFilterArticles_clicked(self, widget, args=[]):
        print 'on_btnCleanFilterArticles_clicked called with self.%s' % widget.get_name()
    

    def on_btnAddClient_clicked(self, widget, args=[]):
        print 'on_btnAddClient_clicked called with self.%s' % widget.get_name()
        clientes = dlgClients().NewClient(self, widget)
        if clientes != None:
            self.clientesview.prepend(clientes)
            self.clientesview.scroll_to_cell(0)
   

    def on_btnEditClient_clicked(self, widget, args=[]):
        print 'on_btnEditClient_clicked called with self.%s' % widget.get_name()
        datos = []
        
        for item in range(6):
            it = self.clientesview.getSelectedItem(item)
            datos.append(it)
        
        editclients = dlgClients().EditClient(datos)
    
        if editclients:
            a = 1
            b = 1
            for x in range(5):
                self.clientesview.update(iter, a, editclients[b])
                a += 1
                b += 1
            print editclients
    

    def on_btnDelClient_clicked(self, widget, args=[]):
        print 'on_btnDelClient_clicked called with self.%s' % widget.get_name()
        item = self.clientesview.getSelectedItem(0)
        DBAccess().remove(self.clients, item)
        self.clientesview.remove()
    

    def on_btnPrintClients_clicked(self, widget, args=[]):
        print 'on_btnPrintClients_clicked called with self.%s' % widget.get_name()
    

    def on_entFilterClients_changed(self, widget, args=[]):
        print 'on_entFilterClients_changed called with self.%s' % widget.get_name()
        self.clientesview.clear()
        
        datos = self.db.filter(self.clients, 'clientes', 'nombre', self.widget.get_widget('entFilterClients').get_text()+'%')
        print datos
        for dato in datos:
            self.clientesview.add(dato)           
                 

    def on_btnCleanFilterClients_clicked(self, widget, args=[]):
        print 'on_btnCleanFilterClients_clicked called with self.%s' % widget.get_name()
        self.widget.get_widget('entFilterClients').set_text('')


    def on_btnAddHistory_clicked(self, widget, args=[]):
        print 'on_btnAddHistory_clicked called with self.%s' % widget.get_name()
    

    def on_btnEditHistory_clicked(self, widget, args=[]):
        print 'on_btnEditHistory_clicked called with self.%s' % widget.get_name()
    

    def on_btnDelHistory_clicked(self, widget, args=[]):
        print 'on_btnDelHistory_clicked called with self.%s' % widget.get_name()
    

    def on_btnPrintHistory_clicked(self, widget, args=[]):
        print 'on_btnPrintHistory_clicked called with self.%s' % widget.get_name()
    

    def on_entFilterHistory_changed(self, widget, args=[]):
        print 'on_entFilterHistory_changed called with self.%s' % widget.get_name()
    

    def on_btnCleanFilterHistory_clicked(self, widget, args=[]):
        print 'on_btnCleanFilterHistory_clicked called with self.%s' % widget.get_name()
    

    def on_btnAddCredit_clicked(self, widget, args=[]):
        print 'on_btnAddCredit_clicked called with self.%s' % widget.get_name()
    

    def on_btnEditCredit_clicked(self, widget, args=[]):
        print 'on_btnEditCredit_clicked called with self.%s' % widget.get_name()
    

    def on_btnDelCredit_clicked(self, widget, args=[]):
        print 'on_btnDelCredit_clicked called with self.%s' % widget.get_name()
    

    def on_btnPrintCredit_clicked(self, widget, args=[]):
        print 'on_btnPrintCredit_clicked called with self.%s' % widget.get_name()
    

    def on_entFilterCredit_changed(self, widget, args=[]):
        print 'on_entFilterCredit_changed called with self.%s' % widget.get_name()
    

    def on_btnCleanFilterCredit_clicked(self, widget, args=[]):
        print 'on_btnCleanFilterCredit_clicked called with self.%s' % widget.get_name()
    

    def on_btnAddCashRegister_clicked(self, widget, args=[]):
        print 'on_btnAddCashRegister_clicked called with self.%s' % widget.get_name()
   

    def on_btnEditCashRegister_clicked(self, widget, args=[]):
        print 'on_btnEditCashRegister_clicked called with self.%s' % widget.get_name()
   

    def on_btnDelCashRegister_clicked(self, widget, args=[]):
        print 'on_btnDelCashRegister_clicked called with self.%s' % widget.get_name()
    

    def on_btnPrintCashRegister_clicked(self, widget, args=[]):
        print 'on_btnPrintCashRegister_clicked called with self.%s' % widget.get_name()
    

    def on_entFilterCashRegister_changed(self, widget, args=[]):
        print 'on_entFilterCashRegister_changed called with self.%s' % widget.get_name()
    

    def on_btnCleanFilterCashResgister_clicked(self, widget, args=[]):
        print 'on_btnCleanFilterCashResgister_clicked called with self.%s' % widget.get_name()
        
        
    def on_btnFamilias_clicked(self, widget, args=[]):
        winfamily = winFamilys()
        
        
    def on_btnEditBotonera_clicked(self, widget, args=[]):
        botonera = Botonera()
#if __name__=='__main__':
#    win = MainWindow()
#    gtk.main()