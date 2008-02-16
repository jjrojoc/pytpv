#!/usr/bin/env python
#coding=utf-8

import gtk
from buttons import MakeButton


class Buttons(gtk.Notebook):
    def __init__(self):
        gtk.Notebook.__init__(self)
        
        #window = gtk.Window()
        #self.notebook = gtk.Notebook()
        table = gtk.Table()
        
        #window.connect('destroy', gtk.main_quit)
        
        #window.add(self.notebook)
        
        for name in ['CARNES', 'PESCADO', 'POSTRES']:
            
            label = gtk.Label(name)
            self.append_page(table, label)
            
        aopt = gtk.FILL|gtk.SHRINK
        
        for row in range(6):
            for col in range(6):
                label2 = "r=%s,c=%d" % (row, col)
                button = MakeButton(label2)
                button.connect("clicked", self.clicked)
                button.set_data("pos", (row, col))
               
                self.get_nth_page(0).attach(button, col, col+1, row, \
                                                    row+1, aopt, aopt, 0, 0)
                
        #window.show_all()

    def clicked(self, button):
        pos = button.get_data("pos")
        page = self.get_current_page()
        print 'page=%d' % page
        print "row=%d , col=%d" % pos