import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate,identity
from resources.user import UserRegister
from resources.submissions import Submission, SignificantSubmissions, SignificantSubmissions_byyrsub, SignificantSubmissions_bysub,SignificantSubmissions_byseasonsub


from models.submissions import SubmissionModel
from models.yearseasons import YearSeasonModel
from models.subreddits import SubredditModel


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "nabeel"
api = Api(app)

jwt =JWT(app,authenticate,identity)

api.add_resource(Submission, '/submission/<string:submission_redditID>')
api.add_resource(SignificantSubmissions,'/sigsubs/<string:yearseason_subreddit>')
api.add_resource(UserRegister, '/register')
api.add_resource(SignificantSubmissions_byyrsub,'/sigsubs_yrteam/<string:year_subreddit>')
api.add_resource(SignificantSubmissions_bysub, '/sigsubs_sub/<string:subreddit>')
api.add_resource(SignificantSubmissions_byseasonsub,'/sigsubs_seasonsub/<string:season_subreddit>')

if __name__== '__main__':
	from db import db
	db.init_app(app)
	app.run(port=5000, debug=True)
