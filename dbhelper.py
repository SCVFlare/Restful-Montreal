import sqlite3


# generate random identifier(default=8)
class Database:
	def __init__(self):
		self.connection = None

	def get_connection(self):
		if self.connection is None:
			self.connection = sqlite3.connect('db/database.db')
		return self.connection

	def disconnect(self):
		if self.connection is not None:
			self.connection.close()
			self.connection = None
	
	def insert_contrevenant(self, adresse, categorie, date_infraction, date_jugement,description, etablissement, montant, proprietaire, ville):
		connection = self.get_connection()
		cursor = connection.cursor()
		cursor.execute("insert into contrevenant(adresse, categorie, date_infraction, date_jugement,"
							"description, etablissement, montant, proprietaire, ville) "
							"values(?, ?, ?, ?, ?, ?, ?, ?, ?)", 
							(adresse, categorie, date_infraction, date_jugement,description, etablissement, montant, proprietaire, ville))
		connection.commit()

	def get_data(self, attr, search):
		connection = self.get_connection()
		cursor = connection.cursor()
		cursor.execute("select * from contrevenant where %s like '%s'" % (attr, '%'+search+'%'))
		items = cursor.fetchall()
		return items
