import sqlite3
from contrevenant import Contrevenant
from etablissement import Etablissement
from infraction import Infraction

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
	
	def insert_contrevenant(self, id, adresse, categorie, date_infraction, date_jugement,description, etablissement, montant,						proprietaire, ville):
		connection = self.get_connection()
		cursor = connection.cursor()
		cursor.execute("insert or replace into contrevenant(id, adresse, categorie, date_infraction, date_jugement,"
								"description, etablissement, montant, proprietaire, ville) "
								"values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
								(id, adresse, categorie, date_infraction, date_jugement,description, etablissement, montant, proprietaire, ville))
		connection.commit()
		
	def get_contrevenants_by_date(self, begin_date,end_date):
		connection = self.get_connection()
		cursor = connection.cursor()
		cursor.execute("select * from contrevenant where date_infraction between ? and ?", 
							(begin_date,end_date))
		results = cursor.fetchall()
		results=[Contrevenant(res[0],res[1],res[2],res[3],res[4],res[5],res[6],res[7],res[8],res[9]) for res in results]
		return results


	def get_data(self, attr, search):
		connection = self.get_connection()
		cursor = connection.cursor()
		cursor.execute("select * from contrevenant where %s like '%s'" % (attr, '%'+search+'%'))
		results = cursor.fetchall()
		results=[Contrevenant(res[0],res[1],res[2],res[3],res[4],res[5],res[6],res[7],res[8],res[9]) for res in results]
		return results
		
	def get_infractions(self,etablissement):
		connection = self.get_connection()
		cursor = connection.cursor()
		cursor.execute("select date_infraction,montant,description from contrevenant where etablissement=?",(etablissement,))
		results = cursor.fetchall()
		infractions=[Infraction(res[0],res[1],res[2]).__dict__ for res in results]
		return infractions
		
	def get_etablissement(self):
		connection = self.get_connection()
		cursor = connection.cursor()
		cursor.execute("select etablissement,count(*) from contrevenant group by etablissement")
		results = cursor.fetchall()
		etablissements=[Etablissement(res[0],res[1],self.get_infractions(res[0])) for res in results]
		etablissements.sort(key=lambda x:x.nbinfractions)
		return etablissements
		
