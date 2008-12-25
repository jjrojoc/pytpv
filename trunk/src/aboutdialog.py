#!/usr/bin/env python
#coding=utf-8

import gtk, gtk.glade

class dlgAbout:
    def __init__(self, aboutdialog):
        
        self.aboutwindow = gtk.glade.XML('pytpv.glade', 'aboutdialog')
        self.aboutdialog = self.aboutwindow.get_widget('aboutdialog')
        self.aboutdialog.run()
