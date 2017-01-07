#!/usr/bin/python
"""OPEN DATA API."""

import os

from flask import Flask
from flask import flash
from flask import render_template
from flask import request
from flask import session
from sqlalchemy.orm import sessionmaker
from tabledef import *
engine = create_engine('sqlite:///opendata.db', echo=True)

app = Flask(__name__)


@app.route('/')
def home():
    """Home."""
    if not session.get('logged_in'):
        return render_template('form.html')
    else:
        return render_template('red.html')


@app.route('/login', methods=['POST'])
def do_admin_login():
    """Login."""
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])

    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]))
    result = query.first()
    if result:
        session['logged_in'] = True
    else:
        flash('Invalid credentials!')
        return render_template('login.html')
    return home()


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()


@app.route('/index', methods=['POST', 'GET'])
def index():
    return render_template('login.html')


@app.route('/test', methods=['POST', 'GET'])
def test():
    val = request.form['projectFilepath']
    # return render_template('login.html', error=error)
    return val


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0', port=80)
