from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash


class Report(db.Model):
    """This class represents the Reoorts table."""

    __tablename__ = 'reports'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    report_details = db.Column(db.String(2000))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    def __init__(self, name,report_details ):
        """initialize with name and report details"""
        self.name = name
        self.report_details= report_details 

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_reports(cls,id):
        report = Report.query.filter_by(id=id).first()

        return report

    @staticmethod
    def get_all():
        return Report.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "".format(self.name)



class User(UserMixin, db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    Address = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
        
