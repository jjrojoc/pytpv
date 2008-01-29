#!/usr/bin/python

from sqlobject import db, table

password = ''

class DBAccess:
    def __init__(self):
        self.d = db(user="root", passwd=password, db="pytpvdb")
        
    def table_clients(self):
        clientes = table(self.d, "clientes")
        return clientes
    
    def select(self, table):
        datos = []
        for row in table:
            datos.append(row)
        return datos
    
    def insert(self, table, *row):
        table.insert(*row)
        
    def get_last_insert(self, table):
        return table[-1]
    
    def remove(self, table, item):
        table.__delitem__(item)
    
    def update(self, table, name, cells, values, condition):
        table.update(name, cells, values, condition)