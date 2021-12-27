from typing import List

from project.infra.database.main import Session
from project.infra.database.cars.model import CarModel

class CarsRepository:

    session = Session()

    def get_all(self) -> List[dict]:
        cars: List[CarModel] = self.session.query(CarModel).all()
        return [car.to_dict() for car in cars]

    def create(self, car: dict) -> None: 
        assert self.get_by_plate(car.get('plate')) is None, "This Car has been created before."

        car = CarModel(**car)
        self.session.add(car) 
        self.session.commit()

    def get_by_plate(self, plate: str) -> CarModel:
        car = self.session.query(CarModel).filter(CarModel.plate == plate).first()
        return car
