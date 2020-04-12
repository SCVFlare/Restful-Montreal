import urllib.request
import xml.etree.ElementTree as ET
import dbhelper
import locale
import datetime as dt

locale.setlocale(locale.LC_ALL, 'fr_FR')
db=dbhelper.Database()
url = 'http://donnees.ville.montreal.qc.ca/dataset/a5c1f0b9-261f-4247-99d8-f28da5000688/resource/92719d9b-8bf2-4dfd-b8e0-1021ffcaee2f/download/inspection-aliments-contrevenants.xml'
response = urllib.request.urlopen(url).read()
tree = ET.fromstring(response)
for c in tree:
	proprietaire=c.find('proprietaire').text
	#print(proprietaire)
	categorie=c.find('categorie').text
	#print(categorie)
	etablissement=c.find('etablissement').text
	#print(etablissement)
	adresse=c.find('adresse').text
	#print(adresse)
	ville=c.find('ville').text
	#print(ville)
	description=c.find('description').text
	#print(description)
	date_infraction=c.find('date_infraction').text
	date_infraction=dt.datetime.strptime(date_infraction,'%d %B %Y')
	#print(date_infraction)
	date_jugement=c.find('date_jugement').text
	date_jugement=dt.datetime.strptime(date_jugement,'%d %B %Y')
	#print(date_jugement)
	montant=c.find('montant')
	montant=montant.text.split(' ')
	montant=int(montant[0])
	#print(montant)
	db.insert_contrevenant(adresse,categorie,date_infraction,date_jugement,description,etablissement,montant,proprietaire,ville)
