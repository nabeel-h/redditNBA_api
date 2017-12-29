from flask_jwt import jwt_required
from flask_restful import Resource, reqparse
from models.submissions import SubmissionModel
from models.subreddits import SubredditModel
from models.yearseasons import YearSeasonModel

class Submission(Resource):
	parser = reqparse.RequestParser()
	
	parser.add_argument('yearseason_id',
		type=int,
		required=True,
		help="Every submission needs a yearseason_id value."
	)
	
	parser.add_argument('subreddit_id',
		type=int,
		required=True,
		help="Every submission needs a subreddit_id value."
	)
	
	parser.add_argument('submission_url',
		required=True,
		help="Every submission needs a submission_url value."
	)
	
	parser.add_argument('submission_title',
		required=True,
		help="Every submission needs a submission_title value."
	)
	
	parser.add_argument('timestamp',
		required=True,
		help="Every submission needs a timestamp value."
	)
	
	parser.add_argument('std_measure',
		type=float,
		required=True,
		help="Every submission needs a std_measure value."
	)
	
	def get(self,submission_redditID):
		submission = SubmissionModel.find_by_redditID(submission_redditID)
		if submission:
			return {'submission': submission.json()}
			
		return {'message': "Submission doesn't exist."}
	
	def post(self,submission_redditID):
		if SubmissionModel.find_by_redditID(submission_redditID):
			return {"message": "A submission with unique reddit submission ID: '{}' already exists.".format(submission_redditID)}, 400
			
		data = Submission.parser.parse_args()
		submission = SubmissionModel(data['yearseason_id'],data['subreddit_id'],data['submission_title'],data['submission_url'],submission_redditID,data['timestamp'],data['std_measure'])
		try:
			submission.save_to_db()
		except:
			return {"message":"An error occured inserting the submission"},500
		return submission.json(),201
		
	def delete(self,submission_redditID):
		submission = SubmissionModel.find_by_redditID(submission_redditID)
		if submission:
			submission.delete_from_db()
			
		return {'message': 'Submission deleted.'}
		
		
class SignificantSubmissions(Resource):
	def get(self,yearseason_subreddit):
		submission_results = SubmissionModel.find_by_yrseasonsub(yearseason_subreddit)
		if submission_results:
			return {'significant submissions':submission_results}
		return {"message":"Retrieval of significant submissions failed, check inputs."}