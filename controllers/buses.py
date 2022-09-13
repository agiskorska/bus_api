from db import bus_db as db
from werkzeug import exceptions


def index(req):
    return [b for b in db.buses], 200

def create(req):
    new_bus = req.get_json()
    db.buses.append(new_bus)
    return new_bus, 201

def show(req, uid):
    return find_by_uid(uid), 200

def update(req, uid):
    bus = find_by_uid(uid)
    data = req.get_json()
    for key, val in data.items():
        bus[key] = val
    return bus, 200

def destroy(req, uid):
    bus = find_by_uid(uid)
    db.buses.remove(bus)
    return 204

def find_by_uid(uid):
    try:
        return next(bus for bus in db.buses if bus['id'] == uid)
    except:
        raise exceptions.NotFound(f"We don't have this bus with id: {uid}!")