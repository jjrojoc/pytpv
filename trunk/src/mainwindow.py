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
        self.scrolledwindow.add_with_viewport(self.clientesview)
        self.scrolledwindow.show_all()
        
        self.db = DBAccess().selectclients()
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
        self.clientesview.add(clientes)
        
    def on_button_del_client_clicked(self,widget):
        item = self.clientesview.getSelectedItem(0)
        clientes = DBAccess().remove_clients(item)
        self.clientesview.remove()
        
    def on_button_edit_client_clicked(self,widget):
        item = self.clientesview.getSelectedItem(0)
        item1 = self.clientesview.getSelectedItem(1)
        item2 = self.clientesview.getSelectedItem(2)
        item3 = self.clientesview.getSelectedItem(3)
        ite = ""
        ite = item, item1, item2, item3
        print ite
        clientes = DialogClients().EditClient(ite)

if __name__=='__main__':
    a=Main()
    gtk.main()