from application import db
from application.models import Types, Reports
from flask_sqlalchemy import SQLAlchemy

db.create_all() 
db.session.commit()

#adding values to the types table:
injury = Types(type_id="Injury", severity="High", role_responsibility="Employee", fixed_in_days=1, policies="If an employee or customer is seriously injured, first aid should be administered and, if needed, emergency services should be called")
db.session.add(injury)
db.session.commit()
