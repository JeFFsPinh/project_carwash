from flask import Flask
from project.blueprints import cars
from project.infra import database

app = Flask(__name__)

cars.init_app(app)
database.init_app()

if __name__ == '__main__':
    app.run(debug=True)
