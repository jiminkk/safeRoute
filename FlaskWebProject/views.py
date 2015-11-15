"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskWebProject import app

from flask import Flask, url_for, json, request
import safeMap as sm

import os
import APP_STATIC

# settings
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_STATIC = os.path.join(APP_ROOT, 'static/content')

@app.route('/addresses', methods = ['GET', 'POST'])
def api_address():
    if request.method == 'POST':
        print "HELLO"
        # print request.mimetype
        print request.get_json()
        # if request.headers['Content-Type'] == 'application/json':
        # first_key = request.get_json()
        json_var = json.dumps(request.json)
        data = json.loads(json_var)
        print data

        ret_json = sm.return_Best_Route(data['Origin'], data['Destination'])
        return ret_json

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )