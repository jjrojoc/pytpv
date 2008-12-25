#!/usr/bin/env python
#coding=utf-8

from sqlobject import db, table
import MySQLdb
password = '1307'

class DBAccess:
    def __init__(self):
        self.d = db(user="root", passwd=password, db="pytpvdb")
    
    def table_clients(self):
        clientes = table(self.d, "clientes")
        return clientes
    
    def table_articles(self):
        articles = table(self.d, "articulos")
        return articles
    
    def table_family(self):
        family = table(self.d, "familia")
        return family
    
    def table_pages_botonera(self):
        pages = table(self.d, "pages_botonera")
        return pages
    
    def table_botonera(self):
        botonera = table(self.d, "botonera")
        return botonera
    
    def table_tickets(self):
        tickets = table(self.d, "ticket")
        return tickets
    
    def table_ticketlinea(self):
        ticketlinea = table(self.d, "ticket_linea")
        return ticketlinea
    
    def select(self, table):
        datos = []
        for row in table:
            datos.append(row)
        return datos
    
    def count(self, table, name):
        count = table(self.d, name)
        return count 
    
    def sort(self, table, condition):
        sort = table.sort(condition)
        return sort
        
    def insert(self, table, *row):
        table.insert(*row)
        
    def get_last_insert(self, table):
        return table[-1]
    
    def remove(self, table, item):
        table.__delitem__(item)
    
    def update(self, table, name, cells, values, condition):
        update = table.update(name, cells, values, condition)
        
        
    def filter(self, table, name, values, condition):
        filter = table.filter(name, values, condition)
        return filter
    
    def time(self, table):
        time = table.time()
        return time
    
    def date(self, table):
        date = table.date()
        return date
    
    def busqueda(self, name, condition):
        search = table.busqueda(name, condition)
        return search
    
    def inner(self, id):
        query = table.inner(id)
        return query
    
    def max_value(self, table, cell, name):
        query = table.max_value(cell, name)
        return query
    
    def ordenar(self, table, condition):
        query = table.ordenar(table, condition)
        return query
    
    def search(self, name, condition):
        search = table.search(name, condition)
        return search
    
    def multiplicar(self, condition):
        result = table.multiplicar(condition)
        return result
