import json
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/run')
def run():
    with open('echo.json', 'r') as file:
        data = json.load(file)
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
