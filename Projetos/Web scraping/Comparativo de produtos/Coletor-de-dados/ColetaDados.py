# Ferramentas para modelagem de dados
import pandas as pd
import numpy

# ajuda para fazer pausas durante as requisições
import time

# Ferramentas para navegação em sites
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service



class ColetaDadosSite:
    df = pd.DataFrame()

    def __init__(self, nomeProduto):
        self.nomeProduto = nomeProduto

    def iniciar_navegador(self):
        opts = Options()
        opts.add_argument('--headless=new')#cria a opção de ocultar a janela
        # Instala o driver atual do google chrome e inicializa
        servico = Service(ChromeDriverManager().install())
        self.navegador = webdriver.Chrome(service=servico, options=opts)

    def pesquisa_amz(self):
        # entra e realiza a pesquisa no site
        self.navegador.get("https://www.amazon.com.br/")
        self.navegador.find_element(
            "xpath", '//*[@id="twotabsearchtextbox"]'
        ).send_keys(self.nomeProduto)
        self.navegador.find_element("xpath", '//*[@id="twotabsearchtextbox"]').submit()

        # tempo de pausa para abrir o site
        time.sleep(2)

    def coleta_dados_amz(self):
        # Armazena informações sobre o produto pesquisado
        self.prod_amz = {"loja": [], "nome": [], "valor": []}

        # coleta informações
        nome = list(
            self.navegador.find_elements(
                "xpath", '//*[@class= "a-size-base-plus a-color-base a-text-normal"]'
            )
        )
        valor = list(
            self.navegador.find_elements("xpath", '//*[@class= "a-price-whole"]')
        )

        # coleta nome da loja
        for i in range(1, 4):
            self.prod_amz["loja"].append("Amazon")

        # coleta nome dos produtos
        for i in nome:
            # se caso der erro, vai coletar a msg de erro
            try:
                if len(self.prod_amz["nome"]) >= 3:
                    break
                self.prod_amz["nome"].append(i.text)
            except:
                self.prod_amz.append("Deu erro no numero" + str(i))

        # coleta valor dos produtos
        for i in valor:
            try:
                if len(self.prod_amz["valor"]) >= 3:
                    break
                self.prod_amz["valor"].append("R$: " + i.text)
            except:
                print("erro")

    def pesquisa_ali(self):
        self.navegador.get("https://best.aliexpress.com/")
        self.navegador.find_element("xpath", '//*[@class="_24EHh"]').click()
        self.navegador.find_element("xpath", '//*[@class="search-key"]').send_keys(
            self.nomeProduto
        )
        self.navegador.find_element("xpath", '//*[@class="search-key"]').submit()
        # tempo de espera
        time.sleep(2)

    def coleta_dados_ali(self):
        self.prod_ali = {"loja": [], "nome": [], "valor": []}

        nome = self.navegador.find_elements(
            "xpath", '//*[@class="manhattan--titleText--WccSjUS"]'
        )
        valor = self.navegador.find_elements(
            "xpath", '//*[@class="manhattan--price-sale--1CCSZfK"]'
        )

        # coleta o nome dp site
        for i in range(1, 4):
            self.prod_ali["loja"].append("AliExpress")

        # coleta o nome dos produtos
        for i in nome:
            try:
                if len(self.prod_ali["nome"]) >= 3:
                    break
                self.prod_ali["nome"].append(i.text)
            except:
                print("Erro produto")

        # coleta valor dos produtos
        for i in valor:
            try:
                if len(self.prod_ali["valor"]) >= 3:
                    break
                self.prod_ali["valor"].append(i.text)
            except:
                print("erro valor ali")

        # def resultado_ali(self):
        for i in self.prod_ali:
            print(str(i) + "\n")

    def fechar_navegador(self):
        self.navegador.close()

    def dataFrame(self):
        df_amz = pd.DataFrame(self.prod_amz, columns=["loja", "nome", "valor"])
        df_ali = pd.DataFrame(self.prod_ali, columns=["loja", "nome", "valor"])
        self.df = pd.concat([df_amz, df_ali], ignore_index=True)
        print(self.df)


def executa_class(produto):
    novo = ColetaDadosSite(produto)
    novo.iniciar_navegador()
    novo.pesquisa_amz()
    novo.coleta_dados_amz()
    novo.pesquisa_ali()
    novo.coleta_dados_ali()
    novo.fechar_navegador()
    novo.dataFrame()

prod = input('Escreva o nome do produto que deseja pesquisar: ')
executa_class(prod)