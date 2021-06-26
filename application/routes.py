from application import app, db
from flask import Flask, render_template, request
from application.models import Types, Reports
from application.forms import New
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from os import getenv

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/readreports')
def readreports():
    all_reports = Reports.query.all()
    reports_string = ""
    for issues in all_reports:
        reports_string += "<br>"+ "<br>"+ str(issues.report_id) + "   |   " + str(issues.incident_date) + "   |   " +  issues.report_type + "   |   " + issues.description + "  |  " +  issues.complete + "  |  " + str(issues.resolution) + "   |   "
    return render_template('readreports.html') + reports_string

@app.route('/newreport', methods=['GET', 'POST'])
def newreport():
    error = ""
    form = New()

    if request.method == 'POST':
        nreport = Reports(product_section = form.product_section.data, description = form.description.data, resolution = form.resolution.data, complete = form.complete.data, report_type = form.report_type.data)
        db.session.add(nreport)
        db.session.commit()
    return render_template("newreport.html", form=form)
    
@app.route('/policies')
def policies():
    all_policies = Types.query.all()
    policies_string = ""
    for policy in all_policies:
        policies_string += "<br>"+ "<br>"+ policy.type_id + "   |   "  + policy.policies + "  |  "
    return render_template('policies.html') + policies_string

#@app.route('/updatereport', methods=['GET', 'POST'])
#def updatereport():
#    error = ""
#    form = New()
#
#    if request.method == 'POST':
#        find_report = Reports.query.filter_by(report_id=form.report_id.data)
#        for change in find_report:
#            find_report.resolution = form.resolution.data
#            find_report.complete = form.complete.data
#            db.session.commit()
#    return render_template("updates.html", form=form)

@app.route('/resolve/', methods=['GET', 'POST'])
def resolve():
    error = ""
    form = New()

    if request.method == 'POST':
        find_report = Reports.query.get(form.report_id.data)
        find_report.resolution = form.resolution.data
        find_report.complete = form.complete.data
        db.session.commit()
    return render_template("resolve.html", form=form)
    