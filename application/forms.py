from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length, ValidationError

class EmptyCheck:
    def __check__(self, message=None):
        if not message:
            message= "Please choose either Y or N"
        self.message = message

class New(FlaskForm):
    report_id = IntegerField('Report Number')
    product_section = SelectField('Section', choices=[(1, "Outdoor Plants"), (2, "Indoor Plants"), (3, "Outdoor Paints"), (4, "Gardening Equipment")])
    report_type = SelectField('Type', choices=[("Damage"), ("Theft"), ("Injury"), ("Complaint"), ("Training"), ("Illness"), ("Technical")])
    description = StringField('Description')
    resolution = StringField('Resolution')
    complete = StringField('Complete', validators=[DataRequired()])
    submit = SubmitField('Submit')
