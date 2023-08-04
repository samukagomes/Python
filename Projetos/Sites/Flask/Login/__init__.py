from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')        

@app.route('/login/')
def login():
    return render_template('login.html')

app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/user/<user>')
def usuario(user):
    return f'Usuario: {user}'

app.run()