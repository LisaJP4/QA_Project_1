from application import app, db
from flask import Flask, render_template

@app.route('/')
def welcome():
    return render_template('welcome.html')
     