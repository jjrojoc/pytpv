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
        self.sort_pages_botonera = self.db.ordenar(self.pages_botonera, 'id_page')
        self.articulos = self.db.table_articles()
        
        self.widget = gtk.glade.XML('pytpv.glade', 'winBotonera')
        self.winbotonera = self.widget.get_widget('winBotonera')
        self.winbotonera.set_title('Configurar Botonera')
        self.winbotonera.set_icon_from_file('images' + os.sep + 'yinyang.png')
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
        
        for page in self.sort_pages_botonera:
            label = gtk.Label(page[1])
            label.set_padding(15, 15)
            self.table = gtk.Table(6, 6)
            self.notebook.append_page(self.table, label)
            
            for x in range(36):
                button = MakeButton(data_botonera[a][5])
                print "button %s" % a
#                button.set_data("id", (a+1))
                button.set_data("id", data_botonera[a][0])
                button.connect("clicked", self.clicked, button.get_data("id"))
                button.set_size_request(100, 100)
#                if button.get_label() is None:
#                    button.set_sensitive(False)
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
        
        self.winbotonera.show_all()
        
        
    def clicked(self, button, data):

        page = self.notebook.get_current_page()
      
        self.articles = self.db.table_articles()
        self.widget = gtk.glade.XML('pytpv.glade', 'dlgEditButton')
        self.dlgeditbutton = self.widget.get_widget('dlgEditButton')
        self.dlgeditbutton.set_title('Editar Botón')
        self.dlgeditbutton.set_icon_from_file('images'+ os.sep +'yinyang.png')
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
        self.dlgaddpage.set_title('Nueva Pestaña')
        self.dlgaddpage.set_icon_from_file('images'+ os.sep +'yinyang.png')
        
        self.entrys = ['entNamePageNotebook']
        
        resultado = self.dlgaddpage.run()
        self.dlgaddpage.hide()
        if resultado == -3:
            table = MakeTable(6, 6)
            table.show_all()
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
                button.show()
                self.notebook.get_nth_page(0).attach(button, c, c+1, r, \
                                                    r+1, aopt, aopt, 0, 0)
                   
                c += 1
                if c == 6:
                    c = 0
                    r += 1
                if r == 6:
                    r = 0
                
                linea = self.pages_botonera.max_value('id_page', 'pages_botonera')
                linea += 1
                self.db.insert(self.botonera, None, linea, r, c, None, None)
            
            pages = self.notebook.get_n_pages() - 1
            print pages
            self.db.insert(self.pages_botonera, None, \
                           self.widget.get_widget(entry).get_text(), linea)
            self.winbotonera.show_all()
            
            
    def on_btnEditPageNoteBook_clicked(self, widget, args=[]):
        print 'on_btnEditPageNotebook_clicked called with self.%s' % widget.get_name()
        
        self.widget = gtk.glade.XML('pytpv.glade', 'dlgAddPage')
        self.dlgaddpage = self.widget.get_widget('dlgAddPage')
        self.dlgaddpage.set_title('Editar Pestaña')
        self.dlgaddpage.set_icon_from_file('images'+ os.sep +'yinyang.png')
        
        self.entrys = ['entNamePageNotebook']
        
        resultado = self.dlgaddpage.run()
        self.dlgaddpage.hide()
        if resultado == -3:
            
            child = self.notebook.get_children()
            index = self.notebook.get_current_page()
            label = gtk.Label(self.widget.get_widget(self.entrys[0]).get_text())
            self.notebook.set_tab_label(child[index], label)
            label.set_padding(15, 15)
            
            searchpagebotonera = self.pages_botonera.busqueda('pages_botonera', \
                                                              'id_page=%s' % index)
            cells = "label_page, id_page"
            datos = []
            datos.append(label.get_text())
            datos.append(searchpagebotonera[2])

            self.db.update(self.pages_botonera , 'pages_botonera', cells, datos, \
                           "id_page=\"%s\"" % index)
            
        
    def on_btnDelPageNotebook_clicked(self, widget, args=[]):
        print 'on_btnDelPageNotebook_clicked called with self.%s' % widget.get_name()
        
        index = self.notebook.get_current_page()
        filterbotonera = self.db.filter(self.botonera, 'botonera', 'botonera_FK_id', index)
        if index:
            for row in filterbotonera:
                self.db.remove(self.botonera, "botonera_FK_id=\"%s\"" % index)
            self.notebook.remove_page(index)

            self.db.remove(self.pages_botonera, "id_page=\"%s\"" % index)
            count = self.pages_botonera.count('pages_botonera')
            print count
            datos = []
            for row in self.pages_botonera:
                datos.append(row)
            a = 0
            for n in range(count):
                print 'COUNT IS %d:' % n
        
                cells = "label_page, id_page"
                values = [datos[a][1], n]
                self.db.update(self.pages_botonera, 'pages_botonera', cells, \
                               values, "id=\"%s\"" % datos[a][0])
                a += 1
            
            a = 0
            datos = []
            prueba = self.botonera.search('botonera', "botonera_FK_id>%s" % index)
            for row in prueba:
                datos.append(row)
                
                cells = 'botonera_FK_id, row'
                index = datos[a][1] - 1
                values = [index, datos[a][2]]
        
                self.db.update(self.botonera, 'botonera', cells, values, "id=\"%s\"" % datos[a][0])
                a +=1
