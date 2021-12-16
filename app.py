from flask import Flask
from project.blueprints import cars

app = Flask(__name__)

cars.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
