#!/usr/bin/env python
#coding=utf-8
from tree import TicketLineaView
import pygtk
pygtk.require('2.0')

import os
import gtk
import gtk.glade
from ddbb import DBAccess
from tree import (ClientesView, TicketView, TicketLineaView, ArticulosView, \
                  CreditoView, HistoricoView, TreeView)
from dialogclients import dlgClients
from dialogarticles import dlgArticles
from aboutdialog import dlgAbout
from winfamilys import winFamilys
#from buttonbox import buttonsBox
from botonera import Botonera
from dialognewticket import dlgNewTicket
from buttons import MakeButton

app = 'PyTPV'
version = '0.1'

class MainWindow:
    """
        Main class of PyTPV.
        Build dinamically notebook and all treeviews.
        All functions of Main Windows are here.
    """
    def __init__(self):
        
        # We create the notebook for store buttons called botonera
        self.notebook = gtk.Notebook()
        
        self.db = DBAccess()
        self.botonera = self.db.table_botonera()
        self.pages_botonera = self.db.table_pages_botonera()
        self.sort_pages_botonera = self.db.ordenar(self.pages_botonera, 'id_page')
        self.ticketlinea = self.db.table_ticketlinea()
        
        self.articulos = self.db.table_articles()
        data_botonera = []
        for item in self.botonera:
            data_botonera.append(item)
            
        data_articulos = []
        for item in self.articulos:
            data_articulos.append(item)
            
        a = 0
        c = 0
        r = 0
        aopt = gtk.FILL|gtk.SHRINK
        
        # Add the pages and buttons to notebook
        for page in self.sort_pages_botonera:
            label = gtk.Label(page[1])
            label.set_padding(15, 15)
            self.table = gtk.Table(6, 6)
            self.notebook.append_page(self.table, label)
            
            for x in range(36):
                
                button = MakeButton(data_botonera[a][5])
                print "button %s" % a
                #button.set_data("id", (a+1))
                button.set_data("id", data_botonera[a][0])
                button.connect("clicked", self.clicked, button.get_data("id"))
                button.set_focus_on_click(False)
                button.set_size_request(100, 100)
                if button.get_label() is None:
                    button.set_sensitive(False)
                self.notebook.get_nth_page(page[2]).attach(button, c, \
                                                     c+1, r, \
                                                     r+1, aopt, aopt, 0, 0)
                a += 1
                c += 1
                if c == 6:
                    c = 0
                    r += 1
                if r == 6:
                    r = 0
        
        
        self.widget = gtk.glade.XML('pytpv.glade')
        window = self.widget.get_widget('mainwindow')
        window.set_title(app + " " + version)
        window.set_icon_from_file('images'+ os.sep +'yinyang.png')
        
        self.clientesview = ClientesView(self)
        
        self.ticketview = TicketView(self)
        self.ticketview.set_size_request(500, 309)
        self.ticketview.connect('cursor-changed', self.on_TicketView_Cursor_Changed)
        
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
       
        hbox = self.widget.get_widget('hbox1')
        self.buttonbox = self.notebook
        #self.buttonbox = Buttons()       
        
        hbox.pack_start(self.buttonbox, False, False)
        
        window.show_all()
        
        self.db = DBAccess()
        self.clients = DBAccess().table_clients()
        self.dbclients = DBAccess().select(self.clients)
        #print self.dbclients
        if self.dbclients:
            for row in self.dbclients:
                self.clientesview.add(row)
            
        self.articles = DBAccess().table_articles()
        self.dbarticles = DBAccess().select(self.articles)
        self.family = self.db.table_family()
        
        if self.dbarticles:
            
            for row in self.dbarticles:
                print "%-5s %-5s %-5s" % (row[:-4])
                
                familyname = self.family.busqueda('familia', 'id=%s' % (row[1]))
                #print familyname[1]
                datos = row[0], familyname[1], row[2], ("%0.2f" %row[3]), \
                ("%0.2f" %row[4]), ("%0.2f" %row[5]), row[6]
                
                self.articlesview.add(datos)
        self.currentdate = self.db.date(self.clients)
        self.ticket = DBAccess().table_tickets()
        self.tickets = self.ticket.search('ticket', "fecha=\"%s\"" % self.currentdate)
        
        if self.tickets:
            for row in self.tickets:
                client = self.clients.busqueda('clientes', 'id=%s' % (row[1]))
                if row[6]:
                    credito = gtk.STOCK_ADD
                else:
                    credito = None
                
                if row[7]:
                    servicio = gtk.STOCK_DIALOG_WARNING
                else:
                    servicio = None
                
                if row[8]:
                    comanda = gtk.STOCK_APPLY
                else:
                    comanda = None
                    
                structured_row = [row[0], credito, servicio, comanda, client[1], \
                                  client[2], None, row[3]]
                print structured_row
                self.ticketview.add(structured_row)
        
                
        self.widget.signal_autoconnect(self)
        
        
    def clicked(self, button, data):
        try:
            x = self.ticketview.getSelectedItem(0)
            if x:
#                if data:
                a = self.botonera.busqueda('botonera', 'id=%s' % (data))
                articuloboton = self.botonera.inner(a[4])
                
                print articuloboton
                suma = float(2.4)*float(3.5)
                print ("%0.2f" %suma)
                ticket = self.ticket.busqueda('tickets', 'id=%s' % \
                                               (self.on_TicketView_Cursor_Changed \
                                                (self, data)))
                
                ticketlinea = self.ticketlinea.busqueda('ticket_linea', \
                                                      'ticket_FK_id=%s and articulo_FK_id=%s' % \
                                                      (ticket[0], data))
                
                
                if ticketlinea:
                    
                    cells = "cantidad, articulo_FK_id"
                    cantidad = ticketlinea[2] + 1
                    datos = cantidad, ticketlinea[3]
                    self.db.update(self.ticketlinea, 'ticket_linea', cells, datos, \
                                   "id=\"%s\"" % ticketlinea[0])
                    
#                    result = float(cantidad)*float(ticketlinea[4])
#                    print ("%0.2f" % result)
#                    self.ticketlineaview.update(1, 2, ("%0.2f" % cantidad))
#                    self.ticketlineaview.update(1, 4, ("%0.2f" % result))
                    importe = cantidad*ticketlinea[4]
                    print "%0.2f" % importe
                    datos = ticketlinea[0], cantidad, importe
                    print datos
                    self.ticketlineaview.model_foreach(datos)
                    
                else:    
                    self.db.insert(self.ticketlinea, None, ticket[0], \
                                   float(1), articuloboton[0], float(articuloboton[5]))
                    row = self.db.get_last_insert(self.ticketlinea)
                    row = row[0], row[1], ("%0.2f" % 1), articuloboton[2], ("%0.2f" % row[4])
                    
                    self.ticketlineaview.add(row)
                print (self.on_TicketView_Cursor_Changed(self, data))
                print ticket
        except:
            print 'You should select a row in ticketview'
    
    
    def on_mainwindow_destroy(self, widget, args=[]):
        print 'on_mainwindow_destroy called with self.%s' % widget.get_name()
        gtk.main_quit()
        print 'aplicacion destruida'
    
    
    def on_btnNewTicket_clicked(self, widget, args=[]):
        print 'on_btnNewTicket_clicked called with self.%s' % widget.get_name()
        #winnewticket = winNewTicket()
        newticket = dlgNewTicket().NewTicket(self, widget)
        if newticket != None:
            print 'va o no' % newticket
            
            path = self.ticketview.add(newticket)
                        
            self.ticketview.scroll_to_cell(path[1])
            self.ticketview.get_selection().select_path(path[1])
            ticket = self.ticket.busqueda('ticket', 'id=%s' % \
                                           (self.on_TicketView_Cursor_Changed \
                                            (self, args)))
            print ticket[1]
            
    
    def on_btnEditTicket_clicked(self, widget, args=[]):
        print 'on_btnEditTicket_clicked called with self.%s' % widget.get_name()
        
        searchticket = dlgNewTicket().tickets.busqueda('ticket', 'id=%s' % \
                                              (self.ticketview.getSelectedItem(0)))
        
        editticket = dlgNewTicket().EditTicket(searchticket)
        print editticket
        
        if editticket != None:
            a = 1
            b = 1
            for x in range(7):
                self.ticketview.update(iter, a, editticket[b])
                a += 1
                b += 1
            print editticket
            
            
    def on_btnDelTicket_clicked(self, widget, args=[]):
        print 'on_btnDelTicket_clicked called with self.%s' % widget.get_name()
        item = self.ticketview.getSelectedItem(0)
        DBAccess().remove(self.tickets, 'id=%s' % item)
        self.ticketview.remove()
        ticketlinea = self.ticketlinea.search('ticket_linea', 'ticket_FK_id=%s' % \
                                              (item))
                
        if ticketlinea:
            for row in ticketlinea:
                self.db.remove(self.ticketlinea, 'ticket_FK_id=%s' % (item))
        self.ticketlineaview.clear()
        
    def on_TicketView_Cursor_Changed(self, widget, args=[]):
        id_ticket = self.ticketview.getSelectedItem(0)
        ticketlinea = self.ticketlinea.search('ticket_linea', 'ticket_FK_id=%s' % \
                                              (id_ticket))
        self.ticketlineaview.clear()
        for row in ticketlinea:
            articulo = self.articles.busqueda('articulos', 'id=%s' % (row[3]))
            structured_row = row[0], row[1], ("%0.2f" % row[2]), \
                                articulo[2], ("%0.2f" % row[4])
            self.ticketlineaview.add(structured_row)
        
        print id_ticket
        return id_ticket
    
    def on_btnOrder_clicked(self, widget, args=[]):
        print 'on_btnOrder_clicked called with self.%s' % widget.get_name()
    

    def on_btnDeselect_clicked(self, widget, args=[]):
        print 'on_btnDeselect_clicked called with self.%s' % widget.get_name()
    

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
        self.ticketview.clear()
        
#        datos = self.clients.search("clientes", "fecha = \"%s\" and nombre like = \"%s\"" % \
#                               (self.currentdate, self.widget. \
#                                get_widget('entFilterTicket').get_text()+'%'))
        datos = self.db.filter(self.clients, 'clientes', 'nombre', self.widget.get_widget('entFilterTicket').get_text()+'%')
        for dato in datos:
            #linea = self.db.filter(self.tickets, 'ticket', 'cliente_FK_id', dato[0])
            linea = self.ticket.search("ticket", "fecha = \"%s\" and cliente_FK_id = %s" % \
                                        (self.currentdate, dato[0]))
            for row in linea:    
                print row
                if row[6]:
                    credito = gtk.STOCK_ADD
                else:
                    credito = None
                
                if row[7]:
                    servicio = gtk.STOCK_DIALOG_WARNING
                else:
                    servicio = None
                
                if row[8]:
                    comanda = gtk.STOCK_APPLY
                else:
                    comanda = None
                    
                structured_row1 = [row[0], credito, servicio, comanda, dato[1], \
                                dato[2], None, row[4]]
                print 'row is' % structured_row1
            
                self.ticketview.add(structured_row1)  

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
        DBAccess().remove(self.articles, 'id=%s' % item)
        self.articlesview.remove()
    

    def on_btnPrintArticles_clicked(self, widget, args=[]):
        print 'on_btnPrintArticles_clicked called with self.%s' % widget.get_name()
    

    def on_entFilterArticles_changed(self, widget, args=[]):
        print 'on_entFilterArticles_changed called with self.%s' % widget.get_name()
        self.articlesview.clear()
        
        datos = self.db.filter(self.articles, 'articulos', 'descripcion', \
                               self.widget.get_widget('entFilterArticles'). \
                               get_text()+'%')
        for dato in datos:
            searchfamily = self.family.busqueda('familia', 'id=%s' % (dato[1]))
            print datos
            estructured_row = [dato[0], searchfamily[1], dato[2], dato[3], \
                               dato[4], dato[5], dato[6]]
            self.articlesview.add(estructured_row)   

    def on_btnCleanFilterArticles_clicked(self, widget, args=[]):
        print 'on_btnCleanFilterArticles_clicked called with self.%s' % widget.get_name()
        a = self.widget.get_widget('entFilterArticles')
        a.delete_text(0, -1)

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
        DBAccess().remove(self.clients, 'id=%s' % item)
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

            
