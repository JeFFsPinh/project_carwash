from flask import request, jsonify
from project.infra.database.cars.repository import CarsRepository


repository = CarsRepository()

def get_all():
    return jsonify({"cars": repository.get_all()})

def create():
    car = request.json
    repository.create(car)
    return "OK", 200
