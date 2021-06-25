from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField

class New(FlaskForm):
    product_section = SelectField('Section', choices=[(1, "Outdoor Plants"), (2, "Indoor Plants"), (3, "Outdoor Paints"), (4, "Gardening Equipment")])
    report_type = SelectField('Type', choices=[("Damage"), ("Theft"), ("Injury"), ("Complaint"), ("Training"), ("Illness"), ("Technical")])
    description = StringField('Description')
    resolution = StringField('Resolution')
    complete = StringField('Complete')
    submit = SubmitField('Submit Report')