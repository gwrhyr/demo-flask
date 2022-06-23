from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import create_database, database_exists
from flask import render_template, request, redirect
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


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        posts = Post.query.all()
        return render_template('index.html', posts=posts)

@app.route("/create", methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')

        POST = Post(title=title, body=body)

        db.session.add(POST)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('create.html')

@app.route("/<int:id>/update", methods=['GET', 'POST'])
def update(id):
    post = Post.query.get(id)
    if request.method == 'GET':
        return render_template('update.html', post=post)
    else:
        post.title = request.form.get('title')
        post.body = request.form.get('body')

        db.session.commit()
        return redirect('/')
    
@app.route("/<int:id>/delete", methods=['GET'])
def delete(id):
    post = Post.query.get(id)

    db.session.delete(post)
    db.session.commit()
    return redirect('/')
    
