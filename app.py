from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug import exceptions
from controllers import buses, towns

app = Flask(__name__)
CORS(app)

@app.route('/')
def welcome():
    return 'Hello, this is the future of the buses!'

@app.route('/bus/')
def bus():
    functions = {
        'GET': buses.index,
        'POST': buses.create
    }
    res, code = functions[request.method](request)
    return jsonify(res), code

@app.route('/bus/<int:bus_id', methods = ['PUT', 'GET', 'DELETE'])
def bus_handler(bus_id):
    functions = {
        'GET': buses.show,
        'PUT': buses.update,
        'DELETE': buses.destroy
    }
    res, code = functions[request.method](request, bus_id)
    return jsonify(res), code

@app.route('/town/<string:town_name>', methods = ['GET'])
def town(town_name):
    functions = {
        'GET': towns.index
    }
    res, code = functions[request.method](request, town_name)
    return jsonify(res), code

if __name__ == '__main__':
    app.run(debug=True)