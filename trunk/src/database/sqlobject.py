#!/usr/bin/python

# Modify the following to support other databases:
import MySQLdb
dbmod = MySQLdb
get_tables = "show tables;"  # how to get a list of tables
row_id = "_rowid"  # name of the row ID keyword

import types

class table:
	"""Emulates a list of DB rows, where each row is a tuple.
		May also be accessed via a string, to pull entire columns.
		Examples:
			t = table(db, "users")
			### select and organize data
			t.search("id<100")
			t.sort("lastname, firstname")
			### retrieve data
			rows = t[3:12]   # get 9 records, from the 4th to the 12th
			record = t[-5]   # get the 5th record from the endd
			names = t["firstname, lastname"]  # return a list of all firstname-lastname tuples
			### iterate over data
			for row in t:  print row
			### add data
			t.insert('', 'Bob', 'Barker', 'bbarker')
			### remove data
			del t[58]
	"""
	def __init__(self, db, name):
		self.db = db
		self.name = name
		self.dbc = None
		self.debug = 1
		self._styles = ["Cursor", "SSCursor"]
		self._new_cursor()
		self._sort = ""
		self._search = ""
		self._row_id = ", %s" % (row_id)
		# detect whether we are accessing more than one table
		if "," in self.name: self._row_id = ""

	def sort(self, method):
		self._sort = ""
		if method: self._sort = "order by %s" % (method)

	def search(self, method):
		self._search = ""
		if method: self._search = "where %s" % (method)

	def _new_cursor(self):
		"ensure we have a fresh, working cursor.  (improves support for SSCursors)"
		if self.dbc:
			self.dbc.close()
		for style in self._styles:
			if hasattr(dbmod.cursors, style):
				print style
				self.dbc = self.db.obj.cursor(getattr(dbmod.cursors, style))
				break

	def _query(self, q, data=None):
		if not self.dbc:
			self._new_cursor()
		if self.debug: print "Query: %s (%s)" % (q, data)
		self.dbc.execute(q, data)

	def __getitem__(self, item):
		q = "select *%s from %s %s %s" % (self._row_id, self.name, self._search, self._sort)
		if isinstance(item, types.SliceType):
			q = q + " limit %s, %s" % (item.start, item.stop - item.start)
			self._query(q)
			return self.dbc.fetchall()
		elif isinstance(item, types.StringType):
			q = "select %s%s from %s %s %s" % (item, self._row_id, self.name, self._search, self._sort)
			self._query(q)
			return self.dbc.fetchall()
		elif isinstance(item, types.IntType):
			if item < 0:  # add support for negative (from the end) indexing
				item = len(self) + item
				if item < 0:
					raise IndexError, "index too negative"
			q = q + " limit %s, 1" % (item)
			self._query(q)
			return self.dbc.fetchone()
		else:
			raise IndexError, "unsupported index type"

	def __setitem__(self, key, value):
		"Not yet implemented."
		if isinstance(key, types.IntType):
			pass
		else:
			raise IndexError, "index not a number"

	def __delitem__(self, item):
		# the method described in the article:
		q = "select %s from %s %s %s limit %s, 1" % ("_rowid", self.name, self._search, self._sort, item)
		self._query(q)
		rid = self.dbc.fetchone()[0]
		q = "delete from %s where %s=%s" % (self.name, "_rowid", rid)
		self._query(q)
		
		# a simpler method:
		#rid = self[item][-1]
		#q = "delete from %s where %s=%s" % (self.name, row_id, rid)
		#self._query(q)

	def insert(self, *row):
		fmt = ("%s," * len(row))[:-1]
		q = "insert into %s values (%s)" % (self.name, fmt)
		self._query(q, row)

	def __iter__(self):
		self._new_cursor()
		q = "select *%s from %s %s %s" % (self._row_id, self.name, self._search, self._sort)
		self._query(q)
		return self

	def next(self):
		r = self.dbc.fetchone()
		if not r:
			self._new_cursor()
			raise StopIteration
		return r

	def __len__(self):
		self._query("select count(*) from %s %s" % (self.name, self._search))
		r = int(self.dbc.fetchone()[0])
		return r
	

class db:
	"""
	A basic wrapper for databases.  Usage is as follows:
		d = db(user="user", passwd="password", db="database")
		table_name = d.tables()[0]
		t = d.table(table_name)
	The parameters for connect() and __init__() are keyword arguments, given
	directly to your database module.

	If you access the same table from several places in your code, there is no
	need to pass the table object around.  This class will keep track of them
	for you and provide the existing copy of a table, if one already exists.
	"""
	def __init__(self, **args):
		self._tables = {}
		if args:
			self.connect(**args)

	def tables(self):
		q = get_tables
		c = self.obj.cursor()
		a = c.execute(q)
		ts = []
		for row in c.fetchall():
			#print row
			ts.append(row[0])

		return ts

	def table(self, name):
		try:
			return self._tables[name]
		except:
			self._tables[name] = table(self, name)
			return self._tables[name]

	def connect(self, **args):
		self.obj = dbmod.connect(**args)

if __name__ == "__main__":
	print "this file should not be executed"
