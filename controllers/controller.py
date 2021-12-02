from app import app
from flask import render_template , request
from models.event_list import *
from models.event import Event

@app.route('/events')
def index():
    return render_template('index.html', title = 'Events', events=events)

    