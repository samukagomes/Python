from app import db

class User(db.Model):    

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String)
    senha = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    admin = db.Column(db.Integer)

    def __init__(self, nome, email, senha, admin):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.admin = admin
        