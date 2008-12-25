#!/usr/bin/env python
#coding=utf-8
import os
import gtk, gtk.glade


class dlgCalendar:
    def __init__(self, date):
        self.widget = gtk.glade.XML('pytpv.glade', 'dlgCalendar')
        self.dlgcalendar= self.widget.get_widget('dlgCalendar') 
        self.dlgcalendar.set_icon_from_file('images'+ os.sep +'yinyang.png')
        self.dlgcalendar.set_title('Calendario')
        self.calendar = self.widget.get_widget('calendar')
        
#        self.date = date
#        
#        self.widget.signal_autoconnect(self)
    
    def newDate(self, date):
#        widget = gtk.glade.XML('pytpv.glade', 'dlgCalendar')
#        dlgcalendar= widget.get_widget('dlgCalendar')
#        calendar = widget.get_widget('calendar')         
        
        result = self.dlgcalendar.run()
        self.dlgcalendar.hide()
        
        if result == -3:
            date = self.calendar.get_date()
            date = "%0.4d-%0.2d-%0.2d" % (date[0], date[1]+1, date[2])
#            date = "%0.2d-%0.2d-%0.4d" %(date[2], date[1]+1, date[0])
        
            return date
        else:
            return None
