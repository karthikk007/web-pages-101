from flask import Flask, render_template, session, redirect
from functools import wraps

import pymongo

app = Flask(__name__)
app.secret_key = b'\xe4\xb8t\x0f\xf1\xd6\xe7\x0bm\xdf\xb7\xc4\x84*\n\x1e'

# Database
client = pymongo.MongoClient('localhost', 27017)
db = client.user_login_system


# Decorators

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/')
            
    return wrap

# Routes
from user import routes


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/dashboard/')
@login_required
def dashboard():
    return render_template('dashboard.html')