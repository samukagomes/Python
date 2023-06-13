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
    lb_df_loja = ttk.Label(frame_df, text=novo.df['loja'])
    lb_df_nome = ttk.Label(frame_df, text=novo.df['nome'])
    lb_df_valor = ttk.Label(frame_df, text=novo.df['valor'])

    lb_df_loja.grid(column=0, row=0)
    lb_df_nome.grid(column=1, row=0)
    lb_df_valor.grid(column=2, row=0)
    
window = Tk()
window.title('Coleta de dados')
window.geometry('700x300')

lb_texto = ttk.Label(text='Escreva o produto que deseja pesquisar:', font=('Roboto', 12))
nome_produto = ttk.Entry(window, width=25)
btn_pesquisar = ttk.Button(window, text='Pesquisar', command=comand_btn)
frame_df = ttk.Frame(window, borderwidth=5, relief="ridge", width=350, height=100)


lb_texto.grid(column=0, row=0, padx=175,pady=[50,10])
nome_produto.grid(column=0, row=1)
btn_pesquisar.grid(column=0, row=2, pady=10)
frame_df.grid(column=0, row=3)

window.mainloop()