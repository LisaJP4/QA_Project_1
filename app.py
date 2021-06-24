from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SECRET_KEY'] = 'lkdfjvn'

db = SQLAlchemy(app)

class Types_of_Report(db.Model):
    type_id = db.Column(db.String(10), primary_key=True)
    severity = db.Column(db.String(10), nullable=False)
    role_responsibility = db.Column(db.String(10))
    fixed_in_days = db.Column(db.Integer)
    policies = db.Column(db.String(200))
    reports = db.relationship('Reports', backref='types_of_report')

class Reports(db.Model):
    report_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_section = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    incident_date = db.Column(db.DateTime)
    complete = db.Column(db.String(1))
    report_type = db.Column(db.String(10), db.ForeignKey('types_of_report.type_id'), nullable=False)
    


if __name__ == '__main__':
    app.run(debug=True)