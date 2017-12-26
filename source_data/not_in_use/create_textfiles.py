import json
import sqlite3

seasontypesList = []
subredditsList = []


with open('significant_subs.json') as fhand:
	data = json.load(fhand)
	for year in data:
		#print(year)
		for subreddit in data[year]:
			if subreddit not in subredditsList:
				subredditsList.append(subreddit)
			for season_type in data[year][subreddit]:
				year_season = year+'-'+season_type
				if year_season not in seasontypesList:
					seasontypesList.append(year_season)
				#for item in data[year][subreddit][season_type]:
					

with open('seasonyears_subreddits.json','w') as out:
	json.dump({"yearseasons":seasontypesList,"subreddits":subredditsList},out)
#print(seasontypesList)
#print(subredditsList)