from flask import Flask, render_template, url_for, g, request, redirect
from dbhelper import Database

app = Flask(__name__)


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
	items = get_db().get_data(attribute, value)
	return render_template("search_result.html", items=items)

if __name__ == '__main__':
	app.run()
