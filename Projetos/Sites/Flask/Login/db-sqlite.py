import sqlite3

class comando_banco:
    def __init__(self, Database):
        self.nome_banco = Database

    def conexao(self):
        try:
            self.banco = sqlite3.connect(self.nome_banco)
            self.cursor = self.banco.cursor()

        except:
            print('erro na conexão com o banco de dados')

    def inserir(self, userName, email, senha, status):
        try:
            self.cursor.execute("INSERT INTO user VALUES(NULL,'"+str(userName)+"', '"+str(email)+"', '"+str(senha)+"', '"+str(status)+"');")
        except:
            print('Erro na inserção de dados')

db = comando_banco('banco')
db.conexao()
db.inserir('alfredo', 'alfredo.alf@gmail.com', "123456", '0')