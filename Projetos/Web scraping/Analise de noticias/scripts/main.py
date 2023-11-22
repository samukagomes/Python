from bs4 import BeautifulSoup as bf
import httpx

class reportagem():
    def __init__(self, endpoint):
        self.endpoint = endpoint 

    def pesquisa(self):
        response = httpx.get('https://g1.globo.com/busca/?q='+self.endpoint)
        self.soup_g1 = bf(response.text, 'html.parser')

        response = httpx.get('https://g1.globo.com/busca/?q='+self.endpoint)
        self.soup_uol = bf(response.text, 'html.parser')

    def g1(self):
        div = self.soup_g1.find_all('div', 'widget--info__text-container', limit=2)

        self.site = {}
        link=div[0].find('a')
        self.site['link'] = link
        print(self.site)


endpoint = input('escreva o tema da noticia que deseja pesquisar: ')

reportagem = reportagem(endpoint)
reportagem.pesquisa()
reportagem.g1()