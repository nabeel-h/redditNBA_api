from db import db
from models.subreddits import SubredditModel
from models.yearseasons import YearSeasonModel
		
class SubmissionModel(db.Model):
	__tablename__ = 'submissions'
	
	id = db.Column(db.Integer,primary_key=True)
	title = db.Column(db.String(500))
	submission_url = db.Column(db.String(1000))
	timestamp = db.Column(db.String(22))
	std_measure = db.Column(db.Float(precision=3))
	submission_redditID = db.Column(db.String(7))
	
	subreddit_id = db.Column(db.Integer, db.ForeignKey('subreddits.id'))
	subreddit = db.relationship('SubredditModel')
	
	yearseason_id = db.Column(db.Integer, db.ForeignKey('yearseasons.id'))
	yearseason = db.relationship('YearSeasonModel')
	
	def __init__(self,yearseason_id,subreddit_id,title,submission_url,submission_redditID,timestamp,std_measure):
		self.yearseason_id = yearseason_id
		self.subreddit_id = subreddit_id
		self.title = title
		self.submission_redditID = submission_redditID
		self.submission_url = submission_url
		self.timestamp = timestamp
		self.std_measure = std_measure
		
		#self.subreddit = subreddit
		#self.year_season = year_season
		
	def json(self):
		return {'title':self.title,'timestamp':self.timestamp,'std_measure':self.std_measure,'subreddit_id':self.subreddit_id, 'year_season_id':self.yearseason_id,'submission_url':self.submission_url,'submission_redditID':self.submission_redditID}
		
	def delete_from_db(self):
		db.session.delete(self)
		db.session.commit()
		
	def save_to_db(self):
		db.session.add(self)
		db.session.commit()
		
	@classmethod
	def find_by_redditID(cls,submission_redditID):
		return cls.query.filter_by(submission_redditID=submission_redditID).first()
		
	@classmethod
	def find_by_yrseasonsub(cls, yearseason_subreddit):
		try:
			split = yearseason_subreddit.split('&')
			yearseason,subreddit = split[0],split[1]
			
			yearseason_id = YearSeasonModel.convert_to_id(yearseason)[0]
			subreddit_id = SubredditModel.convert_to_id(subreddit)[0]
			
			results = cls.query.filter_by(yearseason_id=yearseason_id).filter_by(subreddit_id=subreddit_id).all() 
			return {"results":[result.json() for result in results]}
		except:
			return None
		
	@classmethod
	def find_by_yrsub(cls,year_subreddit):
		try:
			#year_subreddit = 2016&LAL
			split = year_subreddit.split('&')
			year,subreddit = split[0],split[1]

			yearseason_list = [year+'-reg_season',year+'-offseason',year+'-playoffs']
			
			subreddit_id = SubredditModel.convert_to_id(subreddit)[0]
			yearseason_ids = [YearSeasonModel.convert_to_id(yearseason_list[0])[0],YearSeasonModel.convert_to_id(yearseason_list[1])[0],YearSeasonModel.convert_to_id(yearseason_list[2])[0]]
			
			search_results = cls.query.filter_by(subreddit_id=subreddit_id)	
			results = list(filter(lambda x: x.yearseason_id in yearseason_ids, search_results))

			return {"results": [result.json() for result in results]}
		except:
			return None
			
	@classmethod
	def find_by_subreddit(cls,subreddit):
		try:
			subreddit_id = SubredditModel.convert_to_id(subreddit)[0]
			
			results = cls.query.filter_by(subreddit_id=subreddit_id)
			
			return {"results": [result.json() for result in results]}
		except:
			return None
			
	@classmethod
	def find_by_seasonsub(cls, season_subreddit):
		try:
			#season_subreddit = offseason&LAL
			split = season_subreddit.split("&")
			season,subreddit = split[0],split[1]
			
			print(season,subreddit,"step1 pass")
			
			list_ofseasons = YearSeasonModel.return_all()
			print(list_ofseasons,"step2 pass")
			
			list_ofseasons_id =[]
			for yearseason in list_ofseasons:
				if yearseason.yearseason_name.split('-')[1] == season:
					list_ofseasons_id.append(yearseason.id)
			print(list_ofseasons_id)
			
			subreddit_id = SubredditModel.convert_to_id(subreddit)[0]
			
			search_results = cls.query.filter_by(subreddit_id=subreddit_id)
			results = list(filter(lambda x: x.yearseason_id in list_ofseasons_id, search_results))
			
			return {"results":[result.json() for result in results]}
		except:
			return None
		
		
		
