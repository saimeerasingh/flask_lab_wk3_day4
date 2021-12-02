from app import app
from flask import render_template , request
from models.event_list import *
from models.event import Event

@app.route('/events')
def index():
    return render_template('index.html', title = 'Events', events=events)

@app.route('/events', methods =["POST"]) 
def add_event():
    event_date = request.form['date']
    event_name = request.form['event_name'] 
    event_guests = request.form['guests'] 
    room_location = request.form['room_location']
    description = request.form['description']
    event_recurring = request.form['recurring']
    new_event = Event(event_date,event_name,event_guests,room_location,description,event_recurring)
    add_new_event(new_event)
    return render_template('index.html', title = 'Events', events=events)
    
    
    