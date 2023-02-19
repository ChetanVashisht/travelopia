from flask import jsonify, request, Blueprint
import travelService

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
    return jsonify(travelService.getAll())

@travelController.route('/<id>', methods=["GET"])
def getTraveller(id):
    return jsonify(travelService.getTraveller(id))

@travelController.route('/', methods=["POST"])
def createTraveller():
    return jsonify(travelService.insert(request.json))

@travelController.route('/<id>', methods=["DELETE"])
def deleteTraveller(id):
    return jsonify(travelService.delete(id))
