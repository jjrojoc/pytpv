#!/usr/bin/python

import gtk, gtk.glade
from ddbb import DBAccess

class DialogClients:
    def __init__(self):
        self.db = DBAccess()
        
        self.widget = gtk.glade.XML('pytpv.glade', 'dialogclients')
        self.dialogclient = self.widget.get_widget('dialogclients')
    
    def NewClient(self, boton, datos=None):
        self.widget = gtk.glade.XML('pytpv.glade', 'dialogclients')
        self.dialogclient = self.widget.get_widget('dialogclients')
        
        for entry in ['entryIdClient', 'entryNameClient', 'entryAddressClient', 'entryPhoneClient']:
            self.widget.get_widget(entry).set_text('')
        resultado = self.dialogclient.run()
        self.dialogclient.hide()
        
        if resultado == 1:
            datos = []
            for entry in ['entryNameClient', 'entryAddressClient', 'entryPhoneClient']:
                datos.append(self.widget.get_widget(entry).get_text())
            print datos
            
            # lo meto en la base de datos
            self.db.insert_clients(None, datos[0], datos[1], datos[2])
            #datos = [id] + datos
            # lo meto en la interfaz
            row = self.db.get_last_clients_insert()
            id = row[0]
            dato = [id] + datos +[id]
            print dato
            return dato
        
    def EditClient(self,*item):
        self.widget = gtk.glade.XML('pytpv.glade', 'dialogclients')
        self.dialogclient = self.widget.get_widget('dialogclients')
#        selected,iter = self.listclientsview.get_selection().get_selected()
#        
#        if iter:
#            id = selected.get_value(iter, 0)
#            nombre = selected.get_value(iter, 1)
#            direccion = selected.get_value(iter, 2)
#            fechaalta = selected.get_value(iter, 3)

        for ite in item:
            print ite   
            for entry in ['entryIdClient','entryNameClient', 'entryAddressClient', 'entryPhoneClient']:
                self.widget.get_widget(entry).set_text(ite)
#            self.widget.get_widget('entryIdClient').set_text(id)
#            self.widget.get_widget('entryNameClient').set_text(nombre)
#            self.widget.get_widget('entryAddressClient').set_text(direccion)
#            self.widget.get_widget('entryPhoneClient').set_text(fechaalta)
            
        resultado = self.dialogclient.run()
        self.dialogclient.hide()
        
        if resultado == 1:
            datos = []
            for entry in ['entryNameClient', 'entryAddressClient', 'entryPhoneClient']:
                datos.append(self.widget.get_widget(entry).get_text())
            print datos
            
            cells = "nombre, direccion, fecha_alta"
            
            self.db.update_clients('clientes', cells, datos, "id=\"%s\"" %id)
            
            a = self.widget.get_widget('entryNameClient').get_text(),\
            self.widget.get_widget('entryAddressClient').get_text(),\
            self.widget.get_widget('entryPhoneClient').get_text()
            print a
            
#            self.listclientstore.set_value(iter, 1, self.widget.get_widget('entryNameClient').get_text())
#            self.listclientstore.set_value(iter, 2, self.widget.get_widget('entryAddressClient').get_text())
#            self.listclientstore.set_value(iter, 3, self.widget.get_widget('entryPhoneClient').get_text())