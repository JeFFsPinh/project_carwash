import sqlalchemy as db
from project.infra.database.main import Base

class CarModel(Base):
    __tablename__ = 'Cars'

    id = db.Column(db.Integer, primary_key=True)
    plate = db.Column(db.String, nullable=False)

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'plate': self.plate
        }

