class Contrevenant(object):
	def __init__(self,id, adresse, categorie, date_infraction, date_jugement,
					description, etablissement, montant, proprietaire, ville):
		self.id=id
		self.adresse=adresse
		self.categorie=categorie
		self.date_infraction=date_infraction
		self.date_jugement=date_jugement
		self.description=description
		self.etablissement=etablissement
		self.montant=montant
		self.proprietaire=proprietaire
		self.ville=ville