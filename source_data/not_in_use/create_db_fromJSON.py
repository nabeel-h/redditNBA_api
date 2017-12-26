'''

submission_id (PRIMARY KEY), subreddit_id, year, season_type_id, 			submission_title(string length 500),std_measure,num_posts,timestamp



'''

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
					

print(seasontypesList)
print(subredditsList)



connection = sqlite3.connect('ogdb.db')
cursor = connection.cursor()


create_seasontypes = "CREATE TABLE IF NOT EXISTS yearseasons (id integer, yearseason_name text NOT NULL)"
cursor.execute(create_seasontypes)

yearseason_dict = {}

insert_seasontypes = "INSERT INTO yearseasons VALUES(?,?)"
for _id,type in enumerate(seasontypesList):
	yearseason_dict[type] = _id
	insert_tuple = (_id,type)
	cursor.execute(insert_seasontypes,insert_tuple)
connection.commit()

print(yearseason_dict)


create_subreddits = "CREATE TABLE IF NOT EXISTS subreddits (id integer, subreddit_name text NOT NULL)"
cursor.execute(create_subreddits)

subreddits_dict = {}

insert_subreddittypes = "INSERT INTO subreddits VALUES (?,?)"
for id,subreddit in enumerate(subredditsList):
	subreddits_dict[subreddit] = id
	insert_tuple = (id,subreddit)
	cursor.execute(insert_subreddittypes,insert_tuple)
connection.commit()
print(subreddits_dict)




create_submissions = """CREATE TABLE IF NOT EXISTS submissions (
													submission_id PRIMARY KEY,
													yearseason_id integer,
													subreddit_id integer,
													submission_title text,
													submission_redditID text,
													submission_url text,
													timestamp text,
													std_measure float												
													)"""

												
												
cursor.execute(create_submissions)
connection.commit()
__id = 0
insert_subquery = "INSERT INTO submissions VALUES (?,?,?,?,?,?,?,?)"			
with open('significant_subs.json') as fhand:
	data = json.load(fhand)
	for year in data:
		#print(year)
		for subreddit in data[year]:
			subreddit_id = subreddits_dict[subreddit]
			for season_type in data[year][subreddit]:
				year_season = year + '-' + season_type
				yearseason_id = yearseason_dict[year_season]
				for item in data[year][subreddit][season_type]:
					insert_tuple = (__id,yearseason_id,subreddit_id,item['submission_title'],item['submission_redditID'],item['submission_url'],item['timestamp'],item['std_measure'])
					
					cursor.execute(insert_subquery,insert_tuple)

					__id+=1
connection.commit()
connection.close()

