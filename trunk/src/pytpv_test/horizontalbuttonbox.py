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

class HorizontalButtonBox(gtk.HButtonBox):
    def __init__(self):
        # This class represent horizontal box buttons
        gtk.HButtonBox.__init__(self)
        
        self.set_layout(gtk.BUTTONBOX_SPREAD)
        self.set_spacing(5)
        
        button = gtk.Button(stock=gtk.STOCK_NEW)
        button.set_size_request(150,60)
        self.add(button)

        button = gtk.Button(stock=gtk.STOCK_EDIT)
        self.add(button)

        button = gtk.Button(stock=gtk.STOCK_DELETE)
        self.add(button)
            
        button = gtk.Button(stock=gtk.STOCK_FIND)
        self.add(button)
        
        button = gtk.Button(stock=gtk.STOCK_PRINT)
        self.add(button)        