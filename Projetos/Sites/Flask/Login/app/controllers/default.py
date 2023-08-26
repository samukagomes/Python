from flask import render_template, request, redirect, url_for
from app import app, db
from app.models.tabelas import User

#as rotas dos sites são definidos por funções
#direciona ao index pela rota "/" ou "/index"
@app.route('/')
@app.route('/index/')
def index():
    return redirect ('/login/')

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
        if User.query.filter_by(email = email, admin= 1).all():
            return redirect('/admin')
        else: 
            alert = 'erro'
            msg = 'Você não tem acesso de administrador!'
            return render_template('login.html', alert = alert, msg = msg)
    else:
        alert = 'erro'
        msg = 'O campo email ou senha está incorreto!'
        return render_template('login.html', alert = alert, msg = msg)


@app.route('/admin')
def admin():
     users = User.query.all()
     return render_template('admin.html', users = users)

@app.route('/admin/cadastrar', methods = ['GET', 'POST'])
def cadastrar ():
    if request.method == 'POST':
        user = User(nome=request.form.get('nome'), 
                    email=request.form.get('email'), 
                    senha=request.form.get('senha'), 
                    admin=request.form.get('admin'))
        db.session.add(user)
        db.session.commit()
    return redirect('/admin')

@app.route('/admin/<int:id>/delete', methods=['GET', 'POST'])
def deletar(id):
    user = db.get_or_404(User, id)

    if request.method == 'POST':
        db.session(user)
        db.session.commit()
    return redirect('/admin')