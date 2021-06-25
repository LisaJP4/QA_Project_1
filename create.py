from application import db
from application.models import Types, Reports
from flask_sqlalchemy import SQLAlchemy

db.drop_all()
db.create_all() 
db.session.commit()

#adding values to the types table:
damage = Types(type_id="Damage", severity="Medium", role_responsibility="Employee", fixed_in_days=7, policies="In case of damage, either accidental or deliberate, employees should hastily clear the area to ensure customer safety")
theft = Types(type_id="Theft", severity="High", role_responsibility="Manager", fixed_in_days=1, policies="In case of suspected theft, employees must immediately inform their manager who will inform the police")
injury = Types(type_id="Injury", severity="High", role_responsibility="Employee", fixed_in_days=1, policies="If an employee or customer is seriously injured, first aid should be administered and, if needed, emergency services should be called")
complaint = Types(type_id="Complaint", severity="Medium", role_responsibility="Employee", fixed_in_days=7, policies="If a customer wishes to make a complaint, employees should inform their manager, who will log a record of the complaint")
training = Types(type_id="Training", severity="Low", role_responsibility="Manager", fixed_in_days=30, policies="Employees will be required to undergo additional training sessions when new systems are introduced or updated, or new machinery is introduced to the floor")
illness = Types(type_id="Illness", severity="Low", role_responsibility="Employee", fixed_in_days=30, policies="Employees are entitled to paid sick leave as defined and explained in their contracts, however, they are required to log Return To Work reports upon their return")
technical = Types(type_id="Technical", severity="Medium", role_responsibility="Employee", fixed_in_days=7, policies="If systems go down, employees are required to paper log stock changes where necessary and apologise to customers for any inconvenience caused")
db.session.add(damage)
db.session.add(theft)
db.session.add(injury)
db.session.add(complaint)
db.session.add(training)
db.session.add(illness)
db.session.add(technical)
db.session.commit()

report1 = Reports(product_section="Outdoor Plants", description="Patricia [employee] slipped on spilled water leaking out of the outdoor plants onto the patio", complete="N", report_type="Injury")
report2 = Reports(product_section="Outdoor Paint", description="Customer complained that the fence paint they purchased was too watery and did not mix properly", complete="Y", report_type="Complaint", resolution="Customer was offered a full refund and a voucher to purchase additional paint. They accepted the money but did not accept the voucher")
report3 = Reports(product_section="Indoor Plants", description="Intoxicated individual entered the store and fell into the display of flowers by the entrance", complete="Y", report_type="Damage", resolution="Customer was billed for the minor damaged caused: four bunches of roses crushed")
db.session.add(report1)
db.session.add(report2)
db.session.add(report3)
db.session.commit()
