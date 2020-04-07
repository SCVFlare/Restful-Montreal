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
    return "Hello World!"



if __name__ == '__main__':
    app.run()
