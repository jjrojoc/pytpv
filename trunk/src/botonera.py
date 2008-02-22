#!/usr/bin/env python
#coding=utf-8

import os
import gtk
from buttons import MakeButton, MakeTable
from ddbb import DBAccess
from tree import ArticulosView


class Botonera:
    
    def __init__(self):
        
        self.db = DBAccess()
        self.botonera = self.db.table_botonera()
        self.pages_botonera = self.db.table_pages_botonera()
        self.widget = gtk.glade.XML('pytpv.glade', 'winBotonera')
        self.winbotonera = self.widget.get_widget('winBotonera')
        vbox = self.widget.get_widget('vbox13')
        self.winbotonera.show()
        self.widget.signal_autoconnect(self)
        self.notebook = gtk.Notebook()
        self.button = MakeButton('', None)
        vbox.pack_start(self.notebook)
        
        datos = []
        for name in self.pages_botonera:
            datos.append(name[1])
            label = gtk.Label(name[1])
            label.set_padding(0, 15)
            table = gtk.Table()
            self.notebook.append_page(table, label)
        
        aopt = gtk.FILL|gtk.SHRINK
        
        for item in self.botonera:
            datos.append(item)
        
            button = MakeButton(item[5])
            button.connect("clicked", self.clicked)
            button.set_data("row", item[3])
            button.set_data("col",  item[2])
            button.set_data("id", item[0])
            button.set_size_request(100, 100)
            
            self.notebook.get_nth_page(0).attach(button, item[3], \
                                        item[3]+1, item[2], \
                                        item[2]+1, aopt, aopt, 0, 0)
                                        
        self.notebook.foreach(self.prueba, 'hola')
        self.notebook.show_all()
    
    def prueba(self, widget, text):
        print text
        
    def clicked(self, button):
        row = button.get_data("row")
        col = button.get_data("col")
        page = self.notebook.get_current_page()
        id = button.get_data("id")
        
        print 'page=%d' % page
        print "row=%d , col=%d" % (row, col)
        print "id=%s" % id
      
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
                                   %id)            
    
    
    def on_btnAddPageNotebook_clicked(self, widget, args=[]):
        self.widget = gtk.glade.XML('pytpv.glade', 'dlgAddPage')
        self.dlgaddpage = self.widget.get_widget('dlgAddPage')
        
        self.entrys = ['entNamePageNotebook']
        
        resultado = self.dlgaddpage.run()
        self.dlgaddpage.hide()
        if resultado == -3:
            table = MakeTable(6, 6)
            for entry in self.entrys:
                label = gtk.Label(self.widget.get_widget(entry).get_text())
                label.set_padding(0, 15)
                self.notebook.append_page(table, label)
            
            aopt = gtk.FILL|gtk.SHRINK
            
            for row in range(6):
                for col in range(6):
                    label2 = "r=%s,c=%d" % (row, col)
                    button = MakeButton(label2)
                    button.connect("clicked", self.clicked)
                    button.set_data("row", (row))
                    button.set_data("col", (col))
                    button.set_size_request(100, 100)
                   
                    self.notebook.get_nth_page(0).attach(button, col, col+1, row, \
                                                        row+1, aopt, aopt, 0, 0)
                    
                    linea = self.db.get_last_insert(self.pages_botonera)
                
                    self.db.insert(self.botonera, None, (linea[0]), row, col, None, None)
            
            pages = self.notebook.get_n_pages() - 1
            print pages
            self.db.insert(self.pages_botonera, None, \
                            self.widget.get_widget(entry).get_text())
            
            
    def on_btnEditPageNotebook_clicked(self, widget, args=[]):
        pass
    
    
    def on_btnDelPageNotebook_clicked(self, widget, args=[]):
        pass
    