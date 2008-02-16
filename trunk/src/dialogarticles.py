#!/usr/bin/python

import gtk
import gtk.glade
from ddbb import DBAccess

class dlgArticles:
    
    def __init__(self):
        self.db = DBAccess()
        self.articles = self.db.table_articles()
        self.family = self.db.table_family()
        items = []
        for row in self.family:
            items.append(row)
        
        self.widget = gtk.glade.XML('pytpv.glade', 'dlgArticles')
        self.dialogarticles = self.widget.get_widget('dlgArticles')
        self.combo = self.widget.get_widget('cmbFamilyArticle')
        self.MakeCombo(items)
        
        self.entrys = ['entIdArticle', \
                        'cmbFamilyArticle', \
                        'entDescriptionArticle', \
                        'entStockArticle', \
                        'entMinStockArticle', \
                        'entSalePriceArticle', \
                        'entImageArticle']
        
        self.widget.signal_autoconnect(self)
        #TODO: Combo take the values from table and when select the values take 
        # first item like value by insert into database
        
    def MakeCombo(self, items):
        """Setup a ComboBox or ComboBoxEntry based on a list of strings."""           
        model = gtk.ListStore(str, str)
        for i, k, j in items:
            model.append([i] + [k])
        self.combo.set_model(model)
        if type(self.combo) == gtk.ComboBoxEntry:
            self.combo.set_text_column(0)
        elif type(self.combo) == gtk.ComboBox:
            cell = gtk.CellRendererText()
            self.combo.pack_start(cell, False)
            self.combo.add_attribute(cell, 'text', 0)
            cell1 = gtk.CellRendererText()
            self.combo.pack_start(cell1, True)
            self.combo.add_attribute(cell1, 'text', 1)
            
            
    def on_cmbFamilyArticle_changed(self, widget):
        model = self.combo.get_model()
        m_iter = self.combo.get_active_iter()
        if m_iter:
            print model.get_value(m_iter, 0)
            return model.get_value(m_iter, 0)
            
        else:
            return 0
    
    
    def NewArticle(self, boton, datos=None):

        for entry in self.entrys:
            print entry
            if not entry == 'cmbFamilyArticle':
                self.widget.get_widget(entry).set_text('')
        resultado = self.dialogarticles.run()
        self.dialogarticles.hide()
        
        if resultado == 1:
            datos = []
            for entry in self.entrys[1:]:
                if entry != 'cmbFamilyArticle':
                    datos.append(self.widget.get_widget(entry).get_text())
                if entry == 'cmbFamilyArticle':
                    combo = self.on_cmbFamilyArticle_changed(self)
                    print combo
                    datos.append(combo)
                    #datos.append(self.widget.get_widget(entry).get_active_text())
            print datos
            # lo meto en la base de datos

            self.db.insert(self.articles, None, datos[0], datos[1], datos[2], \
                           datos[3], datos[4], datos[5])
            row = self.db.get_last_insert(self.articles)
            familyname = self.family.busqueda('familia', 'id=%s' % (datos[0]))
            print familyname
            
            row = row[0],  familyname[1],  row[2],  row[3],  row[4],  row[5],  row[6]
            print row
            
            return row
        
    
    def EditArticle(self, item):
        searcharticles = self.articles.busqueda('articulos', 'id=%s' % (item[0]))
        searchfamily = self.family.busqueda('familia', 'id=%s' % (searcharticles[1]))
        a = 0
        for entry in self.entrys:
            if not entry == 'cmbFamilyArticle':
                it = item[a]
                print it
                if it <> None:
                    self.widget.get_widget(entry).set_text(str(it))
                elif it == None:
                    self.widget.get_widget(entry).set_text("")
            if entry == 'cmbFamilyArticle':
                self.widget.get_widget(entry).set_active(int(searchfamily[0])-1)
            a += 1
             
        resultado = self.dialogarticles.run()
        self.dialogarticles.hide()
        
        if resultado == 1:
            datos = []
            for entry in self.entrys[1:]:
                if entry == 'cmbFamilyArticle':
                    combo = self.on_cmbFamilyArticle_changed(self)
                    datos.append(combo)
                else:
                    datos.append(self.widget.get_widget(entry).get_text())
                
            #print datos
            cells = "familia_FK_id, descripcion, stock, stock_minimo, \
                    precio_venta, imagen"
            
            self.db.update(self.articles, 'articulos', cells, datos, \
                           "id=\"%s\"" % item[0])
            datos = []
            for entry in self.entrys:
                if not entry == 'cmbFamilyArticle':
                    datos.append(self.widget.get_widget(entry).get_text())
                else:
                    searchfamily = self.family.busqueda('familia', 'id=%s' % \
                    (self.on_cmbFamilyArticle_changed(self)))
                    datos.append(searchfamily[1])
            print datos
            return datos
        
        
    def on_filechooserbutton1_file_set(self, widget, args=[]):
            print 'on_filechooserbutton1_file_set called with self.%s' % widget.get_name()
            c1 = self.widget.get_widget("filechoose").get_filename()
            c2 = self.widget.get_widget("entImageArticle")
            if c1:
                c2.set_text(c1)