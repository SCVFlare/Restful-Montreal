import sqlite3


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
	
    def insert_contrevenant(self, id, adresse, categorie, date_infraction, date_jugement,description, etablissement, montant, proprietaire, ville):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute("insert or replace into contrevenant(id, adresse, categorie, date_infraction, date_jugement,"
                            "description, etablissement, montant, proprietaire, ville) "
                            "values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                                (id, adresse, categorie, date_infraction, date_jugement,description, etablissement, montant, proprietaire, ville))
        connection.commit()