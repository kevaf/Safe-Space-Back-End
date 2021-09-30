
from app.main import main
from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from flask import request, jsonify, abort
from werkzeug.wrappers import response
from app.models import Report


@main.route('/reports/', methods=['POST', 'GET'])
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

@main.route('/reports/delete/<int:id>', methods=['DELETE'])
def report_delete(id, **kwargs):
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
        
@main.route('/reports/edit/<int:id>', methods=['PUT'])
def report_edit(id, **kwargs):
    # retrieve a report using it's ID
    report = Report.query.filter_by(id=id).first()
    if not report:
        # Raise an HTTPException with a 404 not found status code
        abort(404)


    if request.method == 'PUT':
        name = str(request.data.get('name', ''))
        report_details = str(request.data.get('report_details', ''))
        report.report_details = report_details
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
    
@main.route('/reports/fetch/<int:id>', methods=['GET'])
def report_fetch(id, **kwargs):
    # retrieve a report using it's ID
    report = Report.query.filter_by(id=id).first()
    if not report:
        # Raise an HTTPException with a 404 not found status code
        abort(404)    

    if request.method == 'GET':
        # GET
        response = jsonify({
            'id': report.id,
            'name': report.name,
            'date_created': report.date_created,
            'report_details': report.report_details
        })
        response.status_code = 200
        return response
    


