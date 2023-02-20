from flask import jsonify, request, Flask, send_from_directory
from database import createTables
from travelController import travelController
import os

app = Flask(__name__, static_folder='./dist')
app.register_blueprint(travelController, url_prefix='/travellers')

@app.route('/')
@app.route('/tourists')
def _home():
    return send_from_directory('./static/', 'index.html')

@app.route('/assets/<path:path>')
def send(path):
    return send_from_directory('./static/assets', path)


@app.after_request
def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return response

if __name__ == "__main__":
    createTables()
    app.run(host='0.0.0.0', port=8000, debug=False)
