"""
Routes and views for the flask application.
"""
from flask import Flask
from flask_restful import Resource, Api
from datetime import datetime
from flask import render_template
from FlaskWebProject import app

app = Flask(__name__)
api = Api(app)
api.add_resource(HelloWorld, '/')

@app.route('/')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


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