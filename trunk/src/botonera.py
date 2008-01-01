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
from buttons import MakeButton

class botonera(gtk.Notebook):
    def __init__(self):
        # Notebook botonera for article's buttons
        gtk.Notebook.__init__(self)
        
        for i in 'PRINCIPAL', 'GUISOS', 'POSTRES', 'BEBIDAS', 'CARNES', 'ASADOS':
            self.tbl = gtk.Table(7, 6)
            self.tbl.set_homogeneous(True)
            
            label = gtk.Label(i)
            label.set_padding(15, 15)
            
            self.set_homogeneous_tabs(True)
            self.append_page(self.tbl, label)        
                    
        
        aopt = gtk.FILL|gtk.SHRINK
        c = 0
        r = 0
                         
                                
        for x in range (42):
            #stock = 'gtk-apply'
            #for stock in ("gtk-go-up"):
    #           button = gtk.Button(self.descripcion)
            button = MakeButton('POLLO ASADO', 'pixmaps/food065.gif')
            button.set_size_request(100, 100)
            self.get_nth_page(0).attach(button,c,c+1,r,r+1, aopt, aopt, 0, 0)
                        
            #button.connect("clicked", self.callback, self.linea)
                      
            #self.linea = [self.idarticulo] + [self.precio_venta]
            c += 1
            if c == 6:
                c = 0
                r += 1
                
        
    def callback(self, widget, data=None):
        print "Hello again - %s was pressed" % data
        self.idarticulo, self.familia, self.descripcion, self.stock, self.stock_minimo, self.precio_venta, self.imagen = data 
        data = [self.idarticulo]+[self.precio_venta]
##        self.cursor.execute('select * from articulos')
##                         
##        for linea in self.cursor.fetchall():
##            idarticulo, familia, descripcion, stock, stock_minimo, precio_venta, imagen = linea
##        linea = [self.idarticulo] + [self.precio_venta]
        self.cursor.execute('insert into ticket_linea (ticket_FK_id, cantidad, articulo_FK_id, precio_venta) values (1, 1, %s, %s)', data)        