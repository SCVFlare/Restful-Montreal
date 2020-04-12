from flask import Flask, render_template, url_for, g, request, redirect, jsonify
from dbhelper import Database
from apscheduler.schedulers.background import BackgroundScheduler
from extraction_donnees import extract_data
from flask_json_schema import JsonSchema
from flask_json_schema import JsonValidationError
import json
import datetime as dt

app = Flask(__name__)
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

if __name__ == '__main__':
	app.run(debug=True)



