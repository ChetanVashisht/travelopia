from flask import jsonify, request, Flask
from database import createTables
from travelController import travelController

app = Flask(__name__)
app.register_blueprint(travelController, url_prefix='/travellers')

@app.after_request
def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return response

@app.route('/')
def status():
    return jsonify({'status': 'Running'})

if __name__ == "__main__":
    createTables()
    app.run(host='0.0.0.0', port=8000, debug=False)
