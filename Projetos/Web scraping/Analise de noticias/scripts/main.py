from bs4 import BeautifulSoup as bf
import httpx

endpoint = input('escreva o tema da noticia que deseja pesquisar: ')
response = httpx.get('https://g1.globo.com/busca/?q='+endpoint)
soup = bf(response.text, 'html.parser')

link = soup.find_all('a')

for i in range(0,10):
    print(str(i)+" "+link[i].get('href'))