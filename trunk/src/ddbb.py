#!/usr/bin/python

from sqlobject import db, table

password = 'x4jh2O'

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