from flask_restful import Api
import app


class Config:

    api = Api(app)
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:kev2214@localhost/safespace'

    