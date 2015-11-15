"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskWebProject import app

from flask import Flask, url_for, json, request

# app = Flask(__name__)
json_var = {"sup": "yay"}

@app.route('/addresses', methods = ['GET', 'POST'])
def api_address():
    if request.method == 'POST':
        print "HELLO"
        # print request.mimetype
        # print request.get_json()
        # if request.headers['Content-Type'] == 'application/json':
        # return json.dumps(request.json) + '\n'
        return json.dumps(json_var)
        # else:
        #   return "Unsupported Media Type!"

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