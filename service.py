from flask import Flask
from flask import request
from flask import render_template
from Server import Server

app = Flask(__name__)

@app.route('/', methods=['GET'])
def forms():
    return render_template("text.html")

@app.route('/', methods=['POST'])
def form_insert():
    print(request.data)
    if request.method == 'POST':
       name = request.form['Name']
       message = request.form['Message']
       date = request.form['Date']
       ser = Server()
       ser.add(name, message, date)
       return render_template("text.html")
    return 'OK'
    
