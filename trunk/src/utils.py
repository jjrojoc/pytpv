#!/usr/bin/env python
#coding=utf-8


def parseFloatRecord(string):
        if string != "":
            try:
                return float(string.replace(",",","))
            except:
                return float(string)
        else:
            return 0
        
def parseFloat(string):
        try:
            return float(string)
        except:
            return float(0)
