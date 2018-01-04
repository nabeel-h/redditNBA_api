from app import app
from db import db

db.init_app(app)

@app.before_first_request
def create_tables():
	db.create_all()
	
	from models.submissions import SubmissionModel
	if db.session.query(SubmissionModel).count() < 1:
		from fill_up_db import fill_up_db
		print(fill_up_db())  
	