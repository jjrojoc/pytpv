#!/usr/bin/python
import gtk, gtk.glade
from gazpacho.loader.loader import ObjectBuilder
from sqlobject import db, table
password = 'x4jh2O'

class pp:
    def __init__(self):
        d = db(user="root", passwd=password, db="pytpvdb")
        #table_name = d.tables()[0]
        #t = d.table(table_name)
        #self.widget = gtk.glade.XML('/home/asadero/Documentos/prueba.glade')
        self.widget = ObjectBuilder('/home/asadero/Documentos/prueba.glade')
        entry = self.widget.get_widget('entry1')
        entry.connect('changed', self.on_entry1_changed)
        
        clientes = table(d, "clientes")
        window = self.widget.get_widget('window1')
        
        
        self.listclientstore = gtk.ListStore(str, str, str, str, str)  # Id, Nombre, Direccion, Fecha_alta
        
        
        self.listclientsview = self.widget.get_widget('treeview4')
        self.listclientsview.set_model(self.listclientstore)
        self.listclientsview.get_selection().set_mode(gtk.SELECTION_MULTIPLE)
        
    
        columns1 = ['ID', 'NOMBRE', 'DIRECCION', 'FECHA_ALTA', 'PRUEBA']
        for i in range(len(columns1)):
            renderer1 = gtk.CellRendererText()
            #renderer1.set_property('editable', True)
            #renderer1.connect('edited', self.editedCallback, i+1)
            column1 = gtk.TreeViewColumn(columns1[i], renderer1, text=(i))
            #column1.set_resizable(True)
            column1.set_spacing(10)
            column1.set_alignment(0.5)
            #font = pango.FontDescription('helvetica 8')
            #renderer.set_property('font-desc', font)
            self.listclientsview.append_column(column1)
#            column1.set_sizing(gtk.TREE_VIEW_COLUMN_FIXED)
#            column1.set_fixed_width(100)
            column1.set_sort_column_id(i)
            #renderer1.connect('edited', self.editedCallback, i+1)
        
        
    
        for row in clientes:
            
            print row
            ID, NOMBRE, DIRECCION, FECHA_ALTA, PRUEBA = row
            row = [ID] + [NOMBRE] + [DIRECCION] +[FECHA_ALTA] + [PRUEBA]
            #id, nombre, direccion, fecha = row
            #row = [id] + [nombre] + [direccion] + [fecha]
            self.listclientstore.append(row)
        
        
        self.widget.signal_autoconnect(self)
        #clientes.__delitem__(2)
    def on_entry1_changed(self, text):
        print 'hola pepe'
        
    def on_button12_clicked(self, deltext):
         a = self.widget.get_widget('entry1')
         a.delete_text(0, -1)
    
    def on_window1_delete(self, widget, event=None):
        dialog = self.widget.get_widget('dialog1')
        resultado = dialog.run()
        if resultado == 1:
            gtk.main_quit()
            return False
            
        if resultado == 2:
            dialog.hide()
            return True        
        
    def on_button14_clicked(self, widget):
        self.on_window1_delete(self)
    
        
if __name__=='__main__':
    a = pp()
    gtk.main()