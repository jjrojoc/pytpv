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

class ImageLabelButton (gtk.VBox):
    """
    This class is for make label and imagen inside button
    """
    def __init__(self, title, image):
        gtk.VBox.__init__(self, False, 4)
        self.img = gtk.Image()
        self.img.set_from_file(image)
        self.lbl = gtk.Label(title)
        
        self.vbox1 = gtk.VBox(False, 2)
        self.vbox1.pack_start(self.img, False, False, 0)
        self.vbox1.pack_start(self.lbl, False, False, 0)
        
        self.align = gtk.Alignment(0.5, 0.5, 0, 0)
        self.pack_start(self.align)
        self.pack_start(self.vbox1)

class MakeButton (gtk.Button):
    """
    classes for make buttons
    """
    
    def __init__ (self, title='', image=None):
        if title and image:
            gtk.Button.__init__(self)
            content = ImageLabelButton(title, image)
            self.add(content)
        elif title and not image:
            gtk.Button.__init__(self, title)
        else:
            gtk.Button.__init__(self)


class MakeTable(gtk.Table):
    def __init__(self, col=None, row=None):
        gtk.Table.__init__(self, col, row)
        self.set_homogeneous(True)
        self.check_resize()        