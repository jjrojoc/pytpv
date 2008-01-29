#!/usr/bin/python

import gtk, gtk.glade
from ddbb import DBAccess

class DialogClients:
    def __init__(self):
        self.db = DBAccess()
        self.clients = self.db.table_clients()
        
        self.widget = gtk.glade.XML('pytpv.glade', 'dialogclients')
        self.dialogclient = self.widget.get_widget('dialogclients')
    
    def NewClient(self, boton, datos=None):
        self.widget = gtk.glade.XML('pytpv.glade', 'dialogclients')
        self.dialogclient = self.widget.get_widget('dialogclients')
        
        for entry in ['entryIdClient', 'entryNameClient', 'entryAddressClient',\
                      'entryPhoneClient']:
            self.widget.get_widget(entry).set_text('')
        resultado = self.dialogclient.run()
        self.dialogclient.hide()
        
        if resultado == 1:
            datos = []
            for entry in ['entryNameClient', 'entryAddressClient', \
                          'entryPhoneClient']:
                datos.append(self.widget.get_widget(entry).get_text())
            print datos
            # lo meto en la base de datos
#            self.db.insert_clients(None, datos[0], datos[1], datos[2])
            self.db.insert(DBAccess().table_clients(), None, datos[0], datos[1], datos[2])
            row = self.db.get_last_insert(self.clients)
            print row
            id = row[0]
            dato = [id] + datos +[id]
            print dato
            return dato
        
    def EditClient(self, item):
        self.widget = gtk.glade.XML('pytpv.glade', 'dialogclients')
        self.dialogclient = self.widget.get_widget('dialogclients')
        
        a = 0
        for entry in ['entryIdClient','entryNameClient', 'entryAddressClient', \
                      'entryPhoneClient']:
            it = item[a]
            #print it
            if it <> None:
                self.widget.get_widget(entry).set_text(it)
            elif it == None:
                self.widget.get_widget(entry).set_text("")
            a += 1
             
        resultado = self.dialogclient.run()
        self.dialogclient.hide()
        
        if resultado == 1:
            datos = []
            for entry in ['entryNameClient', 'entryAddressClient', \
                          'entryPhoneClient']:
                datos.append(self.widget.get_widget(entry).get_text())
            #print datos
            cells = "nombre, direccion, fecha_alta"
            
            self.db.update(self.clients, 'clientes', cells, datos, "id=\"%s\"" \
                                   %item[0])
            datos = []
            for entry in ['entryIdClient', 'entryNameClient', \
                          'entryAddressClient', 'entryPhoneClient']:
                text = self.widget.get_widget(entry).get_text()
                datos.append(text)
            return datos