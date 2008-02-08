#!/usr/bin/python
import pygtk

import gtk
import gtk.glade
from ddbb import DBAccess
from tree import (ClientesView, TicketView, TicketLineaView, ArticulosView, \
                  CreditoView, HistoricoView)
from dialogclients import DialogClients
from dialogarticles import DialogArticles

class Main:
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
        
        self.scrolledwindow1 = self.widget.get_widget('scrolledwindow1')
        self.scrolledwindow2 = self.widget.get_widget('scrolledwindow2')
        self.scrolledwindow3 = self.widget.get_widget('scrolledwindow3')
        self.scrolledwindow4 = self.widget.get_widget('scrolledwindow4')
        self.scrolledwindow5 = self.widget.get_widget('scrolledwindow5')
        self.scrolledwindow6 = self.widget.get_widget('scrolledwindow6')
        
        self.scrolledwindow1.add(self.ticketview)
        self.scrolledwindow2.add(self.ticketlineaview)
        self.scrolledwindow3.add(self.articlesview)
        self.scrolledwindow4.add(self.clientesview)
        self.scrolledwindow5.add(self.historicoview)
        self.scrolledwindow6.add(self.creditoview)
        linea = (1, 1, 1, 'POLLO ASADO', 9.00)
        self.ticketlineaview.add(linea)
        linea = (1, 1, 1, 1, 'JUAN JOSE ROJO', ' SAUCE, 7', '13:30', 45)
        self.ticketview.add(linea)
        window.show_all()
        
        self.clients = DBAccess().table_clients()
        self.db = DBAccess().select(self.clients)
        if self.db <> 0:
            for row in self.db:
                self.clientesview.add(row)
            
        self.articles = DBAccess().table_articles()
        self.db = DBAccess().select(self.articles)
        if self.db <> 0:
            for row in self.db:
                self.articlesview.add(row)
        self.widget.signal_autoconnect(self)
        
    def on_entrysearchclient_changed(self, text):
        print 'hola pepe'
        
    def on_button_about_clicked(self, widget):
        about = aboutdialog(self)
        
    def on_button_del_filter_clicked(self, deltext):
        a = self.widget.get_widget('entry1')
        a.delete_text(0, -1)
         
    def on_mainwindow_destroy(self, widget, event=None):
        gtk.main_quit()
        print 'aplicacion destruida'
    
    def on_button_quit_clicked(self, widget):
        gtk.main_quit()
        print 'aplicacion destruida'
        
    def on_button_new_client_clicked(self, widget):
        clientes = DialogClients().NewClient(self, widget)
        if clientes != None:
            self.clientesview.prepend(clientes)
        
    def on_button_del_client_clicked(self,widget):
        item = self.clientesview.getSelectedItem(0)
        DBAccess().remove(self.clients, item)
        self.clientesview.remove()
        
    def on_button_edit_client_clicked(self,widget):
        datos = []
        for item in range(4):
            it = self.clientesview.getSelectedItem(item)
            datos.append(it)
        editclients = DialogClients().EditClient(datos)

        a = 1
        b = 1
        for x in range(3):
            self.clientesview.update(iter, a, editclients[b])
            a += 1
            b += 1
        print editclients
    
    
    def on_button_NewArticle_clicked(self, widget):
        articulos = DialogArticles().NewArticle(self, widget)
        if articulos != None:
            self.articlesview.prepend(articulos)
    
    def on_button_EditArticle_clicked(self, widget):
        datos = []
        for item in range(7):
            it = self.articlesview.getSelectedItem(item)
            datos.append(it)
        editarticles = DialogArticles().EditArticle(datos)
        
        a = 1
        b = 1
        for x in range(6):
            self.articlesview.update(iter, a, editarticles[b])
            a += 1
            b += 1
        print editarticles
    
    def on_button_DelArticle_clicked(self, widget):
        item = self.articlesview.getSelectedItem(0)
        DBAccess().remove(self.articles, item)
        self.articlesview.remove()


if __name__=='__main__':
    a=Main()
    gtk.main()