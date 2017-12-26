from db import db

class SubredditModel(db.Model):
	__tablename__ = 'subreddits'
	
	id = db.Column(db.Integer, primary_key=True)
	subreddit_name = db.Column(db.String(20))
	
	#submissions = db.relationship('SubmissionModel', lazy='dynamic')
	
	def __init__(self,subreddit_name):
		self.subreddit_name = subreddit_name
		
	def json(self):
		return {'subreddit':self.subreddit_name, 'submissions':[item.json() for item in self.submissions.all()]}
	
	def save_to_db(self):
		db.session.add(self)
		db.session.commit()
		
	def delete_from_db(self):
		db.session.delete(self)
		db.session.commit()
	
	@classmethod	
	def convert_to_id(cls, subreddit_name):
		result = db.session.query(SubredditModel.id).filter_by(subreddit_name=subreddit_name).first()
		if result:
			return result
		return None
		
	@classmethod	
	def convert_from_id(cls, subreddit_id):
		result= db.session.query(SubredditModel.subreddit_name).filter_by(id=subreddit_id).first()
		if result:
			return result
		return None