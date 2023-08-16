from flask import render_template, request, redirect, url_for
from app import app, db
from app.models.tabelas import User

#as rotas dos sites são definidos por funções
#direciona ao index pela rota "/" ou "/index"
# @app.route('/')
# @app.route('/index')
# def index():
#     return render_template('base.html')

@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/login/', methods=['POST'])
def validation():
    n1 = request.form.get('email')
    print(n1)

    return render_template('admin.html')


# @app.route('/admin')
# def admin():
#      users = User.query.all()
#      return render_template('admin.html', users = users)