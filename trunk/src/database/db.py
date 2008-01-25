#!/usr/bin/python
import gtk, gtk.glade
from gazpacho.loader.loader import ObjectBuilder
from sqlobject import db, table
#from gui.quitdialog import QuitDialog
password = 'x4jh2O'

class pp:
    def __init__(self):
        self.d = db(user="root", passwd=password, db="pytpvdb")
        
        #table_name = d.tables()[0]
        #t = d.table(table_name)
        self.widget = gtk.glade.XML('/home/asadero/Documentos/pruebaglade.glade')
        #self.widget = ObjectBuilder('/home/asadero/Documentos/prueba.glade')
        entry = self.widget.get_widget('entry1')
        entry.connect('changed', self.on_entry1_changed)
        
        self.clientes = table(self.d, "clientes")
        window = self.widget.get_widget('mainwindow')
        
        
        self.listclientstore = gtk.ListStore(str, str, str, str, str)  # Id, Nombre, Direccion, Fecha_alta
        
        
        self.listclientsview = self.widget.get_widget('treeview4')
        self.listclientsview.set_model(self.listclientstore)
        self.listclientsview.get_selection().set_mode(gtk.SELECTION_SINGLE)
        
    
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
        
        
    
        for row in self.clientes:
            
            print row
            #ID, NOMBRE, DIRECCION, FECHA_ALTA, PRUEBA = row
            #row = [ID] + [NOMBRE] + [DIRECCION] +[FECHA_ALTA] + [PRUEBA]
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
    
    def on_mainwindow_destroy(self, widget, event=None):
        gtk.main_quit()
        print 'aplicacion destruida'
    
    def on_button14_clicked(self, widget):
        gtk.main_quit()
        print 'aplicacion destruida'
        
    def on_buttonnuevocliente_clicked(self, boton, datos=None):
        self.dialogclient = self.widget.get_widget('dialogclientes')
        for entry in ['entry4', 'entry13', 'entry12', 'entry11']:
            self.widget.get_widget(entry).set_text('')
        resultado = self.dialogclient.run()
        self.dialogclient.hide()
        
        if resultado == 1:
            datos = []
            for entry in ['entry13', 'entry12', 'entry11']:
                datos.append(self.widget.get_widget(entry).get_text())
            print datos
            
            # lo meto en la base de datos
            self.clientes.insert(None, datos[0], datos[1], datos[2])
            #datos = [id] + datos
            # lo meto en la interfaz
            row = self.clientes[-1]
            id = row[0]
            dato = [id] + datos +[id]
            print dato
            self.listclientstore.prepend(dato)
        
    def on_buttonborracliente_clicked(self, tabla):
        selected,iter = self.listclientsview.get_selection().get_selected()
        if iter:
            item = selected.get_value(iter,0)
            print item
            a = self.clientes.__delitem__(item)
            print a
            self.listclientstore.remove(iter)
        
        
    def on_buttoneditacliente_clicked(self,widget):
        self.dialogclient = self.widget.get_widget('dialogclientes')
        selected,iter = self.listclientsview.get_selection().get_selected()
        if iter:
            id = selected.get_value(iter, 0)
            nombre = selected.get_value(iter, 1)
            direccion = selected.get_value(iter, 2)
            fechaalta = selected.get_value(iter, 3)
            values = nombre, direccion, fechaalta
            
            self.widget.get_widget('entry4').set_text(id)
            self.widget.get_widget('entry13').set_text(nombre)
            self.widget.get_widget('entry12').set_text(direccion)
            self.widget.get_widget('entry11').set_text(fechaalta)
            cells = "nombre, direccion, fecha_alta"
            self.clientes.update('clientes', cells, values, id)
            
        resultado = self.dialogclient.run()
        self.dialogclient.hide()
        
        
        
        #d = self.widget.get_widget('entry11').set_text(self.listclientstore.get_value(iter, 3))
        
#        if resultado == 1:
#            datos = []
#            for entry in ['entry13', 'entry12', 'entry11']:
#                datos.append(self.widget.get_widget(entry).get_text())
#            print datos
#            
#            # lo meto en la base de datos
#            self.clientes.insert(None, datos[0], datos[1], datos[2])
#            #datos = [id] + datos
#            # lo meto en la interfaz
#            row = self.clientes[-1]
#            id = row[0]
#            dato = [id] + datos +[id]
#            print dato
#            self.listclientstore.prepend(dato)
#        
#        selected,iter = self.listclientsview.get_selection().get_selected()
#        id_record = selected.get_value(iter,0)
#        self.parent.editRecord(id_record)
            
        
if __name__=='__main__':
    a = pp()
    gtk.main()