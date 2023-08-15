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
            self.cursor.execute("INSERT INTO user VALUES (NULL,'"+userName+"', '"+email+"', "+str(senha)+", "+str(status)+");""")
            self.banco.commit()
            print('deu certo')
        except:
            print('Erro na inserção de dados')

    def alterar(self, id, numeroColuna, novoValor):
        try:
            comamdo_alterar = lambda coluna: self.cursor.execute("UPDATE user SET "+coluna+" ='"+str(novoValor)+"' WHERE id='"+str(id)+"';")
            match numeroColuna:
                case 1:
                    comamdo_alterar('nome')
                    self.banco.commit()
                case 2:
                    comamdo_alterar('email')
                    self.banco.commit()
                case 3:
                    comamdo_alterar('senha')
                    self.banco.commit()     
                case _:
                    print('Coluna invalida')
        except:
            print('Erro no comamdo_alterar alterar')

    def deletar (self, id):
        try:
            self.cursor.execute("DELETE FROM user WHERE id='"+str(id)+"';")
            self.banco.commit()
        except:
            print('Erro ao deletar')

