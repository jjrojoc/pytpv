#!/usr/bin/python

import gtk, gtk.glade
from ddbb import DBAccess

class DialogArticles:
    def __init__(self):
        self.db = DBAccess()
        self.articles = self.db.table_articles()
        
        self.widget = gtk.glade.XML('pytpv.glade', 'dialogArticles')
        self.dialogarticles = self.widget.get_widget('dialogArticles')
        self.combo = self.widget.get_widget('comboboxFamilyArticle')
        
        self.model = gtk.ListStore(str)
        cell = gtk.CellRendererText()
        self.combo.pack_start(cell, True)
        self.combo.add_attribute(cell, 'text', 0)
        self.model.clear()
        for entry in ['PEPE', 'JUAN']:
            self.model.append([entry])
        self.combo.set_model(self.model)
        
        self.combo.show()

        
    def NewArticle(self, boton, datos=None):
        self.widget = gtk.glade.XML('pytpv.glade', 'dialogArticles')
        self.dialogarticle = self.widget.get_widget('dialogArticles')
        
        
        for entry in ['entryIdArticle', \
                      'entryDescriptionArticle', 'entryStockArticle', \
                      'entryMinStockArticle', 'entrySalePriceArticle', \
                      'entryImageArticle']:
            
            self.widget.get_widget(entry).set_text('')
        resultado = self.dialogarticle.run()
        self.dialogarticle.hide()
        
        if resultado == 1:
            datos = []
            for entry in ['comboboxFamilyArticle', 'entryDescriptionArticle', \
                          'entryStockArticle', 'entryMinStockArticle', \
                          'entrySalePriceArticle', 'entryImageArticle']:
                if entry != 'comboboxFamilyArticle':
                    datos.append(self.widget.get_widget(entry).get_text())
                if entry == 'comboboxFamilyArticle':
                    datos.append(self.widget.get_widget(entry).get_active_text())
            print datos
            # lo meto en la base de datos
#            self.db.insert_clients(None, datos[0], datos[1], datos[2])
            self.db.insert(self.articles, None, 2, datos[1], datos[2], \
                           datos[3], datos[4], datos[5])
            row = self.db.get_last_insert(self.articles)
            print row
            id = row[0]
            dato = [id] + datos +[id]
            print dato
            return dato
        
    def EditArticle(self, item):
        self.widget = gtk.glade.XML('pytpv.glade', 'dialogArticles')
        self.dialogarticle = self.widget.get_widget('dialogArticles')
        
        a = 0
        for entry in ['entryIdArticle', \
                      'entryDescriptionArticle', 'entryStockArticle', \
                      'entryMinStockArticle', 'entrySalePriceArticle', \
                      'entryImageArticle']:
            it = item[a]
            print it
            if it <> None:
                self.widget.get_widget(entry).set_text(it)
            elif it == None:
                self.widget.get_widget(entry).set_text("")
            a += 1
             
        resultado = self.dialogarticle.run()
        self.dialogarticle.hide()
        
        if resultado == 1:
            datos = []
            for entry in ['comboboxFamilyArticle', 'entryDescriptionArticle', \
                          'entryStockArticle', 'entryMinStockArticle', \
                          'entrySalePriceArticle', 'entryImageArticle']:
                datos.append(self.widget.get_widget(entry).get_text())
            #print datos
            cells = "familia_FK_id, descripcion, stock, stock_minimo, \
                    precio venta, imagen"
            
            self.db.update(self.articles, 'articulos', cells, datos, \
                           "id=\"%s\"" % item[0])
            datos = []
            for entry in ['entryIdArticle', 'comboboxFamilyArticle', \
                      'entryDescriptionArticle', 'entryStockArticle', \
                      'entryMinStockArticle', 'entrySalePrice', \
                      'entryImageArticle']:
                text = self.widget.get_widget(entry).get_text()
                datos.append(text)
            return datos