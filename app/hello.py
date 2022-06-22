from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import create_database, database_exists
from flask import render_template
from datetime import datetime
import pytz

# Intatiate Flask and SQLAlchemy
app = Flask(__name__)
db_url = 'postgresql://admin:password@postgres:5432/testdb'

if not database_exists(db_url):
    create_database(db_url)

db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = db_url

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    body = db.Column(db.String(300), nullable=False)
    create_at = db.Column(db.DateTime, nullable=False,default=datetime.now(pytz.timezone('Asia/Tokyo')))


@app.route("/")
def index():
    return render_template('index.html')


