#!/usr/bin/env python
#coding=utf-8

import gtk, gtk.glade


class dlgCalendar:
    def __init__(self, date):
#        self.widget = gtk.glade.XML('pytpv.glade', 'dlgCalendar')
#        self.dlgcalendar= self.widget.get_widget('dlgCalendar') 
#        self.calendar = self.widget.get_widget('calendar')
#        
#        self.date = date
#        
#        self.widget.signal_autoconnect(self)
        pass
    
    def newDate(self, date):
        widget = gtk.glade.XML('pytpv.glade', 'dlgCalendar')
        dlgcalendar= widget.get_widget('dlgCalendar')
        calendar = widget.get_widget('calendar')         
        
        result = dlgcalendar.run()
        dlgcalendar.hide()
        
        if result == 1:
            date = calendar.get_date()
            date = "%0.2d-%0.2d-%0.4d" %(date[2], date[1]+1, date[0])
        
        return date