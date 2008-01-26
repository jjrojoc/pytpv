import gtk

class aboutdialog:
    def __init__(self, aboutdialog):
        
        self.aboutwindow = gtk.glade.XML('pytpv.glade', 'aboutdialog1')
        self.aboutdialog = self.aboutwindow.get_widget('aboutdialog1')
        self.aboutdialog.run()