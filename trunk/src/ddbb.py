#!/usr/bin/python

from sqlobject import db, table

password = 'x4jh2O'

class DBAccess:
    def __init__(self):
        self.d = db(user="root", passwd=password, db="pytpvdb")
        
    def selectclients(self):
        clientes = table(self.d, "clientes")
        datos = []
        for row in clientes:
            datos.append(row)
        return datos
    def insert_clients(self, *row):
        clientes = table(self.d, "clientes")
        clientes.insert(*row)
        
    def get_last_clients_insert(self):
        clientes = table(self.d, "clientes")
        return clientes[-1]
    
    def remove_clients(self, item):
        clientes = table(self.d, "clientes")
        clientes.__delitem__(item)
    
    def update_clients(self, *row):
        clientes = table(self.d, "clientes")
        clientes.update(name, cells, values, condition)