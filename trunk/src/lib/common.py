#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
#from lib import i18n

# Application info
APPNAME = ("PyTPV")
APPVERSION = "0.1"
COPYRIGHTS = ("PyPTV - Copyright (c) 2007\nJuan José Rojo <jjrojoc@gmail.com>")
WEBSITE = "http://pytpv.sourceforge.net"
AUTHORS = [
    ('Developers:'),
    'Juan José Rojo <jjrojoc@gmail.com>',
    'Leandro Terrés <lord_lt@clubgtt.org>',
    '',
    ('Contributors:'),
    ''
]

ARTISTS = [
    
]

LICENSE = """
This application is distributed under the GPLv2 
Licensing scheme.  An online version of the 
license can be obtained from 
http://www.fsf.org/licensing/licenses/gpl.html.

Copyright (c) 2007, Juan José Rojo
All rights reserved.
"""

# Media path
if os.path.exists(os.path.abspath('../images/')):
    IMAGE_PATH = os.path.abspath('../images/')
else:
    IMAGE_PATH = '/usr/share/billreminder/images'

# Images
APP_ICON = os.path.join(IMAGE_PATH, 'billreminder.png')
APP_HEADER = os.path.join(IMAGE_PATH, 'header.png')

# Config info
CFG_NAME = 'billreminder.cfg'
CFG_PATH =  os.path.expanduser('~/.config/billreminder/')

# Database info
DB_NAME = 'billreminder.db'
DB_PATH =  os.path.expanduser('~/.config/billreminder/data/')

# DBus info
DBUS_INTERFACE = 'org.gnome.Billreminder.Daemon'
DBUS_PATH = '/org/gnome/Billreminder/Daemon'

# Notification info
NOTIFICATION_INTERFACE = 'org.freedesktop.Notifications'
NOTIFICATION_PATH = '/org/freedesktop/Notifications'

# Daemon files
DAEMON_LOCK_FILE = '/tmp/billreminderd.pid'
DAEMON_LOG_FILE = '/tmp/billreminderd.log'
