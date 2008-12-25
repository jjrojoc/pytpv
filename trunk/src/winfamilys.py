#!/usr/bin/env python
#coding=utf-8
import os
import gtk, gtk.glade
from tree import FamiliaView
from ddbb import DBAccess
from dialogfamilys import dlgFamilys

class winFamilys:
    def __init__(self):
        self.db = DBAccess()
        self.family = self.db.table_family()
        
        self.widget = gtk.glade.XML('pytpv.glade', 'winFamily')
        self.winfamily = self.widget.get_widget('winFamily')
        self.winfamily.set_icon_from_file('images'+ os.sep +'yinyang.png')
        self.winfamily.set_title('Familias')
        
        vbox = self.widget.get_widget('vbox10')
        
        self.familiasview = FamiliaView(self)
        self.familiasview.set_size_request(400, 300)
        vbox.pack_end(self.familiasview, False, False)
        
        for row in self.family:
            self.familiasview.add(row)
        
        self.winfamily.show_all()
        self.widget.signal_autoconnect(self)
        
        
    def on_btnNewFamily_clicked(self, widget, args=[]):
        familys = dlgFamilys().NewFamily(self, widget)
        print familys
        if familys != None:
            self.familiasview.prepend(familys)
            self.familiasview.scroll_to_cell(0)
            
    
    def on_btnEditFamily_clicked(self, item):
        datos = []
                
        for item in range(3):
            it = self.familiasview.getSelectedItem(item)
            datos.append(it)
        
        editfamilys = dlgFamilys().EditFamily(datos)

        if editfamilys:
            a = 1
            b = 1
            for x in range(2):
                self.familiasview.update(iter, a, editfamilys[b])
                a += 1
                b += 1
            print editfamilys
            
    
    def on_btnDelFamily_clicked(self, item):
        item = self.familiasview.getSelectedItem(0)
        DBAccess().remove(self.family, 'id=%s' % item)
        self.familiasview.remove()        
        
        
    def on_btnPrintFamily_clicked(self, item):
       pass
