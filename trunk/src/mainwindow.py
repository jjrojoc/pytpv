#!/usr/bin/python
import gtk
import gtk.glade
from ddbb import DBAccess
from tree import ClientesView
from dialogclients import DialogClients

class Main:
    def __init__(self):
        self.widget = gtk.glade.XML('pytpv.glade')
        window = self.widget.get_widget('mainwindow')
        
        self.clientesview = ClientesView(self)
        self.scrolledwindow = self.widget.get_widget('scrolledwindow4')
        self.scrolledwindow.add(self.clientesview)
        self.scrolledwindow.show_all()
        
        self.clients = DBAccess().table_clients()
        self.db = DBAccess().select(self.clients)
        for row in self.db:
            
            self.clientesview.add(row)
        self.widget.signal_autoconnect(self)
        
    def on_entrysearchclient_changed(self, text):
        print 'hola pepe'
        
    def on_button_about_clicked(self, widget):
        about = aboutdialog(self)
        
    def on_button_del_filter_clicked(self, deltext):
        a = self.widget.get_widget('entry1')
        a.delete_text(0, -1)
         
    def on_mainwindow_destroy(self, widget, event=None):
        gtk.main_quit()
        print 'aplicacion destruida'
    
    def on_button_quit_clicked(self, widget):
        gtk.main_quit()
        print 'aplicacion destruida'
        
    def on_button_new_client_clicked(self, widget):
        clientes = DialogClients().NewClient(self, widget)
        self.clientesview.prepend(clientes)
        
    def on_button_del_client_clicked(self,widget):
        item = self.clientesview.getSelectedItem(0)
        DBAccess().remove(self.clients, item)
        self.clientesview.remove()
        
    def on_button_edit_client_clicked(self,widget):
        datos = []
        for item in range(4):
            it = self.clientesview.getSelectedItem(item)
            datos.append(it)
        editclients = DialogClients().EditClient(datos)

        a = 1
        b = 1
        for x in range(3):
            self.clientesview.update(iter, a, editclients[b])
            a += 1
            b += 1
        print editclients

if __name__=='__main__':
    a=Main()
    gtk.main()