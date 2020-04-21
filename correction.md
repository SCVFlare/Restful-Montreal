# Correction
TOTAL - 110XP
## A1 - 10XP
Extraction des donn�es se fait dans le fichier 
*extraction_donees.py* a l'aide de fonction *extract_data()*
Le table dans la base de donn�e s'appelle 
*contrevenant* et est d�crit dans *contrevenant.sql*

## A2 - 10XP
C'est la page d'acceuil qui permet le recherche. Apr�s l'utilisateur est redig� vers */search* pour les resultats

## A3 - 5 XP
La fonction *extract_data()* est appel�
dans le d�but de fichier *app.py* avec la ligne:
*sched.add_job(extract_data, 'cron', hour=00, minute=1)*
## A4 - 10XP
La documentation sur */doc* d�crit le service. La route est */api/contrevenant*
Les arguments attendus sont "du" et "au".

## A5 - 10XP
La route est */dates*. Le script javascript est dans *static/dates.js*

## A6 - 10XP
La route est */noms*. Le script javascript est dans *static/noms.js*.
Le service REST qui etait cr�e est sur
*/api/infraction/{etablissement}*.
Elle est document�e sur */doc*

## C1 - 10XP
La route sur le service est 
*/api/etablissement*.
C'est OBLIGATOIRE d'ajouter dans le request un header:
*Content-Type:application/json*.

Elle est document�e sur */doc*

## C2 - 5XP
La route sur le service est 
*/api/etablissement*.
C'est OBLIGATOIRE d'ajouter dans le request un header:
*Content-Type:application/xml*.

Elle est document�e sur */doc*

## C3 - 5XP
La route sur le service est 
*/api/etablissement*.
C'est OBLIGATOIRE d'ajouter dans le request un header:
*Content-Type:text/xml*.

Elle est document�e sur */doc*

## D1 - 15XP
La page de formulaire est
*/plainte* est le script javascript est  dans *static/formulaire_plainte.js*.
La route de service POST est 
*/api/plainte*
Elle est document�e sur */doc*

## D2 - 5XP
La route de service DELETE est 
*/api/plainte/{id}*
Elle est document�e sur */doc*

## F1 - 15XP
Le lien de site Heroku est 

*https://restful-montreal.herokuapp.com/*