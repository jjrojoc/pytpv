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

class Toolbar(gtk.Toolbar):
    def __init__(self):
        """
        Class for generate toolbar
        """
        gtk.Toolbar.__init__(self)

        self.set_tooltips(True)
        self.set_border_width(1)
        self.set_style(gtk.TOOLBAR_BOTH)
        

    def add_space(self):
        self.insert(gtk.SeparatorToolItem(), -1)

    def add_button(self, image, title, tip_text=None, callback=None):
        toolitem = gtk.ToolButton(image)
        toolitem.set_label(title)
        if callback:
            toolitem.connect('clicked', callback)
        self.insert(toolitem,-1)

    def add_stock(self, stock_id, tip_text=None, callback=None):
        toolitem = gtk.ToolButton(stock_id)
        toolitem.set_tooltip(gtk.Tooltips(), tip_text, tip_text)
        if callback:
            toolitem.connect('clicked', callback)
        self.insert(toolitem,-1)

    def add_toggle(self, stock_id, title, tip_text, callback):
        toolitem = gtk.ToggleToolButton(stock_id)
        toolitem.connect('toggled', callback)
        toolitem.set_tooltip(gtk.Tooltips(), tip_text, tip_text)
        self.insert(toolitem,-1)

    def add_widget(self, widget, tip_text, private_text):
        toolitem = gtk.ToolItem()
        toolitem.add(widget)
        toolitem.set_expand(False)
        toolitem.set_homogeneous(False)
        toolitem.set_tooltip(gtk.Tooltips(), tip_text, private_text)
        self.insert(toolitem,-1)
    