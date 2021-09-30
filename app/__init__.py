from flask import Flask
from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from flask import request, jsonify, abort
from werkzeug.wrappers import response

# local import
from instance.config import app_config



# initialize sql-alchemy
db = SQLAlchemy()

def create_app(config_name):
    from app.models import Report
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

     # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

   

    
    


    return app