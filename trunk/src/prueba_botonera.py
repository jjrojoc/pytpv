#!/usr/bin/env python

# example treemodelsort.py

import pygtk
pygtk.require('2.0')
import gtk
import random

class TreeModelSortExample:

    # close the window and quit
    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        return False

    def add_row(self, b):
        rand = self.rand
        # add a row of random ints
        i0 = self.w[0].sm.get_model().append([rand.randint(0, 1000),
                                              rand.randint(0, 1000000),
                                              rand.randint(-10000, 10000)])
        # select the new row in each view
        for n in range(3):
            sel = self.w[n].tv.get_selection()
            i1 = self.w[n].sm.convert_child_iter_to_iter(None, i0)
            sel.select_iter(i1)

    def __init__(self):
        # create a liststore with three int columns
        self.liststore = gtk.ListStore(int, int, int)

        # create a random number generator
        self.rand = random.Random()

        # Create new windows
        self.w = [None] * 3
        
        for n in range(3):
            self.w[n] = gtk.Window(gtk.WINDOW_TOPLEVEL)
            win = self.w[n]
            win.set_title("TreeModelSort Example %i" % n)
            win.set_size_request(220, 200)
            win.connect("delete_event", self.delete_event)
            win.vbox = gtk.VBox()
            win.add(win.vbox)
            win.sw = gtk.ScrolledWindow()
            win.sm = gtk.TreeModelSort(self.liststore)
            # Set sort column
            win.sm.set_sort_column_id(n, gtk.SORT_ASCENDING)
            win.tv = gtk.TreeView(win.sm)
            win.vbox.pack_start(win.sw)
            win.b = gtk.Button('Add a Row')
            win.b.connect('clicked', self.add_row)
            win.vbox.pack_start(win.b, False)
            win.sw.add(win.tv)
            win.tv.column = [None]*3
            win.tv.column[0] = gtk.TreeViewColumn('0-1000')
            win.tv.column[1] = gtk.TreeViewColumn('0-1000000')
            win.tv.column[2] = gtk.TreeViewColumn('-10000-10000')
            win.tv.cell = [None]*3
            for i in range(3):
                win.tv.cell[i] = gtk.CellRendererText()
                win.tv.append_column(win.tv.column[i])
                win.tv.column[i].set_sort_column_id(i)
                win.tv.column[i].pack_start(win.tv.cell[i], True)
                win.tv.column[i].set_attributes(win.tv.cell[i], text=i)
            win.show_all()

def main():
    gtk.main()

if __name__ == "__main__":
    tmsexample = TreeModelSortExample()
    main()
    

import gtk
import gobject
import random


COLOMN_1 =0
COLOMN_2 =1
COLOMN_3 =2
COLOMN_4 =3
COLOMN_5 =4
COLOMN_6 =5
COLOMN_7 =6
MAX_COLOMN = 7



def GenData(num):
    '''
    Some function to generate lists of different sizes
    (up to 7 elements)
    '''
    print 'Going the generate %d colomns' % num
    names = ['first','second','third', 'forth', 'fifth', 'sixth', 'seventh']
    adata = ['a1','a2','a3','a4','a5','a6', 'a7' ]
    bdata = ['b1','b2','b3','b4','b5','b6', 'b7' ]
    cdata = ['c1','c2','c3','c4','c5','c6', 'c7' ]
    return names[:num], [adata[:num],bdata[:num],cdata[:num]]


#fname, data = GenData(rannum)
#nfields = len(fname)
title = "test dialog"


class window:
    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        #self.window.connect("delete_event", self.delete_event)
        self.window.connect("destroy",  lambda wid: gtk.main_quit())
        button = gtk.Button('dialog')
        button.connect('clicked', self.show_dialog)
        self.window.add(button)
        self.window.show_all()

    def show_dialog(self, widget) :
        print "===== dialog ====== "
        #dynamically generate data at press of dialog button
        #cause I got tired of closing app to get another random number of colomns
        global data, fname, nfields, heading
        rannum = int(MAX_COLOMN * random.Random().random())
        fname, data = GenData(rannum)
        nfields = len(fname)
        heading = "Heading for %d colomns" % nfields
        print 'nfields = %d' % nfields

        # create the dialog
        dialog = gtk.Dialog(title, self.window,
                gtk.DIALOG_DESTROY_WITH_PARENT,
                (gtk.STOCK_OK, gtk.RESPONSE_OK))
        dialog.connect("response", lambda x,y: dialog.destroy())
        vbox = dialog.vbox

        # put the heading in the dialog
        vbox.pack_start(gtk.Label(heading), False, False)

        # create the list store
        dialog._model = gtk.ListStore(str,str,str, str, str ,str, str)
        dialog._treeview = gtk.TreeView()
        dialog._column = [None] * nfields
        # add the columns to the list view
        for x in range(nfields) :
            # we need to know how to justify the columns
            xalign = 1.0
            # create and append the column
            cell = gtk.CellRendererText()
            dialog._column[x] = gtk.TreeViewColumn(fname[x].replace('_',' '), cell, text=x)
            cell.set_property('xalign', xalign)
            dialog._treeview.append_column(dialog._column[x])
        # create the scrolled window etc.
        dialog._scrolledwindow = gtk.ScrolledWindow()
        dialog._scrolledwindow.add(dialog._treeview)
        vbox.pack_start(dialog._scrolledwindow, True, True)
        dialog._treeview.set_model(dialog._model)

        # set the rows for the list
        self.set_rows_new(dialog)

        # show the dialog
        vbox.show_all()
        dialog.show()

    def set_rows_new(self, dialog):
        # limit the display to 20 rows
        limit = len(data)
        # show at max 20 rows
        print "title = \"%s\"" % (title)
        print "heading = \"%s\"" % (heading)
        row = [None] * nfields
        for x in data:
            extra = MAX_COLOMN - len(x)
            for i in range(extra):
                x.append(None)
            try:
                    dialog._model.append(x)
            except ValueError,msg:
                    print str(msg).strip()
            print

    def _set_rows(self, dialog) :
        # limit the display to 20 rows
        limit = len(data)
        # show at max 20 rows
        print "title = \"%s\"" % (title)
        print "heading = \"%s\"" % (heading)
        for x in range(limit) :
            iter = dialog._model.append()
            for y in range(nfields) :
                value = data[x][y]
                if value :
                    print "row %d field %d = %s" % (x, y, value)
                    try :
                        dialog._model.set(iter, y, str(value))
                    except ValueError, msg:
                        print "ERROR: %s" % (str(msg).strip())
                        return

    def set_rows(self, dialog) :
        # limit the display to 20 rows
        limit = len(data)
        # show at max 20 rows
        print "title = \"%s\"" % (title)
        print "heading = \"%s\"" % (heading)
        row = [None] * nfields
        for x in range(limit) :
            for y in range(nfields) :
                value = data[x][y]
                if value :
                    row[y] = str(value)
                else :
                    row[y] = None
            print "row = %d items = " % (len(row)),row
            try:
                dialog._model.append(row)
            except ValueError,msg:
                print str(msg).strip()
            print

    def main(self):
        gtk.main()
        
if __name__ == "__main__":
    window = window()
    window.main()

