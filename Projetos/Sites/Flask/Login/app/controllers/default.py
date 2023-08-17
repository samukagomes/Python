from flask import render_template, request, redirect, url_for
from app import app, db
from app.models.tabelas import User

#as rotas dos sites são definidos por funções
#direciona ao index pela rota "/" ou "/index"
@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html')

@app.route('/login/')
def login():
    return render_template('login.html', alert = '')

@app.route('/login/', methods=['POST'])
def validation():
    #pega o email e a senha do forms
    email = request.form.get('email')
    senha = request.form.get('senha')
    #se o email e a senha for igual a do banco, ira redirecionar para a pagina de admin
    if User.query.filter(User.email.like(email)).all() and User.query.filter(User.senha.like(senha)).all():
        return redirect('/admin')
    else:
        alert = 'erro'
        msg = 'O campo email ou senha está incorreto!'
        return render_template('login.html', alert = alert, msg = msg)


@app.route('/admin')
def admin():
     users = User.query.all()
     return render_template('admin.html', users = users)