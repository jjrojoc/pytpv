#!/usr/bin/env python
#coding=utf-8

import os
import gtk, gtk.glade
from buttons import MakeButton, MakeTable
from ddbb import DBAccess
from tree import ArticulosView

class Botonera:
    
    def __init__(self):
        
        self.db = DBAccess()
        self.botonera = self.db.table_botonera()
        self.pages_botonera = self.db.table_pages_botonera()
        self.articulos = self.db.table_articles()
        self.widget = gtk.glade.XML('pytpv.glade', 'winBotonera')
        self.winbotonera = self.widget.get_widget('winBotonera')
        vbox = self.widget.get_widget('vbox13')
        self.winbotonera.show()
        self.widget.signal_autoconnect(self)
        self.notebook = gtk.Notebook()
        
        data_botonera = []
        for item in self.botonera:
            data_botonera.append(item)
            
        data_articulos = []
        for item in self.articulos:
            data_articulos.append(item)
        
        vbox.pack_start(self.notebook)
        a = 0
        c = 0
        r = 0
        aopt = gtk.FILL|gtk.SHRINK
        
        for page in self.pages_botonera:
            label = gtk.Label(page[1])
            label.set_padding(15, 15)
            self.table = gtk.Table(6, 6)
            self.notebook.append_page(self.table, label)
            
            for x in range(36):
                button = MakeButton(data_botonera[a][5])
                print "button %s" % a
                button.set_data("id", (a+1))
                button.connect("clicked", self.clicked, button.get_data("id"))
                button.set_size_request(100, 100)
#                if button.get_label() is None:
#                    button.set_sensitive(False)
                self.notebook.get_nth_page((page[0])-1).attach(button, c, \
                                                     c+1, r, \
                                                     r+1, aopt, aopt, 0, 0)
                a += 1
                c += 1
                if c == 6:
                    c = 0
                    r += 1
                if r == 6:
                    r = 0
        
        self.winbotonera.show_all()
        
        
    def clicked(self, button, data):
#        if data :
#            a = self.botonera.busqueda('botonera', 'id=%s' % (data))
#        
#            articuloboton = self.botonera.inner(a[4])
#            print articuloboton
        page = self.notebook.get_current_page()
      
        self.articles = self.db.table_articles()
        self.widget = gtk.glade.XML('pytpv.glade', 'dlgEditButton')
        self.dlgeditbutton = self.widget.get_widget('dlgEditButton')
        self.scrolledbotonera = self.widget.get_widget('scrolledbotonera')
        self.articlesview = ArticulosView(self)
        self.scrolledbotonera.add(self.articlesview)
        
        for article in self.articles:
            self.articlesview.add(article)
        
        self.articlesview.show_all()
        
        self.entrys = ['entIdArticleButton', 'entLabelButton']
        
        resultado = self.dlgeditbutton.run()
        self.dlgeditbutton.hide()
        if resultado == -3:
            #for entry in self.entrys:
            datos = []
            it = self.articlesview.getSelectedItem(0)
            datos.append(int(it))
            for entry in self.entrys[1:]:
                datos.append(self.widget.get_widget(entry).get_text())
            print datos
            cells = "article_FK_Id, label_button"
            
            self.db.update(self.botonera, 'botonera', cells, datos, "id=\"%s\"" \
                                   %int(button.get_data("id")))            
    
    
    def on_btnAddPageNotebook_clicked(self, widget, args=[]):
        self.widget = gtk.glade.XML('pytpv.glade', 'dlgAddPage')
        self.dlgaddpage = self.widget.get_widget('dlgAddPage')
        
        self.entrys = ['entNamePageNotebook']
        
        resultado = self.dlgaddpage.run()
        self.dlgaddpage.hide()
        if resultado == -3:
            table = MakeTable(6, 6)
            c = 0
            r = 0
            for entry in self.entrys:
                label = gtk.Label(self.widget.get_widget(entry).get_text())
                label.set_padding(0, 15)
                self.notebook.append_page(table, label)
            
            aopt = gtk.FILL|gtk.SHRINK
            
            for x in range(36):
                label2 = "r=%s,c=%d" % (r, c)
                button = MakeButton(label2)
                button.connect("clicked", self.clicked)
                button.set_data("row", (r))
                button.set_data("col", (c))
                button.set_size_request(100, 100)
               
                self.notebook.get_nth_page(0).attach(button, c, c+1, r, \
                                                    r+1, aopt, aopt, 0, 0)
                    
                c += 1
                if c == 6:
                    c = 0
                    r += 1
                if r == 6:
                    r = 0
                
                linea = self.db.get_last_insert(self.pages_botonera)
                
                self.db.insert(self.botonera, None, (linea[0]), r, c, None, None)
            
            pages = self.notebook.get_n_pages() - 1
            print pages
            self.db.insert(self.pages_botonera, None, \
                            self.widget.get_widget(entry).get_text())
            
            
    def on_btnEditPageNotebook_clicked(self, widget, args=[]):
        pass
    
    
    def on_btnDelPageNotebook_clicked(self, widget, args=[]):
        pass
    