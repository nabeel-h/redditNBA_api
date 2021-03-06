# REST API for reddit submissions from the NBA community
https://reddit-nba-sub-api.herokuapp.com

## Description

This RESTFUL API returns reddit submissions JSON data including title, timestamp, submission url and a unit of measure used to determine the significance of the submission. 

The database of these submissions deemed significant were generated by a process that looked at all NBA reddit submissions from within all 31 communities. The submissions were selected by a process that identified spikes in submission activity and then extracted the highest rated submission in that time frame.

The code that identified and generated these submissions is [here](https://github.com/nabeel-h/port.io/blob/master/Notebooks/nba_reddit/On%20generating%20significant%20submission%20dates%20from%20a%20subreddit%20period.ipynb).

The API offers the following __GET__ methods to retrieve specific data from the postgresql db.

*Returns significant submissions during the 2015 regular season for the Los Angeles Lakers subreddit community.

```All submissions for particular season year and subseason and subreddit:- /sigsubs/<year>-<sub_season>&<subreddit>```

e.g :- https://reddit-nba-sub-api.herokuapp.com/sigsubs/2015-reg_season&LAL

*Returns significant submissions during the whole 2015 NBA season (including playoffs, offseason and regular season) for the Los Angeles Lakers subreddit community.

```All submissions for a particular season year and subreddit:- /sigsubs_yrteam/<year>&<subreddit>```

e.g :- https://reddit-nba-sub-api.herokuapp.com/sigsubs_yrteam/2015&LAL


* Returns all significant submissions across all years for the Los Angeles Lakers subreddit community.

```All submissions for particular subreddit across all years:- /sigsubs_sub/<subreddit>```

e.g :- https://reddit-nba-sub-api.herokuapp.com/sigsubs_sub/LAL


* Returns significant submissions from offseasons across all NBA seasons for the Los Angeles Lakers subreddit community.

```All submissions across all years for partiulcar subseason and subreddit:- /sigsubs_seasonsub/<sub_season>&<subreddit>```

e.g :- https://reddit-nba-sub-api.herokuapp.com/sigsubs_seasonsub/offseason&LAL


* There is additionally a __POST__ method available to update the database with new submission data if needed.

```endpoint : /submission/<unique_reddit_submission_id>```
```
reuquired header: {
	"yearseason_id":,
	"subreddit_id":,
	"submission_title":"",
	"timestamp":"",
	"std_measure":,
	"submission_url": ""
	}
```
	
*Finally there is __DELETE__ method available to delete a submission by its unique reddit submission id.

```endpoint: /submission/<unique_reddit_submission_id>```


## Implementation

This project was implemented with:
```
Flask
Postgresql
sqlalchemy
Nginx
uwsgi

The API is on a server running Ubuntu 16.04 through Digital Ocean.
Python 3.5.2
```

