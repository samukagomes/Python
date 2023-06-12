import ColetaDados as cd
import pandas as pd
from tkinter import ttk,Tk
from tkinter import *

def comand_btn():
    novo = cd.ColetaDadosSite(str(nome_produto.get()))
    novo.iniciar_navegador()
    novo.pesquisa_amz() 
    novo.coleta_dados_amz()
    novo.pesquisa_ali()
    novo.coleta_dados_ali()
    novo.fechar_navegador()
    novo.dataFrame() 
    win_df = novo.df
    dados = ttk.Label(window,text=win_df.head()).pack()
         

window = Tk()
window.geometry('700x300')
texto = ttk.Label(text='Escreva o produto que deseja pesquisar:', font=('Roboto', 12))
texto.pack()

nome_produto = ttk.Entry(window, width=25)
nome_produto.pack()

btn = ttk.Button(window, text='Pesquisar', command=comand_btn)
btn.pack()

#win_df = pd.DataFrame(columns=['Loja', 'Nome', 'valor'])

window.mainloop()