from typing import List


class CarsRepository:

    cars: List[dict] = []

    def get_all(self) -> List[dict]:
        return self.cars
    
    def create(self, car) -> None: 
        self.cars.append(car)
