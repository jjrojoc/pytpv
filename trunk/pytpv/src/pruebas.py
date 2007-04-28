#!/bin/env python

import pygtk
pygtk.require('2.0')
import gtk

def on_edit_item(renderer, row, text, col):
  model[row][col] = unicode(text)

def get_first_selected_row():
  try:
    return treeview.get_selected_rows()[1][0][0]
  except:
    return 0

def on_key_press(widget, event):
  keyname = gtk.gdk.keyval_name(event.keyval)
  if keyname == 'Tab': # event.keyval = 65289
    row, col = widget.get_cursor()
    if row == None:
      row = get_first_selected_row()
    if col == None:
      col = 0
    else:
      col = col.get_data('id')
    if col == colnum - 1:
      nextcol = 0
    else:
      nextcol = col + 1
    print nextcol
    if isinstance(row, (list, tuple)):
      row = row[0]
    renderer = widget.get_column(col).get_data('renderer')

    #  this doesn't work...
    ##tree_iter = model.get_iter(row)
    ##renderer.emit('edited', row, model.get_value(tree_iter, col))
    
    #  this either
    ##renderer.stop_editing(False)
    
    widget.set_cursor(row, widget.get_column(nextcol), True)
    return True # cancel the event

win = gtk.Window(gtk.WINDOW_TOPLEVEL)
win.set_default_size(700, 450)
win.set_title('Test')
win.connect('delete_event', gtk.main_quit)

model     = gtk.ListStore(str, str, str, str, str, str, str, str)
treeview  = gtk.TreeView(model)
colnum    = 8
colwidths = [90, 70, 140, 40, 30, 100, 100, 100]
coltexts  = ['blah'] * 8

for col in range(colnum):
  renderer = gtk.CellRendererText()
  renderer.set_property('ellipsize', True)
  renderer.set_property('editable', True)
  renderer.set_property('xpad', 5)
  if col % 2 == 0:
    renderer.set_property('background', '#DEDEDE')
  else:
    renderer.set_property('background', '#EFEFEF')
  renderer.connect('edited', on_edit_item, col)
  treecol = treeview.insert_column_with_attributes(
              -1, coltexts[col], renderer, text=col
            )
  treecol.set_spacing(10)
  treecol.set_resizable(True)
  treecol.set_alignment(0.5)
  treecol.set_data('id', col)
  treecol.set_data('renderer', renderer)
  treecol.set_min_width(colwidths[col])

model.append(['Foo', 'Bar', 'Baz', 'Bat',
              'Foo', 'Bar', 'Baz', 'Bat'])

treeview.set_cursor(0)
treeview.connect('key_press_event', on_key_press)

win.add(treeview)
win.show_all()
gtk.main()