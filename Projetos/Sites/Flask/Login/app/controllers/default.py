from flask import render_template
from app import app
from app.models.tabelas import User

# from app.models.forms import loginForm
#as rotas dos sites são definidos por funções
#direciona ao index pela rota "/" ou "/index"
@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html')


@app.route('/login/')
def login():
    # form = loginForm()
    return render_template('login.html')


