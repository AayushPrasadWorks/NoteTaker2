from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def forms():
    return render_template("text.html")

@app.route('/', methods=['POST', 'GET'])
def form_insert():
    print(request.data)
    if request.method == 'POST':
       name = request.form.get('name')
       message = request.form.get('message')
       date = request.form.get('date')
       ser = Server()
       ser.add(name, message, date)
    else:
        name = request.form.get('name')
        message = request.form.get('message')
        date = request.form.get('date')
        return name
    
