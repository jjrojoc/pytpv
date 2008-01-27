import gtk

class aboutdialog:
    def __init__(self, aboutdialog):
        
        self.aboutwindow = gtk.glade.XML('pytpv.glade', 'aboutdialog')
        self.aboutdialog = self.aboutwindow.get_widget('aboutdialog')
        self.aboutdialog.run()