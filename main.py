import customtkinter as ctk
import requests
import pandas as pd

app = ctk.CTk()
app.geometry("500x500")
app.title("Consulta Cep")
app.resizable(False,False)
# Fontes
font = ctk.CTkFont(family='Bahnschrift SemiBold Condensed',size=40)
quests = ctk.CTkFont(family='Bahnschrift',size=20)
anwsors = ctk.CTkFont(family='Bahnschrift',size=12)

def consultar():
    result_cep = ""
    result_cep = cep.get()
    result_cep = result_cep.replace("-","").replace(".","").replace(" ","")
    if len(result_cep) ==8:
        link = f'https://viacep.com.br/ws/{result_cep}/json/'
        requisicao = requests.get(link)

        dic_requisicao = requisicao.json()
        cep1 = dic_requisicao['cep']
        estado = dic_requisicao['uf']
        cidade = dic_requisicao['localidade']
        rua = dic_requisicao['logradouro']
        ddd = dic_requisicao['ddd']

        ### CRIANDO AS RESPOSTAS
        cepp = ctk.CTkLabel(app, text=f"{cep1}",font=anwsors)
        cepp.pack()
        cepp.place(x=100,y=300)
        ###
        estado = ctk.CTkLabel(app, text=f"Estado: {estado}",font=anwsors)
        estado.pack()
        estado.place(x=100,y=320)
        ###
        cidade = ctk.CTkLabel(app, text=f"Cidade: {cidade}",font=anwsors)
        cidade.pack()
        cidade.place(x=100,y=340)
        ###
        rua = ctk.CTkLabel(app, text=f"Rua: {rua}",font=anwsors)
        rua.pack()
        rua.place(x=100,y=360)
        ###
        ddd = ctk.CTkLabel(app, text=f"DDD: {ddd}",font=anwsors)
        ddd.pack()
        ddd.place(x=100,y=380)
        ###
    else:
        incorret = ctk.CTkLabel(app, text="Cep Incorreto",font=anwsors)
        incorret.pack()
        incorret.place(x=100,y=300)

        cepp.destroy()
        estado.destroy()
        cidade.destroy()
        rua.destroy()
        ddd.destroy()
        
        


text = ctk.CTkLabel(app, text="Consulta por CEP",font=font)
text.pack()
text.place(x=140,y=50)

text1 = ctk.CTkLabel(app, text="Digite o CEP:",font=quests)
text1.pack()
text1.place(x=100,y=150)

cep = ctk.CTkEntry(app,placeholder_text="Digite o CEP com os 8 digitos",width=300,font=quests)
cep.pack()
cep.place(x=100,y=185)

consultar = ctk.CTkButton(app,text="Consultar",font=quests,width=210,command=consultar)
consultar.pack()
consultar.place(x=140,y=260)

app.mainloop()