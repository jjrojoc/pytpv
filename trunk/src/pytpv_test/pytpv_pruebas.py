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
import pygtk
pygtk.require('2.0')
from notebookclass import notebook
import dialogs


class PyTPV(gtk.Window):
    def __init__(self):
        """
        Main window of PyTPV application
        """
        gtk.Window.__init__(self)
        self.maximize()
        #self.set_size_request(1024, 768)
        self.set_border_width(3)
        self.set_title('PyTPV')
        icon = gtk.gdk.pixbuf_new_from_file("yinyang.png")
        self.set_icon(icon)
        self.connect("delete_event", self.delete)
        
        vbox = gtk.VBox()   
        self.add(vbox)
        
        self.notebook = notebook()
        
        vbox.pack_start(self.notebook)
        

    def delete(window, widget, event=None):
        dialog = gtk.Dialog("Salir", window, 0,
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
    
    
#    def delete(self, widget, event=None):
#        # Show the dialog for close application
#        from kiwi.ui.dialogs import yesno
#        from gtk import RESPONSE_YES
#        from gtk import RESPONSE_NO
#        
#        resp = yesno('Desea cerrar PyTPV?')
#        if resp == RESPONSE_YES:
#            gtk.main_quit()
#            return False
#        if resp == RESPONSE_NO:
#            return True
       
           
def main():
    gtk.main()

if __name__ == "__main__":
    pp = PyTPV()
    pp.show_all()
    main()
