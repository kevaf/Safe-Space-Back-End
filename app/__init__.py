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

    @app.route('/reports/', methods=['POST', 'GET'])
    def reports():
        if request.method == "POST":
            name = str(request.data.get('name', ''))
            report_details = str(request.data.get('report_details', ''))
            if name:
                report = Report(name=name,report_details =report_details )
                report.save()
                response = jsonify({
                    'id': report.id,
                    'name': report.name,
                    'date_created': report.date_created,
                    'report_details': report.report_details
                })
                response.status_code = 201
                return response
        else:
            # GET
            reports = Report.get_all()
            results = []

            for report in reports:
                obj = {
                    'id': report.id,
                    'name': report.name,
                    'date_created': report.date_created,
                    'report_details': report.report_details
                }
                results.append(obj)
            response = jsonify(results)
            response.status_code = 200
            return response

    @app.route('/reports/<int:id>', methods=['GET', 'PUT', 'DELETE'])
    def report_manipulation(id, **kwargs):
     # retrieve a report using it's ID
        report = Report.query.filter_by(id=id).first()
        if not report:
            # Raise an HTTPException with a 404 not found status code
            abort(404)

        if request.method == 'DELETE':
            report.delete()
            return {
            "message": "report {} deleted successfully".format(report.id) 
         }, 200

        elif request.method == 'PUT':
            name = str(request.data.get('name', ''))
            report.name = name
            report.save()
            response = jsonify({
                'id': report.id,
                'name': report.name,
                'date_created': report.date_created,
                'report_details': report.report_details
            })
            response.status_code = 200
            return response
        else:
            # GET
            response = jsonify({
                'id': report.id,
                'name': report.name,
                'date_created': report.date_created,
                'report_details': report.report_details
            })
            response.status_code = 200
            return response


    return app