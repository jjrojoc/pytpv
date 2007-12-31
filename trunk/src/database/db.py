import    pygtk
import    gtk
import    os

instruct = """
 To reproduce bug:

     leaving tree unexpanded and without a cursor, push bug button,
     selection bar will be placed on top line,  then expand top line,
     and try to select second line; selection bar will not work
"""


class    Main:

 def    __init__ (self):
     self. window = gtk. Window (gtk. WINDOW_TOPLEVEL)
     #self. window. maximize ()
     self. window. connect ("delete_event", self. delete_event)
     self. window. connect ("destroy", self. destroy)
     self. window. show ()

     self. box = gtk. VBox ()
     self. box. show ()
     self. window. add (self. box)

     self. text = gtk. TextView ()
     self. text. show ()
     bu = gtk. TextBuffer ()
     bu. set_text (instruct)
     self. text. set_buffer (bu)

     self. tv = gtk. TreeView ()
     self. tv. show ()
     self. ts = gtk. TreeStore (str)
     self. tv. set_model (self. ts)
     col = gtk. TreeViewColumn ('My column')
     self. tv. append_column (col)
     cell = gtk. CellRendererText ()
     col. pack_start (cell, False)
     col. add_attribute (cell, 'text', 0)
     r1 = self. ts. append (None, ('Test1', ))
     r2 = self. ts. append (r1, ('Test2', ))
     r3 = self. ts. append (r2, ('Test3', ))

     self. box. pack_start (self. tv)

     self. button = gtk. Button ('Bug')
     self. button. show ()
     self. button. connect ('clicked', self. bug)
     self. box. pack_end (self. text)
     self. box. pack_end (self. button, expand = False)



 def    bug (self, ev):
     self. tv. set_cursor ((0, 0, 0))


 def    main (self):
     gtk. main ()



 def delete_event (self, widget, event, data=None):
     #print    'Delete event'
     return False

 def destroy (self, widget, data = None):
     gtk. main_quit ()



if __name__ == '__main__':
 py = Main ()
 py. main ()