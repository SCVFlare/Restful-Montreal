from flask import Flask, render_template, url_for, g, request, redirect
from dbhelper import Database
from apscheduler.schedulers.background import BackgroundScheduler
from extraction_donnees import extract_data

app = Flask(__name__)
sched = BackgroundScheduler()
sched.start()
sched.add_job(extract_data,'cron',hour=00,minute=01)


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
	return "Hi bruh!"



if __name__ == '__main__':
	app.run(debug=True)