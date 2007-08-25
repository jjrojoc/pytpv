#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk
import lib.common as common

TRANSLATORS = "translator-credits"


class AboutDialog(gtk.AboutDialog):
    """
    About dialog class.
    """
    def __init__(self, parent=None):
        gtk.AboutDialog.__init__(self)

        # Set up the UI
        self._initialize_dialog_widgets()

    def _initialize_dialog_widgets(self):
        self.set_name(common.APPNAME)
        self.set_version(common.APPVERSION)
        self.set_copyright(common.COPYRIGHTS)
        self.set_logo(gtk.gdk.pixbuf_new_from_file(common.APP_HEADER))
        self.set_translator_credits(TRANSLATORS)
        self.set_license(common.LICENSE)
        self.set_website(common.WEBSITE)
        self.set_website_label(common.APPNAME)
        self.set_authors(common.AUTHORS)
        self.set_artists(common.ARTISTS)

        # Show all widgets
        self.show_all()
