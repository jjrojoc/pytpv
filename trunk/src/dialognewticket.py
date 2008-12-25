#!/usr/bin/env python
#coding=utf-8
import os
import gtk, gtk.glade
from ddbb import DBAccess
from wincalendar import dlgCalendar
from tree import ClientesView

class dlgNewTicket:
    def __init__(self):
        self.db = DBAccess()
        self.clients = self.db.table_clients()
        self.tickets = self.db.table_tickets()
        
        self.widget = gtk.glade.XML('pytpv.glade', 'dlgNewTicket')
        self.dialognewticket = self.widget.get_widget('dlgNewTicket')
        self.dialognewticket.set_icon_from_file('images'+ os.sep +'yinyang.png')
        self.combo = self.widget.get_widget('cmbOderTimeNewTicket')
        self.widget.signal_autoconnect(self)
        items = ['12:00', '12:15', '12:30', '12:45', '13:00', '13:15', \
                 '13:30', '13:45', '14:00', '14:15', '14:30', '14:45', \
                 '15:00', '15:15', '15:30']
        self.MakeCombo(items)
        
        self.idnewticket = self.widget.get_widget('entIdNewTicket')
        self.entidclientnewticket = self.widget.get_widget('entIdClientNewTicket')
        self.entnamenewticket = self.widget.get_widget('entNameNewTicket')
        self.entaddressnewticket = self.widget.get_widget('entAddressNewTicket')
        self.entphonenewticket = self.widget.get_widget('entPhoneNewTicket')
        self.entoderhournewticket = self.widget.get_widget('entOrderHourNewTicket')
        self.entdatenewticket = self.widget.get_widget('entDateNewTicket')
        self.entcallhournewticket = self.widget.get_widget('entCallHourNewTicket')
        self.checkcredit = self.widget.get_widget('checkCredit')
        self.checkdelivery = self.widget.get_widget('checkDelivery')
        self.checkordered = self.widget.get_widget('checkOrdered')
        self.checkorderwithdrawn = self.widget.get_widget('checkOrderWithdrawn')
        
        
#        self.entrys = ['entIdNewTicket',\
#                        'entIdClientNewTicket', \
#                        'entNameNewTicket',\
#                        'entAddressNewTicket', \
#                        'entPhoneNewTicket', \
#                        'entOrderHourNewTicket', \
#                        'entDateNewTicket', \
#                        'entCallHourNewTicket', \
#                        'checkCredit', \
#                        'checkDelivery', \
#                        'checkOrdered', \
#                        'checkOrderWithdrawn']
#        print self.entrys
        self.clientesview = ClientesView(self)
        self.scrollednewticket = self.widget.get_widget('scrolledNewTicket')
        self.scrollednewticket.add(self.clientesview)
        self.clientesview.set_size_request(400, 250)
        
        for client in self.clients:
            self.clientesview.add(client)
        self.clientesview.show()
        self.clientesview.connect('cursor-changed', self.update_entrys)
        
    
    def NewTicket(self, boton, datos=None):
        #TODO: fix write a function for don't repeat code
        self.dialognewticket.set_title('Nuevo Pedido')
        self.dialognewticket.add_buttons(gtk.STOCK_NEW, gtk.RESPONSE_OK , \
                           gtk.STOCK_OK, gtk.RESPONSE_ACCEPT, \
                           gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL)
        
        currenttime = self.db.time(self.clients)
        self.entcallhournewticket.set_text(str(currenttime))
        currentdate = self.db.date(self.clients)
        self.entdatenewticket.set_text(str(currentdate))
        
#        for entry in self.entrys:
#            self.widget.get_widget(entry).set_text('')
#            pass
        resultado = self.dialognewticket.run()
        self.dialognewticket.hide()
        
        if resultado == -3:
            datos = []
            datos.append(self.entidclientnewticket.get_text())
            datos.append(self.entnamenewticket.get_text())
            datos.append(self.entaddressnewticket.get_text())
            datos.append(self.entphonenewticket.get_text())
            datos.append(self.entoderhournewticket.get_text())
            datos.append(self.entdatenewticket.get_text())
            datos.append(self.entcallhournewticket.get_text())
            if self.checkcredit.get_active():
                datos.append(1)
            else:
                datos.append(0)
            if self.checkdelivery.get_active():
                datos.append(1)
            else:
                datos.append(0)
            if self.checkordered.get_active():
                datos.append(1)
            else:
                datos.append(0)
            if self.checkorderwithdrawn.get_active():
                datos.append(1)
            else:
                datos.append(0)
            datos.append(0)
            print datos
            
            self.db.insert(self.tickets, None, datos[0], None, datos[4], datos[5], \
                           currenttime, datos[7], datos[8], datos[9], \
                           datos[10], datos[11])
            row = self.db.get_last_insert(self.tickets)
            searclients = self.clients.busqueda('clientes', 'id=%s' % (datos[0]))
            if row[6]:
                credito = gtk.STOCK_ADD
            else:
                credito = None
            
            if row[7]:
                servicio = gtk.STOCK_DIALOG_WARNING
            else:
                servicio = None
            
            if row[8]:
                comanda = gtk.STOCK_APPLY
            else:
                comanda = None
                
            structured_row = [row[0], credito, servicio, comanda, searclients[1], \
                            searclients[2], None, datos[4]]
            print 'row is' % structured_row
            
            return structured_row
        if resultado == -5:
            datos = []
            datos.append(self.entnamenewticket.get_text())
            datos.append(self.entaddressnewticket.get_text())
            datos.append(self.entphonenewticket.get_text())
            
            currentdate = self.db.date(self.clients)
            
            self.db.insert(self.clients, None, datos[0], datos[1], datos[2], \
                            currentdate, currentdate)
            row = self.db.get_last_insert(self.clients)
            
            datos1 = []
            datos1.append(row[0])
            datos1.append(row[1])
            datos1.append(row[2])
            datos1.append(row[3])
            datos1.append(self.entoderhournewticket.get_text())
            datos1.append(self.entdatenewticket.get_text())
            datos1.append(self.entcallhournewticket.get_text())
            if self.checkcredit.get_active():
                datos1.append(1)
            else:
                datos1.append(0)
            if self.checkdelivery.get_active():
                datos1.append(1)
            else:
                datos1.append(0)
            if self.checkordered.get_active():
                datos1.append(1)
            else:
                datos1.append(0)
            if self.checkorderwithdrawn.get_active():
                datos1.append(1)
            else:
                datos1.append(0)
            datos1.append(0)
            print datos1
            
            self.db.insert(self.tickets, None, row[0], None, datos1[4], datos1[5], \
                           currenttime, datos1[7], datos1[8], datos1[9], \
                           datos1[10], datos1[11])
            row = self.db.get_last_insert(self.tickets)
            searclients = self.clients.busqueda('clientes', 'id=%s' % (datos1[0]))
            if row[6]:
                credito = gtk.STOCK_ADD
            else:
                credito = None
            
            if row[7]:
                servicio = gtk.STOCK_DIALOG_WARNING
            else:
                servicio = None
            
            if row[8]:
                comanda = gtk.STOCK_APPLY
            else:
                comanda = None
                
            structured_row1 = [row[0], credito, servicio, comanda, searclients[1], \
                            searclients[2], None, datos1[4]]
            print 'row is' % structured_row1
            
            return structured_row1
        
        
    def EditTicket(self, datos):
        
        self.dialognewticket.set_title('Editar Pedido')
        self.dialognewticket.add_buttons(gtk.STOCK_OK, gtk.RESPONSE_ACCEPT, \
                           gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL)
        
        client = self.clients.busqueda('clientes', 'id=%s' % int(datos[1]))
        self.idnewticket.set_text(str(datos[0]))
        self.entidclientnewticket.set_text(str(client[0]))
        self.entnamenewticket.set_text(client[1])
        self.entaddressnewticket.set_text(client[2])
        self.entphonenewticket.set_text(client[3])
        self.entoderhournewticket.set_text(str(datos[3]))
        self.entdatenewticket.set_text(str(datos[4]))
        self.entcallhournewticket.set_text(str(datos[5]))
        if datos[6] != 0:
            self.checkcredit.set_active(True)
        if datos[7] != 0:
            self.checkdelivery.set_active(True)
        if datos[8] != 0:
            self.checkordered.set_active(True)
        if datos[9] != 0:
            self.checkorderwithdrawn.set_active(True)
            
        resultado = self.dialognewticket.run()
        self.dialognewticket.hide()
        
        if resultado == -3:
            datos1 = []
            datos1.append(self.entidclientnewticket.get_text())
            datos1.append(0)
            datos1.append(self.entoderhournewticket.get_text())
            datos1.append(self.entdatenewticket.get_text())
            datos1.append(self.entcallhournewticket.get_text())
            if self.checkcredit.get_active():
                datos1.append(1)
            else:
                datos1.append(0)
            if self.checkdelivery.get_active():
                datos1.append(1)
            else:
                datos1.append(0)
            if self.checkordered.get_active():
                datos1.append(1)
            else:
                datos1.append(0)
            if self.checkorderwithdrawn.get_active():
                datos1.append(1)
            else:
                datos1.append(0)
            datos1.append(datos[8])
            print datos1
            
            cells = "cliente_FK_id, caja_FK_id, hora, fecha, hora_llamada, \
                    credito, servicioadomicilio, comandaenviada, servido, oculto"
            self.db.update(self.tickets, 'ticket', cells, datos1, "id=\"%s\"" % datos[0])
            
            client = self.clients.busqueda('clientes', 'id=%s' % datos1[0])
            
            if datos1[5]:
                credito = gtk.STOCK_ADD
            else:
                credito = None
            
            if datos1[6]:
                servicio = gtk.STOCK_DIALOG_WARNING
            else:
                servicio = None
            
            if datos1[7]:
                comanda = gtk.STOCK_APPLY
            else:
                comanda = None
                
            structured_row1 = [datos1[0], credito, servicio, comanda, client[1], \
                               client[2], None, datos1[2]]
            
            return structured_row1
    
    def on_tglNameNewTicket_toggled(self, widget, args=[]):
        print 'on_tglNameNewTicket_toggled called with self.%s' % widget.get_name()
        self.clientesview.clear()
        
        datos = self.db.filter(self.clients, 'clientes', 'nombre', \
                               self.entnamenewticket. \
                               get_text()+'%')
        print datos
        for dato in datos:
            self.clientesview.add(dato)  
    
    def on_tglAddressNewTicket_toggled(self, widget, args=[]):
        print 'on_tglAddressNewTicket_toggled called with self.%s' % widget.get_name()
        self.clientesview.clear()
        
        datos = self.db.filter(self.clients, 'clientes', 'direccion', \
                               self.entaddressnewticket. \
                               get_text()+'%')
        print datos
        for dato in datos:
            self.clientesview.add(dato)
    
    def on_tglPhoneNewTicket_toggled(self, widget, args=[]):
        print 'on_tglPhoneNewTicket_toggled called with self.%s' % widget.get_name()
        self.clientesview.clear()
        
        datos = self.db.filter(self.clients, 'clientes', 'telefono', \
                               self.entphonenewticket. \
                               get_text()+'%')
        print datos
        for dato in datos:
            self.clientesview.add(dato)
    
    def on_btnShowCalendar_clicked(self, widget):
        print 'on_btnShowCalendar_clicked called with self.%s' % widget.get_name()
        dlgcalendar = dlgCalendar(self).newDate(self)
        if dlgcalendar:
            self.entdatenewticket.set_text(dlgcalendar)
            
    def update_entrys(self, widget):
        print 'on_update_entrys called with self.%s' % widget.get_name()
        id = self.clientesview.getSelectedItem(0)
        nombre = self.clientesview.getSelectedItem(1)
        direccion = self.clientesview.getSelectedItem(2)
        telefono = self.clientesview.getSelectedItem(3)
        
        self.entidclientnewticket.set_text(str(id))
        self.entnamenewticket.set_text(nombre)
        self.entaddressnewticket.set_text(direccion)
        self.entphonenewticket.set_text(telefono)
        
    
    def MakeCombo(self, items):
        """Setup a ComboBox or ComboBoxEntry based on a list of strings."""           
        model = gtk.ListStore(str)
        for i in items:
            model.append([i])
        self.combo.set_model(model)
        if type(self.combo) == gtk.ComboBoxEntry:
            self.combo.set_text_column(0)
        elif type(self.combo) == gtk.ComboBox:
            cell = gtk.CellRendererText()
            self.combo.pack_start(cell, False)
            self.combo.add_attribute(cell, 'text', 0)
            cell1 = gtk.CellRendererText()
            self.combo.pack_start(cell1, True)
            self.combo.add_attribute(cell1, 'text', 1)
        