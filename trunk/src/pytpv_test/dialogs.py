#!/usr/bin/env python
#coding=utf-8

# PyTPV, software point of sale for restaurant, bar and pizzeria.
# Copyright (C) 2007 Juan Jose Rojo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Can you contact with author by means of email: <jjrojoc@gmail.com> or the
# next postal address:
# Juan Jose Rojo. San Lazaro, 13. 30840 Alhama de Murcia. Murcia. Spain
# This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
# This is free software, and you are welcome to redistribute it
# under certain conditions; type `show c' for details.

import gtk

def delete(window, widget, event=None):
    dialog = gtk.Dialog("Salir", None, 0,
                    (gtk.STOCK_YES, gtk.RESPONSE_YES,
                    gtk.STOCK_NO, gtk.RESPONSE_NO))
    
    hbox = gtk.HBox(False, 8)
    hbox.set_border_width(8)
    dialog.vbox.pack_start(hbox, False, False, 0)

    stock = gtk.image_new_from_stock(
            gtk.STOCK_DIALOG_WARNING,
            gtk.ICON_SIZE_DIALOG)
    hbox.pack_start(stock, False, False, 0)
    
    label = gtk.Label()
    label.set_markup("<b>Desea cerrar PyTPV?</b>")
    
    hbox.pack_start(label)
    dialog.show_all()

    response = dialog.run()

    if response == gtk.RESPONSE_YES:
        gtk.main_quit()
        return False
    if response == gtk.RESPONSE_NO:
        dialog.hide()
        return True



#class DialogQuit(gtk.Dialog):
#    
#    def __init__(self, parent=None):
#        # Create the toplevel window
#        gtk.Dialog.__init__(self, "Salir", None, 0,
#                            (gtk.STOCK_YES, gtk.RESPONSE_YES,
#                            gtk.STOCK_NO, gtk.RESPONSE_NO))
#                
#        hbox = gtk.HBox(False, 8)
#        hbox.set_border_width(8)
#        self.vbox.pack_start(hbox, False, False, 0)
#
#        stock = gtk.image_new_from_stock(
#                gtk.STOCK_DIALOG_WARNING,
#                gtk.ICON_SIZE_DIALOG)
#        hbox.pack_start(stock, False, False, 0)
#        
#        label = gtk.Label()
#        label.set_markup("<b>Desea cerrar PyTPV?</b>")
#        
#        hbox.pack_start(label)
#        self.show_all()
#
#        response = self.run()
#        print response
#        if response == gtk.RESPONSE_YES:
#            print response
#            gtk.main_quit()
#        if response == gtk.RESPONSE_NO:
#            self.hide()