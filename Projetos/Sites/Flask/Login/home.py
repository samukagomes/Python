from flask import Flask
from flask import render_template

app = Flask(__name__)

# @app.route('/')
# dwf index(/)

@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/user/<user>')
def usuario(user):
    return f'Usuario: {user}'

app.run()