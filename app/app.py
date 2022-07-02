from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import create_database, database_exists
from flask import render_template, request, redirect
from flask_login import UserMixin, LoginManager, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import pytz
import os

# Intatiate Flask and SQLAlchemy
app = Flask(__name__)
db_url = 'postgresql://admin:password@postgres:5432/testdb'

if not database_exists(db_url):
    create_database(db_url)

db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SECRET_KEY'] = os.urandom(24)
login_manager = LoginManager()
login_manager.init_app(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    body = db.Column(db.String(300), nullable=False)
    create_at = db.Column(db.DateTime, nullable=False,default=datetime.now(pytz.timezone('Asia/Tokyo')))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(150))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/", methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'GET':
        posts = Post.query.all()
        return render_template('index.html', posts=posts)

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User(username=username, password=generate_password_hash(password, method='sha256'))

        db.session.add(user)
        db.session.commit()
        return redirect('/login')
    else:
        return render_template('signup.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if check_password_hash(user.password, password):
            login_user(user)
            return redirect('/')

        db.session.add(user)
        db.session.commit()
        return redirect('/')
    else:
       return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')

@app.route("/create", methods=['GET', 'POST'])
@login_required
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
@login_required
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
@login_required
def delete(id):
    post = Post.query.get(id)

    db.session.delete(post)
    db.session.commit()
    return redirect('/')
    
