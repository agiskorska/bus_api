from db import bus_db as db
from werkzeug import exceptions


def index(req, tid):
    return [b for b in db.buses if b['calling_at'].count(tid)>0], 200