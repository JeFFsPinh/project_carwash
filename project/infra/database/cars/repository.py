from typing import List

from project.infra.database.main import Session
from project.infra.database.cars.model import CarModel

class CarsRepository:

    session = Session()

    def get_all(self) -> List[dict]:
        cars: List[CarModel] = self.session.query(CarModel).all()
        return [car.to_dict() for car in cars]

    def create(self, car) -> None: 
        car = CarModel(plate=car.get('plate', ""))
        self.session.add(car)
        self.session.commit()
