from app import app
from db import db
from models.submissions import SubmissionModel

db.init_app(app)

@app.before_first_request
def create_tables():
	db.create_all()
	
	#if database is already not populated then populate items
	if db.session.query(SubmissionModel).count() < 1:
		from fill_up_db import fill_up_db
		print(fill_up_db())