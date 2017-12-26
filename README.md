# My REST API for significant reddit submissions from the NBA community

## Installation

'''
pip install Flask
python app.py
'''

## Description

This RESTFUL API returns reddit submissions data including title, timestamp, submission url and a unit of measure used to determine the significance of the submission.

This data can be pulled via the GET method by providing both the season year/type ('2015-reg_season') and the acronym for the NBA team ('LAL'). eg GET '2015-reg_season&LAL'

## Implementation

This project is implemented using Flask and sqlite3.
