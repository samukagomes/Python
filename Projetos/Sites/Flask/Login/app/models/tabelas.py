from app import db

class User(db.Model):
    __tablename__= 'user'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    senha = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    admin = db.Column(db.Integer)

    def __init__(self, nome, email, senha, admin):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.admin = admin
        
    def __repr__ (self):
        return "<User %r>" % self.nome