from sqlalchemy.orm import backref
from . import db

class Complainant(db.Model):
    __tablename__= 'complainants'
    
    id = db.Column(db.Integer, primary_key = True)
    fullname = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    phoneNo = db.column(db.Integer)
    profile_pic_path = db.Column(db.String)
    pass_secure = db.Column(db.String(255))
    reports = db.relationship('Report', backref = 'complainant', lazy = "dynamic")
    officers = db.relationship('Officers', backref = 'complainant', lazy = "dynamic")

class Report(db.Model):
    __tablename__ = "reports"


    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(1000))
    caseDetails = db.Column(db.String(5000))
    complainantId = db.Column(db.Integer, db.ForeignKey("complainants.id"))
    reports = db.relationship('Officers', backref = 'report', lazy = "dynamic")
   
class Officers(db.Model):
    __tablename__ = "officers"

    id = db.Column(db.Integer, primary_key = True)
    officername = db.Column(db.String(255))
    complainantId = db.Column(db.Integer, db.ForeignKey("complainants.id"))
    report = db.Column(db.Integer, db.ForeignKey("reports.id"))
