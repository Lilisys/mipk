from flask import render_template, request
from app import app
from schedule_api import *

@app.route('/')
def index():
    options = {}

    options['terms'] = get_terms()
    options['schools'] = get_schools(2060)

    return render_template('index.html', **options)

@app.route('/selectedterm/<term>',  methods=['POST', 'GET'])
def selectedterm(term):
    options = {}
    options[schools] = get_schools(term)

    return render_template('index.html', **options)

@app.route('/contact/')
def contact():
    options = {}
    return render_template('contact.html', **options)

@app.route('/photos/')
def photos():
    options = {}
    return render_template('photos.html', **options)