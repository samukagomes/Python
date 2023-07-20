from h11 import SWITCHED_PROTOCOL
import ColetaDados as cd
import pandas as pd
from PySimpleGUI import (Window, Text, Input, 
                         Button, Column, 
                         HSeparator, Push)

layout_esquerda = [
    [Push(),Text('Escreva o nome de um produto:', key='-LABEL1-'),Push()], 
    [Input(key='-PESQUISA-')],
    [Push(),Button('Enviar', key='-ENVIAR-'), 
     Button('Graficos', key='-GRAFICOS-'),Push()]
    ]

layout_direita = [
    [Push(),
     Text(key='-LOJA-'), 
     Text(key='-NOME-'),
     Text(key='-VALOR-'), 
     Push()]
    ]

layout = [
    [Column(layout_esquerda)], [HSeparator()], [Column(layout_direita)]
    ]

window=Window("Coleta de dados" , size=[800,200], layout=layout, element_justification="center")

dados_df = pd.DataFrame()

def webScraping(produto):
    pesquisa = cd.ColetaDadosSite(produto)
    pesquisa.iniciar_navegador()
    pesquisa.pesquisa_amz()
    pesquisa.coleta_dados_amz()
    pesquisa.pesquisa_ali()
    pesquisa.coleta_dados_ali()
    pesquisa.fechar_navegador()
    pesquisa.dataFrame()
    pesquisa.exportar_csv()
    window['-LOJA-'].update(pesquisa.df['loja'])
    window['-NOME-'].update(pesquisa.df['nome-produto'])
    window['-VALOR-'].update(pesquisa.df['valor'])


while True:
    #lê os eventos e valores da janela
    event, value = window.read()
    print(event, value)

    #switch e case do python
    match event:
        case '-ENVIAR-':
            if value['-PESQUISA-'] == '':
                window['-LABEL1-'].Update(text_color = "red")
            else:
                window['-LABEL1-'].Update(text_color = "Black")
                webScraping(value['-PESQUISA-'.upper()])
        case None:
            break

window.close()