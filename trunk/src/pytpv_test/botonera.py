#!/usr/bin/env python
#coding=utf-8

import gtk

class botonera(gtk.Notebook):
    def __init__(self):
        # Notebook botonera for article's buttons
        gtk.Notebook.__init__(self)
        
        for i in 'PRINCIPAL', 'GUISOS', 'POSTRES', 'BEBIDAS', 'CARNES', 'ASADOS':
            self.tbl = gtk.Table(7, 6)
            self.tbl.set_homogeneous(True)
            
            
            label = gtk.Label(i)
            label.set_padding(15, 15)
            
            self.set_homogeneous_tabs(True)
            self.append_page(self.tbl, label)        
                    
        
        aopt = gtk.FILL|gtk.SHRINK
        c = 0
        r = 0
                         
                                
        for x in range (42):
            stock = 'gtk-apply'
             #for stock in ("gtk-go-up"):
    #            button = gtk.Button(self.descripcion)
            button = gtk.Button()
            box1 = self.xpm_label_box('food065.gif', 'POLLO ASADO Y ALGO MAS')
            button.add(box1)
            button.set_size_request(100, 100)
            self.get_nth_page(0).attach(button,c,c+1,r,r+1, aopt, aopt, 0, 0)
                        
            #button.connect("clicked", self.callback, self.linea)
                      
             #self.linea = [self.idarticulo] + [self.precio_venta]
            c += 1
            if c == 6:
                c = 0
                r += 1
                
    def xpm_label_box(parent, xpm_filename, label_text):
        # Create box for xpm and label
#        box1 = gtk.HBox(False, 0)#Boton con texto al lado de la imagen
        box1 = gtk.VBox(False, 0)#Boton con texto debajo de la magen
        box1.set_border_width(2)
    
        # Now on to the image stuff
        image = gtk.Image()
        image.set_from_file(xpm_filename)
    
        # Create a label for the button
        label = gtk.Label(label_text)
    
        # Pack the pixmap and label into the box
        box1.pack_start(image, False, False, 3)
        box1.pack_start(label, False, False, 3)
    
        image.show()
        label.show()
        return box1
        
    def callback(self, widget, data=None):
        print "Hello again - %s was pressed" % data
        self.idarticulo, self.familia, self.descripcion, self.stock, self.stock_minimo, self.precio_venta, self.imagen = data 
        data = [self.idarticulo]+[self.precio_venta]
##        self.cursor.execute('select * from articulos')
##                         
##        for linea in self.cursor.fetchall():
##            idarticulo, familia, descripcion, stock, stock_minimo, precio_venta, imagen = linea
##        linea = [self.idarticulo] + [self.precio_venta]
        self.cursor.execute('insert into ticket_linea (ticket_FK_id, cantidad, articulo_FK_id, precio_venta) values (1, 1, %s, %s)', data)        