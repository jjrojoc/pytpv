#!/usr/bin/env python
# PyTPV, software point of sale for restaurant, bar and pizzeria.
# Copyright (C) 2007 Juan Jose Rojo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Can you contact with author by means of email: <jjrojoc@gmail.com> or the
# next postal address:
# Juan Jose Rojo. San Lazaro, 13. 30840 Alhama de Murcia. Murcia. Spain
# This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
# This is free software, and you are welcome to redistribute it
# under certain conditions; type `show c' for details.


# db/accesodbeventos.py
import MySQLdb, time, string, _mysql, _mysql_exceptions
def executeSQLCommand(cursor, command):
    result = ''
    command = string.strip(command)
    if len(command):
        try:
             cursor.execute(command) # Ejecuta el comando
             if string.lower(command).startswith('select'):
                 # si es una select ...
                 lines = cursor.fetchall() # recuperar todos losresultados
                 for line in lines:
                     print line
                     
                     for column in line:
                         print column
                         if column == None:
                             result = result + 'null '
                         else:
                             result = result + str(column) + ' '
                     result = result + '\n'
        except _mysql_exceptions.ProgrammingError, e:
             print e
             sys.exit()

if __name__ == '__main__':
    db=MySQLdb.connect(host='localhost',user='deusto', passwd='deusto',db='deusto')
    cursor = db.cursor()
    executeSQLCommand(cursor, 'update eventos set fecha=' + str(time.time()*500))
    executeSQLCommand(cursor, 'select * from eventos')
#    print results
#    print results.split() # crear una lista y la visualiza
    cursor.close()


import ConfigParser
import os, sys



# write to screen
conf_dir = os.path.join( os.path.expanduser('~'), '.pytpv' )
settingsfile = os.path.join(conf_dir, 'settings')

settings = ConfigParser.ConfigParser()

if not os.path.isdir( conf_dir ):
    os.mkdir( conf_dir )
            
if not os.path.isfile( settingsfile ):
    f = open( settingsfile, 'w' )
    settings.read( settingsfile )
    if  settings.sections() == []:
        settings.add_section( 'Mysql' )
        settings.set( 'Mysql', 'host', '' )
        settings.set( 'Mysql', 'user', '')
        settings.set( 'Mysql', 'passwd', '')
        settings.set( 'Mysql', 'db', '')    
        settings.write(f)
        f.close()
        
settings.read( settingsfile )
settings.set('Mysql', 'host', 'localhost')
schoolnet = settings.get('Mysql', 'host').split(',')
#settings.read( settingsfile )
print schoolnet




#f = open(conf_dir +/config.ini', 'w')
#config.write(f)
#f.close()
