import xml.etree.ElementTree as ET
from dbhelper import Database
import csv
import io

def etablissement_to_xml(etablissements):
	top=ET.Element('Etablissements')
	for e in etablissements:
		child=ET.Element('Etablissement')
		name=ET.SubElement(child,'name')
		name.text=e['name']
		nb=ET.SubElement(child,'nbinfractions')
		nb.text=str(e['nbinfractions'])
		for i in e['infractions']:
			infraction=ET.Element("Infraction")
			date_i=ET.SubElement(infraction,'date_infraction')
			date_i.text=i['date_infraction']
			montant=ET.SubElement(infraction,'nbinfractions')
			montant.text=str(i['montant'])
			description=ET.SubElement(infraction,'description')
			description.text=i['description']
			child.append(infraction)
		top.append(child)
	return ET.tostring(top,'utf-8')

def etablissement_to_csv(etablissements):
	si = io.StringIO()
	dict_writer = csv.DictWriter(si, fieldnames=['name','nbinfractions'],extrasaction='ignore')
	dict_writer.writeheader()
	dict_writer.writerows(etablissements)
	return si.getvalue()