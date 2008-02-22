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
from buttons import MakeButton, MakeTable
from ddbb import DBAccess

class buttonsBox(gtk.Notebook):
    def __init__(self):
        # Notebook botonera for article's buttons
        gtk.Notebook.__init__(self)
        
        self.db = DBAccess()
        self.botonera = self.db.table_botonera()
        self.pages_botonera = self.db.table_pages_botonera()
        #window = gtk.Window()
        #self.notebook = gtk.Notebook()
        #table = gtk.Table()
        
        #window.connect('destroy', gtk.main_quit)
        table = MakeTable(6, 6)
        #window.add(self.notebook)
        for name in self.pages_botonera:
#            table = gtk.Table(6, 6)
#            table.set_homogeneous(True)
#            table.check_resize()
            
            label = gtk.Label(name[1])
            label.set_padding(0, 15)
            
            self.set_homogeneous_tabs(True)
            self.append_page(table, label)
            
        aopt = gtk.FILL|gtk.SHRINK
        
        for row in range(6):
            for col in range(6):
                label2 = "r=%s,c=%d" % (row, col)
                button = MakeButton(label2)
                button.set_size_request(100, 100)
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
        
        
        
#        self.db = DBAccess()
#        self.familys = self.db.table_family()
#        self.dbfamilys = DBAccess().select(self.familys)        
#        self.articles = self.db.table_articles()
#        self.dbarticles = DBAccess().select(self.articles)
#        
#        for i in self.dbfamilys:
#            self.tbl = gtk.Table(6, 6)
#            self.tbl.set_homogeneous(True)
#            self.tbl.check_resize()
#            
#            label = gtk.Label(i[1])
#            label.set_padding(0, 15)
#            
#            self.set_homogeneous_tabs(True)
#            self.append_page(self.tbl, label)        
#                    
#        aopt = gtk.FILL|gtk.SHRINK
#        c = 0
#        r = 0
#        
#        for article in self.articles:
#            button = MakeButton(article[2], None)
#            button.set_size_request(120, 100)
#            self.get_nth_page(int(article[1])-2).attach(button,c,c+1,r,r+1, aopt, aopt, 0, 0)
#        #button.connect("clicked", self.callback, self.linea)
#                  
#         #self.linea = [self.idarticulo] + [self.precio_venta]
#            c += 1
#            if c == 6:
#                c = 0
#                r += 1
#            if r == 6:
#               pass 
#        #print self.get_nth_page(0).get_children()
#        
#    def callback(self, widget, data=None):
#        print "Hello again - %s was pressed" % data
#        self.idarticulo, self.familia, self.descripcion, self.stock, self.stock_minimo, self.precio_venta, self.imagen = data 
#        data = [self.idarticulo]+[self.precio_venta]
###        self.cursor.execute('select * from articulos')
###                         
###        for linea in self.cursor.fetchall():
###            idarticulo, familia, descripcion, stock, stock_minimo, precio_venta, imagen = linea
###        linea = [self.idarticulo] + [self.precio_venta]
#        self.cursor.execute('insert into ticket_linea (ticket_FK_id, cantidad, articulo_FK_id, precio_venta) values (1, 1, %s, %s)', data)        
