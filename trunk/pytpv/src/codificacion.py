#!/usr/bien/env python
# -*- coding: utf-8 -*-

def CUTF8(string="", encode = None):
    if string is None:
        string = ""
        if encode is None:
            try:
                return unicode(string).encode('utf8')
            except:
                return unicode(string, 'latin1').encode('utf8')
            else:
                try:
                    return unicode(string, 'latin1').encode('utf8')
                except:
                    return unicode(string).encode('utf8')

def CISO(string=""):
    try:
        str1 = unicode(string).encode("ISO-8859-1")
            
    except:
        string = CUTF8(string,"")
        str1 = unicode(string).encode("ISO-8859-1")
    return str1