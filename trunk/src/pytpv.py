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
#Testing
import locale

import gettext

import sys

import gtk
#import gtk.glade

import os

basic_rc = """
style "basic_style" {
    GtkPaned::handle_size = 4
    GtkRange::slider_width = 30
    GtkTreeView::horizontal-separator = 0
    GtkTreeView::vertical-separator = 0
    }
class "GtkWidget" style "basic_style"
"""
gtk.rc_parse_string(basic_rc)

from mainwindow import MainWindow


def main():
    #Run pytpv
    pytpv = MainWindow()

if __name__=="__main__":
    main()
    gtk.main()
