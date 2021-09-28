from app import db


class Report(db.Model):
    """This class represents the Reoorts table."""

    __tablename__ = 'reports'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    report_details = db.Column(db.String(2000))

    def __init__(self, name,report_details ):
        """initialize with name."""
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