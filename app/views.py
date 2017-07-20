from flask import render_template, request
from app import app

@app.route('/')
def homepage():
    name = request.args.get('name') if request.args.get('name') else '<unknown>'
    return render_template('homepage.html', name=name)