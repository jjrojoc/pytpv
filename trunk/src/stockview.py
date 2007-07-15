#!/usr/bin/env python
#coding=utf-8

import pygtk
pygtk.require('2.0')
import gtk
import math

#this will generate the list of all the stock options
stock_options = [option for option in dir(gtk) if option.startswith("STOCK")]

class Stock_Buttons:

    def createButton(self,stock_option): 

        #ugly but this is a test.
        button = gtk.Button(stock=eval("gtk."+stock_option))
        button.connect("clicked", self.clicked,stock_option)
        button.show()
        return button

def clicked(self,widget,data=None):

    print "gtk.Button(stock=gtk.%s))" % data

def __init__(self):

    #setting some defaults.
    self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
    self.window.set_title("Sample stock buttons")
    self.window.set_border_width(10)#this will handle both gui events (click the X) and system events like
    #the kill command.
    self.window.connect("destroy", lambda wid: gtk.main_quit())
    self.window.connect("delete_event",lambda a1,a2:gtk.main_quit())

    #small trick to get the the size if the grid
    #93 boxes fit into a 10×10 grid
    #45 boxes fit into a 5×5 grid and so on.
    
    length = math.ceil(math.sqrt(len(stock_options)))

    #pasing floats to gtk is deprecated so to avoid that we make sure it’s an int
    length = int(length)
    print len(stock_options)
    #we set false so gtk will strink the buttons.
    table = gtk.Table(length,length,False)
    #set one widget on each 1×1 slot until we run out of widgets
    for index,option in enumerate(stock_options):
        i=index / length
        j=index % length
        #~ why this shows a weird layout?
        #~ i=index % length
        #~ j=index / length
        table.attach(self.createButton(option),i,i+1,j,j+1)

    self.window.add(table)
    table.show()
    self.window.show_all()

def main():

    gtk.main()
    return 0

if __name__ == "__main__":
    pp = Stock_Buttons()
    main()
