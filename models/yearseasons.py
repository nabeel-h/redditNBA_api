from db import db

		
class YearSeasonModel(db.Model):
	__tablename__ = 'yearseasons'
	
	id = db.Column(db.Integer,primary_key=True)
	yearseason_name = db.Column(db.String(20))
	
	submissions = db.relationship('SubmissionModel', lazy='dynamic')
	
	
	def __init__(self,yearseason_name):
		self.yearseason_name = yearseason_name
		
	def json(self):
		return {'yearseason':self.yearseason_name, 'submissions':[item.json() for item in self.submissions.all()]}
		
	def save_to_db(self):
		db.session.add(self)
		db.session.commit()
		
	def delete_from_db(self):
		db.session.delete(self)
		db.session.commit()
	
	@classmethod	
	def convert_to_id(cls, yearseason_name):
		result = db.session.query(YearSeasonModel.id).filter_by(yearseason_name=yearseason_name).first()
		if result:
			return result
		return None
		
	@classmethod
	def convert_from_id(cls, yearseason_id):
		result =  db.session.query(YearSeasonModel.yearseason_name).filter_by(id=yearseason_id)
		if result:
			return result
		return None
