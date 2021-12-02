
from models.event import *

event1 = Event("3/12/2021", 'DJ night', 20,'Hopper','Party all night!',True)
event2 = Event("5/12/2021",'Pool Party',15,'Swimming Pool','Bring your bathing suits!', False)

events = [event1,event2]

def add_new_event(event):
    events.append(event)

