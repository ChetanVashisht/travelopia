from flask import jsonify, request, Blueprint

results = [
    {
        "name": "namus",
        "email": "4namus@fff.com",
        "destination": "Europe",
        "travellerCount": "201",
        "budget": "2200"
    }
]

travelController = Blueprint('travellers', __name__)

@travelController.route('/', methods=["GET"])
def getTravellers():
    return jsonify(results)

@travelController.route('/<id>', methods=["GET"])
def getTraveller(id):
    return jsonify(results)
