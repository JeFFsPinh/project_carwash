from flask import Flask, Blueprint
from project.blueprints.cars import view


bp = Blueprint('cars' ,__name__, url_prefix='/')
bp.add_url_rule('/', view_func=view.get_all, methods=['GET'])
bp.add_url_rule('/', view_func=view.create, methods=['POST'])


def init_app(app: Flask):
    app.register_blueprint(bp)