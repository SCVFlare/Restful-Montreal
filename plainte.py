class Plainte(object):
	def __init__(self,id, etablissement, adresse, ville, date_visite, prenom, nom, description):
		self.id=id
		self.etablissement=etablissement
		self.adresse=adresse
		self.ville=ville
		self.date_visite=date_visite
		self.prenom=prenom
		self.nom=nom
		self.description=description