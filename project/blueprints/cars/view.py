from flask import request, jsonify

from project.infra.database.cars.repository import CarsRepository
from project.blueprints.cars.utils import ValidationError, validate


repository = CarsRepository()

def get_all():
    try:
        cars = repository.get_all()
    except Exception:
        return "Internal Error", 500
    return jsonify({"cars": cars})

def create():
    data = request.json

    try:
        car = validate(data)
    except ValidationError as ve:
        return f"{ve}", 422
    
    try:
        repository.create(car)
    except AssertionError as ae:
        return f"{ae}", 422
    except Exception:
        return "Internal Error", 500

    return "OK", 200
