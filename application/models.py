from application import db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField

class Types(db.Model):
    type_id = db.Column(db.String(10), primary_key=True)
    severity = db.Column(db.String(10), nullable=False)
    role_responsibility = db.Column(db.String(10))
    fixed_in_days = db.Column(db.Integer)
    policies = db.Column(db.String(200))
    reports = db.relationship('Reports', backref='types')

class Reports(db.Model):
    report_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_section = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    incident_date = db.Column(db.DateTime, default=datetime.now)
    resolution = db.Column(db.String(200))
    complete = db.Column(db.String(1))
    report_type = db.Column(db.String(10), db.ForeignKey('types.type_id'), nullable=False)


