from h11 import SWITCHED_PROTOCOL
import ColetaDados as cd
import pandas as pd
from PySimpleGUI import (Window, Text, Input, 
                         Button, Column, 
                         HSeparator, Push)

layout_esquerda = [
    [Push(),Text('Escreva o nome de um produto:'),Push()], 
    [Input(key='-PESQUISA-')],
    [Push(),Button('Enviar', key='-ENVIAR-'), Button('Exportar'),Push()]
    ]

layout_direita = [
    [Push(),Text(key='-LOJA-'), Text(key='-NOME-'),
    Text(key='-VALOR-'), Push()]
    ]

layout = [
    [Column(layout_esquerda)], [HSeparator()], [Column(layout_direita)]
    ]

window=Window("Coleta de dados" , size=[800,200], layout=layout, element_justification="center")

def webScraping(produto):
    novo = cd.ColetaDadosSite(produto)
    novo.iniciar_navegador()
    novo.pesquisa_amz()
    novo.coleta_dados_amz()
    novo.pesquisa_ali()
    novo.coleta_dados_ali()
    novo.fechar_navegador()
    novo.dataFrame()
    window['-LOJA-'].update(novo.df['loja'])
    window['-NOME-'].update(novo.df['nome'])
    window['-VALOR-'].update(novo.df['valor'])


while True:
    event, value = window.read()
    print(event, value)

    match event:
        case '-ENVIAR-':
            webScraping(value['-PESQUISA-'])
        case None:
            break

window.close()