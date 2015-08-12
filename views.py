from flask import render_template, request
from app import app

@app.route('/')
def index():
    options = {}
    return render_template('index.html', **options)

@app.route('/contact/')
def contact():
    options = {}
    return render_template('contact.html', **options)

@app.route('/photos/')
def photos():
    options = {}
    return render_template('photos.html', **options)