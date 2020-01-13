from flask_wtf import FlaskForm
from flask import Flask, render_template, url_for, flash, redirect
from form import InsertForm, DeleteForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde270ba245'

@app.route("/", methods=['GET', 'POST'])
def insert():
    form = InsertForm()
    serv = server()
    if form.validate_on_submit():
        serv.add(form.name.data, form.message.data, form.date.data)

        

    
    


