import sqlalchemy as db
from project.infra.database.main import Base

class CarModel(Base):
    __tablename__ = 'Cars'

    id = db.Column(db.Integer, primary_key=True)
    plate = db.Column(db.String(7), nullable=False)
    model = db.Column(db.String, nullable=True)
    brand = db.Column(db.String, nullable=True)
    description = db.Column(db.String, nullable=False)
    color = db.Column(db.String, nullable=False)

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'plate': self.plate,
            'model': self.model or 'Not Specified',
            'brand': self.brand or 'Not Specified',
            'description': self.description,
            'color': self.color
        }
