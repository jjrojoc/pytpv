#!/usr/bin/env python
#coding=utf-8
import os
import gtk, gtk.glade
from ddbb import DBAccess

class dlgClients:
    def __init__(self):
        self.db = DBAccess()
        self.clients = self.db.table_clients()
        
        self.widget = gtk.glade.XML('pytpv.glade', 'dlgClients')
        self.dialogclient = self.widget.get_widget('dlgClients')
        self.dialogclient.set_icon_from_file('images'+ os.sep +'yinyang.png')
        
        self.entrys = ['entIdClient',\
                        'entNameClient', \
                        'entAddressClient',\
                        'entPhoneClient', \
                        'entDateClient', \
                        'entLastBuyClient']
        
    
    def NewClient(self, boton, datos=None):
        self.dialogclient.set_title('Nuevo Cliente')
        for entry in self.entrys:
            self.widget.get_widget(entry).set_text('')
        resultado = self.dialogclient.run()
        self.dialogclient.hide()
        
        if resultado == -3:
            datos = []
            for entry in self.entrys[1:]:
                datos.append(self.widget.get_widget(entry).get_text())
            print datos
            # lo meto en la base de datos

            currentdate = self.db.date(self.clients)
            print "fecha de hoy es %s" % currentdate
            self.db.insert(self.clients, None, datos[0], datos[1], datos[2],\
                            currentdate, None)
            row = self.db.get_last_insert(self.clients)
            print row
            
            return row
        
        
    def EditClient(self, item):
        self.dialogclient.set_title('Editar Cliente')
        a = 0
        for entry in self.entrys:
            it = item[a]
            #print it
            if it != None:
                if entry == 'entIdClient':
                    self.widget.get_widget(entry).set_text(str(it))
                else:
                    self.widget.get_widget(entry).set_text(it)
            elif it == None:
                self.widget.get_widget(entry).set_text("")
            a += 1
             
        resultado = self.dialogclient.run()
        self.dialogclient.hide()
        
        if resultado == -3:
            datos = []
            for entry in self.entrys[1:-1]:
                datos.append(self.widget.get_widget(entry).get_text())
            #print datos
            cells = "nombre, direccion, telefono, fecha_alta"
            
            self.db.update(self.clients, 'clientes', cells, datos, "id=\"%s\"" \
                                   %item[0])
            datos = []
            for entry in self.entrys:
                text = self.widget.get_widget(entry).get_text()
                datos.append(text)
            return datos
