#!/usr/bin/env python
import pygtk
pygtk.require('2.0')
import gtk
import pickle


rect = gtk.gdk.Rectangle(100,100)
print rect.x
file = open('rect', 'wb')
pickle.dump(rect, file, pickle.HIGHEST_PROTOCOL)
file.close()

file = open('rect', 'rb')
rect = pickle.load(file)
print rect.x
file.close()