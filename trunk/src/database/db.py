#!/usr/bin/python

import gtk, gtk.glade

class win:
    def __init__(self):
        self.widgets = gtk.glade.XML('/home/asadero/Documentos/prueba.glade')
        self.w = self.widgets.get_widget('window1')

if __name__=="__main__":
    a = win()
    gtk.main()