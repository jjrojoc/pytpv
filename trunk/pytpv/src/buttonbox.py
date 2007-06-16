#!/usr/bin/env python
# -*- coding: utf-8 -*-
from encodings import utf_8

from codificacion import *


#print dir(pytpv)
import locale
import MySQLdb

class botonera:
    def __init__(self):
    
        self.db = MySQLdb.connect(db='pytpvdb',
                                      user='root')
        self.cursor = self.db.cursor()
        
        
    def pollo_asado (self, linea=None):
        self.cursor.execute('select id, descripcion, precio_venta from articulos where id = 1')
        for linea in self.cursor.fetchall():
            id, descripcion, precio = linea
    #            a=7.25+2.67
    #            b= locale.format("%.2f", a)
    #            print b
            linea = [id] + [precio]
            id_ticket = self.insertalinea(linea)
            print id_ticket
            linea = [id_ticket] + [1] + [descripcion] + [precio]
            print linea
            
#            self.ticketstore.append(linea)
                
            
    def insertalinea (self, linea):
        self.cursor.execute('insert into ticket_linea (ticket_FK_id, cantidad, articulo_FK_id, precio_venta) values (1, 1, %s, %s)', linea)
        self.cursor.execute('SELECT last_insert_id(), cantidad, (select descripcion from articulos where id = 1),\
                             (cantidad*precio_venta) from ticket_linea where articulo_FK_id = %s and precio_venta = %s', linea)
        
        return int(self.cursor.fetchone()[0])
    
    
    def medio_pollo(self, linea=None):
        
            self.cursor.execute('select id, descripcion, precio_venta from articulos where id = 2')
            for linea in self.cursor.fetchall():
                id, descripcion, precio = linea
    #            a=7.25+2.67
    #            b= locale.format("%.2f", a)
    #            print b
                linea = [id] + [precio]
                id_ticket = self.insertalinea1(linea)
    #            print id_ticket
                linea = [id_ticket] + [1] + [descripcion] + [precio]
                print linea
                self.ticketstore.append(linea)
                
                            
    def insertalinea1 (self, linea):
        self.cursor.execute('insert into ticket_linea (ticket_FK_id, cantidad, articulo_FK_id, precio_venta) values (1, 1, %s, %s)', linea)
        self.cursor.execute('select last_insert_id(), cantidad, (select descripcion from articulos where id = 2), precio_venta from ticket_linea where articulo_FK_id = %s and precio_venta = %s', linea)
        
        return int(self.cursor.fetchone()[0])
        
        
                   
                        
            
