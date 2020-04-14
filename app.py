from flask import Flask, render_template, url_for, g, request, redirect, jsonify, make_response
from dbhelper import Database
from apscheduler.schedulers.background import BackgroundScheduler
from extraction_donnees import extract_data
from flask_json_schema import JsonSchema
from flask_json_schema import JsonValidationError
from schemas import plainte_insert_schema
import json
import datetime as dt
import converter as conv
from plainte import Plainte

app = Flask(__name__,static_url_path="", static_folder="static")
schema = JsonSchema(app)
sched = BackgroundScheduler()
sched.start()
sched.add_job(extract_data,'cron',hour=00,minute=1)

def get_db():
	db = getattr(g, '_database', None)
	if db is None:
		g._database = Database()
	return g._database

@app.teardown_appcontext
def close_connection(exception):
	db = getattr(g, '_database', None)
	if db is not None:
		db.disconnect()

@app.route('/')
def home_page():
	return render_template('home.html')

@app.route('/search', methods = ["GET"])
def search():
	attribute = request.args.get('select')
	value = request.args.get('search')
	results = get_db().get_data(attribute, value)
	return render_template("search_result.html", items=results)
	
@app.route('/plainte')
def plainte():
	return render_template("plainte.html")

@app.route('/api')
def api_page():
	return render_template("api.html")

@app.route('/api/doc')
def get_api_doc():
	return render_template("doc.html")
	

@app.route('/api/contrevenant',methods=["GET"])
def get_contrevenants():
	try:
		d1=request.args.get('du')
		d2=request.args.get('au')
		begin=dt.datetime.strptime(d1,"%Y-%m-%d")
		end=dt.datetime.strptime(d2,"%Y-%m-%d")
	except:
		return "Invalid date format or paramater names", 400
	contrevenants=get_db().get_contrevenants_by_date(begin,end)
	contrevenants=[c.__dict__ for c in contrevenants]
	return jsonify(contrevenants),200
	
@app.route('/api/etablissement',methods=["GET"])
def get_etablissement():
	etablissements=get_db().get_etablissement()
	etablissements=[e.__dict__ for e in etablissements]
	try:
		ctype=request.headers.get('Content-Type')
	except:
		return "No Content-Type specified", 400
	if ctype=="application/json":
		res = make_response(jsonify(etablissements),200)
		res.headers["Content-Type"]=ctype
		return res
	elif ctype=="application/xml":
		res = make_response(conv.etablissement_to_xml(etablissements),200)
		res.headers["Content-Type"]=ctype
		return res
	elif ctype=="text/csv":
		res = make_response(conv.etablissement_to_csv(etablissements),200)
		res.headers["Content-Type"]=ctype
		return res
	else:
		return "Invalid Content-Type", 400

@app.route('/api/plainte',methods=["POST"])
@schema.validate(plainte_insert_schema)
def insert_plainte():
	data = request.get_json()
	plainte=Plainte(data["id"],data["etablissement"],data["adresse"],data["ville"],data["date_visite"],data["prenom"],data["nom"],data["description"])
	plainte=get_db().insert_plainte(plainte)
	return jsonify(plainte.__dict__), 201
	
@app.route('/api/plainte/<id>', methods=["DELETE"])
def delete_plainte(id):
    plainte = get_db().get_plainte(id)
    if plainte is None:
        return "Invalid ID", 400
    else:
        get_db().delete_plainte(plainte)
        return "Plainte N:"+id+" was deleted", 200

		
if __name__ == '__main__':
	app.run(debug=True)



