import json
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/run')
def run():
    with open('occupation.json', 'r') as file:
        data = json.load(file)
    return jsonify(data)

@app.route('/lidar-hub/api/v1/event_zones')
def event_zones():
    with open('event_zones.json', 'r') as file:
        data = json.load(file)
    return jsonify(data)

@app.route('/lidar-hub/api/v1/event_zones/realtime')
def event_zones_realtime():
    with open('event_zones_realtime.json', 'r') as file:
        data = json.load(file)
    return jsonify(data)

@app.route('/lidar-hub/api/v1/event_zones/timeseries')
def event_zones_timeseries():
    with open('event_zones_timeseries.json', 'r') as file:
        data = json.load(file)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
