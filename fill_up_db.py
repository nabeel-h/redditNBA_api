import json
from models.submissions import SubmissionModel
from models.yearseasons import YearSeasonModel
from models.subreddits import SubredditModel
from db import db

#need to use a relative file path for the static json files that will be used to load up
#the database before the first request. So I used the os library for this
import os
current_file_directory = os.path.dirname(__file__)

seasonyears_subreddits_path = os.path.join(current_file_directory,'seasonyears_subreddits.json')
significant_subs_path = os.path.join(current_file_directory,'significant_subs.json')


def fill_up_db():
	with open(seasonyears_subreddits_path) as fhand:
		data = json.load(fhand)
		
		#fill up subreddits and year_seasons tables
		list_of_subreddits = data['subreddits']
		list_of_yearseasons = data['yearseasons']
		
		for subreddit in list_of_subreddits:
			insert_sub = SubredditModel(subreddit)
			db.session.add(insert_sub)
			db.session.commit()
		
		for yearseason in list_of_yearseasons:
			insert_yearseason = YearSeasonModel(yearseason)
			db.session.add(insert_yearseason)
			db.session.commit()
			
		#build dict for id reference
		subreddits_dict = {}
		yearseason_dict = {}
		for subreddit in list_of_subreddits:
			subreddit_retrieve_id = SubredditModel.convert_to_id(subreddit)[0]
			subreddits_dict[subreddit] = subreddit_retrieve_id
		for yearseason in list_of_yearseasons:
			yearseason_retrieve_id = YearSeasonModel.convert_to_id(yearseason)[0]
			yearseason_dict[yearseason] = yearseason_retrieve_id
			
	#insert all submissions
	with open(significant_subs_path) as fhand:
		data = json.load(fhand)
		for year in data:
			for subreddit in data[year]:
				subreddit_id = subreddits_dict[subreddit]
				for season_type in data[year][subreddit]:
					year_season = year + '-' + season_type
					#print(year_season)
					yearseason_id = yearseason_dict[year_season]
					#print(subreddit_id,yearseason_id)
					for sub_item in data[year][subreddit][season_type]:
						insert_sub = SubmissionModel(yearseason_id,subreddit_id,sub_item['submission_title'],sub_item['submission_url'],sub_item['submission_redditID'],sub_item['timestamp'],sub_item['std_measure'])
						db.session.add(insert_sub)
						db.session.commit()
						
	return {'message':'database successfully filled'}
	

