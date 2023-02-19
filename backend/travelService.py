from database import *

def get(id):
    return getTraveller(id)

def insert(traveller):
    return insertTraveller(traveller)

def getAll():
    return getTravellers()

def delete(id):
    return deleteTraveller(id)
