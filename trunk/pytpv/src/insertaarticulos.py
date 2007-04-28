#!/usr/bin/env python
# -*- coding: utf-8 -*-
from encodings import utf_8

from codificacion import *

from acredita import *

def on_buclefor_clicked(insertaarticulos):
    print 'on_buclefor_clicked'
    insertaarticulos = '''insert into ventas (cantidad, descripcion, precio) 
                        select {descripcion [descripcion], {precio[precio]| *}
                        from articulos [where id_articulos=1];'''
