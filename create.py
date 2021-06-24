from application import db
from application.models import Types, Reports

db.drop_all()
db.create_all()
#adding values to the types table:
damage = Types(severity="Medium", role_responsibility="Employee", fixed_in_days=7, policies="In case of damage, either accidental or deliberate, employees should hastily clear the area to ensure customer safety")
db.session.add(damage)
db.session.commit
