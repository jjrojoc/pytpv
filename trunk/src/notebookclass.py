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
from toolbar import Toolbar
from tree import TicketView, TicketLineaView, ClientesView, ArticulosView,\
                 CreditoView, HistoricoView
from horizontalbuttonbox import HorizontalButtonBox
from botonera import botonera
from buttons import MakeButton
import dialogs
class notebook(gtk.Notebook):
    def __init__(self):
        """
        Main Notebook of PyTPV application
        """
        gtk.Notebook.__init__(self)
        
        # Add all widgets for first notebook page
        for n in 'TPV', 'STOCK', 'CLIENTES', 'ARTICULOS', 'CREDITO', 'HISTORICO':
            vbox = gtk.VBox()
                      
            label = gtk.Label(n)
            label.set_padding(15, 15)
            
            self.set_homogeneous_tabs(True)
            self.append_page(vbox, label)
        
        # All widget for st up in notebook
        self.toolbar = Toolbar()
        
        self._populate_toolbar()   
        
        self.ticketview = TicketView(self)
        
        self.ticketlineaview = TicketLineaView(self)
        
        self.clientesview = ClientesView(self)
        
        self.articulosview = ArticulosView(self)
        
        self.creditoview = CreditoView(self)
        
        self.historicoview = HistoricoView(self)
        
        # Spacing where we pack
        self.vbox1 = gtk.VBox()
        self.vbox2 = gtk.VBox()    
        self.hbox = gtk.HBox()
        self.hbox1 = gtk.HBox()
        self.hbox2 = gtk.HBox()
        
        # Add the toolbar
        self.get_nth_page(0).pack_start(self.toolbar, expand=False, fill=True, padding=0)
        
        self.get_nth_page(0).add(self.hbox)
        
        # Add the first treeview (ticketview)
        self.scrolledwindow = gtk.ScrolledWindow()
        self.scrolledwindow.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_ALWAYS)
        self.hbox.pack_start(self.scrolledwindow, expand=True, fill=True, padding=0)
        self.scrolledwindow.add_with_viewport(self.ticketview)
        self.scrolledwindow.set_size_request(300, 300)
        self.ticketview.add([1, gtk.STOCK_ABOUT, gtk.STOCK_APPLY,\
            gtk.STOCK_CANCEL, 'JUAN JOSE ROJO', 'DESENGAÑO, 21', '13.50', '13.45'])
        
        self.hbox.add(self.vbox1)
        
        # Add the second treeview (ticketlineaview)
        self.scrolledwindow2 = gtk.ScrolledWindow()
        self.scrolledwindow2.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        self.vbox1.pack_start(self.scrolledwindow2, expand=True, fill=True, padding=0)
        self.scrolledwindow2.add_with_viewport(self.ticketlineaview)        
        self.ticketlineaview.add([1, 1, 2, 'POLLO ASADO', '18.00'])
        
        # Add the table for ticketlineaview buttons
        self.table = gtk.Table(2, 2)
        self.table.set_homogeneous(True)
        self.vbox1.pack_start(self.table, expand=False, fill=True, padding=2)
        
        aopt = gtk.FILL|gtk.SHRINK
        c = 0
        r = 0
                         
        for x in 'ENVIAR COMANDA', 'TOTALIZAR', 'BORRAR LINEA', 'ABRIR CAJON':
            
            button = MakeButton(x, 'pixmaps/food065.gif')
            if x == 'ENVIAR COMANDA':
                button.connect('clicked', self.enviarcomanda)
            elif x == 'TOTALIZAR':
                button.connect('clicked', self.totalizar)
            elif x == 'BORRAR LINEA':
                button.connect('clicked', self.borrarlinea_ticketlineaview)
            elif x == 'ABRIR CAJON':
                button.connect('clicked', self.abrircajon)            
            button.set_size_request(150, 92)
            self.table.attach(button,c,c+1,r,r+1, aopt, aopt, 0, 0)
                        
            #button.connect("clicked", self.callback, self.linea)
                      
            #self.linea = [self.idarticulo] + [self.precio_venta]
            c += 1
            if c == 2:
                c = 0
                r += 1        

        # Add the group filter for
        self.hbox.add(self.vbox2)
        self.vbox2.add(self.hbox1)
        
        label = gtk.Label('Filtrar por:')
        entry = gtk.Entry()
        entry.set_size_request(200, 40)
        self.button = MakeButton('Buscar')
        self.button.set_size_request(100, 60)
        self.hbox1.pack_start(label, expand=False, fill=False, padding=2)
        self.hbox1.pack_start(entry, expand=True, fill=True, padding=2)
        self.hbox1.pack_start(self.button, expand=False, fill=False, padding=2)
        
        # Add botonera where going all buttons for articles
        self.botonera = botonera()
        self.vbox2.pack_start(self.botonera, expand=True, fill=True, padding=2)
        
        
        # All all widget for second notebook page
        
        
        # Add all widgets for third notebook page
        self.hbuttonbox = HorizontalButtonBox()
        button = MakeButton('prueba')
        self.hbuttonbox.add(button)
        
        self.get_nth_page(2).pack_start(self.hbuttonbox, expand=False, fill=False, padding=0)
        
        self.scrolledwindow3 = gtk.ScrolledWindow()
        self.scrolledwindow3.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_ALWAYS)
        self.get_nth_page(2).pack_start(self.scrolledwindow3, expand=True, fill=True, padding=0)   
        self.scrolledwindow3.add_with_viewport(self.clientesview)
        
        linea = ([1, 'JUAN JOSE ROJO', 'DONDE SEA, 21', '15/05/1945'], [2, 'LEANDRO TERRES', 'HASTA EL INFINITO Y MAS ALLA, 249', '12/03/1999'])
        self.clientesview.addList(linea) 
        
        
        # Add all widgets for fourth notebook page
        self.hbuttonbox = HorizontalButtonBox()
        self.get_nth_page(3).pack_start(self.hbuttonbox, expand=False, fill=False, padding=0)
               
        self.scrolledwindow4 = gtk.ScrolledWindow()
        self.scrolledwindow4.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_ALWAYS)
        self.get_nth_page(3).pack_start(self.scrolledwindow4, expand=True, fill=True, padding=0)   
        self.scrolledwindow4.add_with_viewport(self.articulosview)               
        
        
        # Add all widgets for fifth notebook page
        self.hbuttonbox = HorizontalButtonBox()
        self.get_nth_page(4).pack_start(self.hbuttonbox, expand=False, fill=False, padding=0)
                        
        self.scrolledwindow5 = gtk.ScrolledWindow()
        self.scrolledwindow5.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_ALWAYS)
        self.get_nth_page(4).pack_start(self.scrolledwindow5, expand=True, fill=True, padding=0)   
        self.scrolledwindow5.add_with_viewport(self.creditoview)     
        
        
        # Add all widgets for sixth notebook page
        self.hbuttonbox = HorizontalButtonBox()
        self.get_nth_page(5).pack_start(self.hbuttonbox, expand=False, fill=False, padding=0)
                
        self.scrolledwindow6 = gtk.ScrolledWindow()
        self.scrolledwindow6.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_ALWAYS)
        self.get_nth_page(5).pack_start(self.scrolledwindow6, expand=True, fill=True, padding=0)   
        self.scrolledwindow6.add_with_viewport(self.historicoview)                
    
    
    def _populate_toolbar(self):
            
        self.toolbar.add_stock(gtk.STOCK_ABOUT, "About the application", self.borrarlinea_ticketlineaview)
        self.toolbar.add_space()
        self.toolbar.add_stock(gtk.STOCK_CLOSE, "Quit the application", self.delete)

    def on_mnuAbout_clicked(self, button):
        pass
    
    def delete(self, widget, event=None):
        dialogs.delete(self, event)
#    def delete(self, widget, event=None):
#        # Show the dialog for close application
#        from kiwi.ui.dialogs import yesno
#        from gtk import RESPONSE_YES
#        from gtk import RESPONSE_NO
#        
#        resp = yesno('Desea cerrar PyTPV?')
#        if resp == RESPONSE_YES:
#            gtk.main_quit()
#            return False
#        if resp == RESPONSE_NO:
#            return True
        
    def borrarlinea_ticketlineaview(self, iter):
        self.ticketlineaview.remove()
        
    def enviarcomanda(self, event):
        pass
    
    def totalizar(self, event):
        pass
    
    def abrircajon(self, event):
        pass