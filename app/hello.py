from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import create_database, database_exists
from flask import render_template

# Intatiate Flask and SQLAlchemy
app = Flask(__name__)
db_url = 'postgresql://admin:password@postgres:5432/testdb'

if not database_exists(db_url):
    create_database(db_url)

db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = db_url

@app.route("/")
def hello():
    return render_template('hello.html')