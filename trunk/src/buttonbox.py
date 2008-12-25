#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
from ddbb import DBAccess

class buttonsBox:
    def __init__(self):
        # Notebook botonera for article's buttons
        self.notebook = gtk.Notebook()
        
        self.db = DBAccess()
        self.botonera = self.db.table_botonera()
        self.pages_botonera = self.db.table_pages_botonera()
        self.articulos = self.db.table_articles()
        self.tickets = self.db.table_tickets()
        data_botonera = []
        for item in self.botonera:
            data_botonera.append(item)
            
        data_articulos = []
        for item in self.articulos:
            data_articulos.append(item)
            
        a = 0
        c = 0
        r = 0
        aopt = gtk.FILL|gtk.SHRINK
        
        for page in self.pages_botonera:
            label = gtk.Label(page[1])
            label.set_padding(15, 15)
            self.table = gtk.Table(6, 6)
            self.notebook.append_page(self.table, label)
            
            for x in range(36):
                button = MakeButton(data_botonera[a][5])
                print "button %s" % a
                button.set_data("id", (a+1))
                button.connect("clicked", self.clicked, button.get_data("id"))
                button.set_focus_on_click(False)
                button.set_size_request(100, 100)
                if button.get_label() is None:
                    button.set_sensitive(False)
                self.notebook.get_nth_page((page[0])-1).attach(button, c, \
                                                     c+1, r, \
                                                     r+1, aopt, aopt, 0, 0)
                a += 1
                c += 1
                if c == 6:
                    c = 0
                    r += 1
                if r == 6:
                    r = 0
        
    
        def clicked(self, button, data):
            if data :
                a = self.botonera.busqueda('botonera', 'id=%s' % (data))
            
                articuloboton = self.botonera.inner(a[4])
                print articuloboton
                suma = float(2.4)*float(3.5)
                print ("%0.2f" %suma)
                ticket = self.tickets.busqueda('tickets', 'id=%s' % \
                                               (self.on_TicketView_Cursor_Changed \
                                                (self, data)))
                print ticket[1]
