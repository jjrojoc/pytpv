#!/usr/bin/env python
#coding=utf-8
import gtk, gtk.glade
from ddbb import DBAccess


class dlgFamilys:
    
    def __init__(self):
        
        self.db = DBAccess()
        self.family = self.db.table_family()        
        
        self.widget = gtk.glade.XML('pytpv.glade', 'dlgFamilys')
        self.dlgfamily = self.widget.get_widget('dlgFamilys')
        
        self.entrys = ['entIdFamily', \
                        'entNameFamily', \
                        'entDescriptionFamily']        
        
        self.widget.signal_autoconnect(self)
        
    
    def NewFamily(self, widget, datos=None):
        
        for entry in self.entrys:
            self.widget.get_widget(entry).set_text('')
        resultado = self.dlgfamily.run()
        self.dlgfamily.hide()
        
        if resultado == -3:
            datos = []
            for entry in self.entrys[1:]:
                datos.append(self.widget.get_widget(entry).get_text())
            print datos
            # lo meto en la base de datos

            
            
            self.db.insert(self.family, None, datos[0], datos[1])
            row = self.db.get_last_insert(self.family)
            print row
            
            return row
        
        
    def EditFamily(self, item):
        
        
        a = 0
        for entry in self.entrys:
            it = item[a]
            #print it
            if it <> None:
                if entry == 'entIdFamily':
                    self.widget.get_widget(entry).set_text(str(it))
                else:
                    self.widget.get_widget(entry).set_text(it)
            elif it == None:
                self.widget.get_widget(entry).set_text("")
            a += 1
             
        resultado = self.dlgfamily.run()
        self.dlgfamily.hide()
        
        if resultado == 1:
            datos = []
            for entry in self.entrys[1:]:
                datos.append(self.widget.get_widget(entry).get_text())
            #print datos
            cells = "nombre, descripcion"
            
            self.db.update(self.family, 'familias', cells, datos, "id=\"%s\"" \
                                   %item[0])
            datos = []
            for entry in self.entrys:
                text = self.widget.get_widget(entry).get_text()
                datos.append(text)
            return datos
