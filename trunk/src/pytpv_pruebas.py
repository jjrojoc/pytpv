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

import pygtk
pygtk.require('2.0')

import gtk
from notebookclass import notebook
import MySQLdb

class PyTPV(gtk.Window):
    def __init__(self):
        """
        Start Main Window of PyTPV application
        """
        gtk.Window.__init__(self,type=gtk.WINDOW_TOPLEVEL)
        
        self.connect("destroy", self.ss)
        self.maximize()
        
        self.set_border_width(3)
        self.set_title('PyTPV')
        icon = gtk.gdk.pixbuf_new_from_file("yinyang.png")
        self.set_icon(icon)
        self.connect("delete_event", self.delete)
        
        vbox = gtk.VBox()   
        self.add(vbox)
        self._quit = False
        self.notebook = notebook()
        
        vbox.pack_start(self.notebook)
        
        self.validated = False
        
        self.in_menu_main_validation(self)
        
    def ss(self, widget):
        self._quit = True 
    
    def do_expose_event(self,event):
        gtk.Window.do_expose_event(self, event)
        if self._quit:
            gtk.main_quit()
            
    def in_menu_main_validation(self, button):
        """
        Starting validation dialog
        """
        
        self.validation = gtk.Dialog("PyTPV ( Autentificar Usuario )", None, 0,
                            (gtk.STOCK_OK, gtk.RESPONSE_OK,
                            gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL))
        
        self.validation.set_default_response(gtk.RESPONSE_OK)
        hbox = gtk.HBox(False, 8)
        hbox.set_border_width(8)
        self.validation.vbox.pack_start(hbox, False, False, 0)
        image = gtk.Image()
        image.set_from_file ( '/home/asadero/Documents/pruebas_python/pytpv_pruebas/autentificacion.png' )
        hbox.pack_start(image, False, False, 0)
 
        table = gtk.Table(2, 2)
        table.set_row_spacings(4)
        table.set_col_spacings(4)
        hbox.pack_start(table, True, True, 0)
 
        label = gtk.Label("Usuario")
        label.set_use_underline(True)
        table.attach(label, 0, 1, 0, 1)
        self.local_entry1 = gtk.Entry()
        self.local_entry1.set_text(self.local_entry1.get_text())
        table.attach(self.local_entry1, 1, 2, 0, 1)
        label.set_mnemonic_widget(self.local_entry1)
 
        label = gtk.Label("Password")
        label.set_use_underline(True)
        table.attach(label, 0, 1, 1, 2)
        self.local_entry2 = gtk.Entry()
        self.local_entry2.set_text(self.local_entry2.get_text())
        table.attach(self.local_entry2, 1, 2, 1, 2)
        label.set_mnemonic_widget(self.local_entry2)
 
        self.validation.show_all()
 
        response = self.validation.run()
 
        if response == gtk.RESPONSE_OK:
            self.local_entry1.set_text(self.local_entry1.get_text())
            usuario = self.local_entry1.get_text()
            
            print self.local_entry1.get_text()
            self.local_entry2.set_text(self.local_entry2.get_text())
            password = self.local_entry2.get_text()
            print self.local_entry2.get_text()
            
            try:
                self.conn = MySQLdb.connect (host = 'localhost', \
                                             user = usuario,\
                                             passwd = password,\
                                             db = 'pytpvdb')
                print 'conexion realizada con exito'
                self.validated=True
                
            except Exception,msg:
                
                self.destroy()
                
            if self.validated:
                self.validation.destroy()
                #self.maintree.get_widget('main').show()
                  
            
            self.validation.destroy()
            return False
            
        if response == gtk.RESPONSE_CANCEL:
            self.destroy()
            self.validation.destroy()
            return True
    
    
    def delete(self, widget, event=None):
        dialog = gtk.Dialog("Salir", self, 0,
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
       
           
import gobject
gobject.type_register(PyTPV)

if __name__ == "__main__":
    pp = PyTPV()
    pp.show_all()
    gtk.main()
