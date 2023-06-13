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
    dados = ttk.Label(frame_df,text=novo.df).pack()
    

window = Tk()
frame1 = ttk.Frame(window)
window.geometry('700x300')

texto = ttk.Label(text='Escreva o produto que deseja pesquisar:', font=('Roboto', 12))
nome_produto = ttk.Entry(window, width=25)
btn = ttk.Button(window, text='Pesquisar', command=comand_btn)
frame_df = ttk.Frame(window, borderwidth=5, relief="ridge", width=200, height=100)

frame1.grid(column=0, row=0)
texto.grid(column=1, row=1)
nome_produto.grid(column=1, row=2)
btn.grid(column=1, row=3)
frame_df.grid(column=1, row=4)

window.mainloop()