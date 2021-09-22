from flask import Flask, app
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, reqparse, Resource, abort
db = SQLAlchemy()


def create_app(config_name):
    
    app = Flask(__name__)


     # Initializing flask extensions
    db.init_app(app)

