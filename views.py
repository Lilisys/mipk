from flask import render_template, request
from app import app

@app.route('/')
def index():
    options = {}
    return render_template('index.html', **options)

@app.route('/locations/')
def locations():
    options = {}
    return render_template('locations.html', **options)

@app.route('/media/')
def media():
    options = {}
    return render_template('media.html', **options)

@app.route('/events/')
def events():
    options = {}
    return render_template('events.html', **options)

@app.route('/contact/')
def contact():
    options = {}
    return render_template('contact.html', **options)