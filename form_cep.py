import tkinter as tk
from consulta_cep import *

class Form_cep:

    def interface(self):
        

        def procura_cep():
           
           endereco=Consulta_cep().consulta(cep.get())
           
           logadouro.delete(0, 'end')
           logadouro.insert(0, endereco['end'])
           logadouro['bg'] = '#F3F781'
           
           bairro.delete(0, 'end')
           bairro.insert(0, endereco['bairro'])
           bairro['bg'] = '#F3F781'
           
           cidade.delete(0, 'end')
           cidade.insert(0, endereco['cidade'])
           cidade['bg'] = '#F3F781'
           
           estado.delete(0, 'end')
           estado.insert(0, endereco['uf'])
           estado['bg'] = '#F3F781'


        janela = tk.Tk()
        janela['bg'] = '#F2F2F2'
        janela.title("Endereco")

        cep = tk.Entry(janela)
        cep.place(x= 100, y=50,width=100)
        lbCep = tk.Label(janela, text='CEP: ')
        lbCep['bg'] = '#F2F2F2'
        lbCep.place(x = 25, y=50)

        logadouro = tk.Entry(janela)
        logadouro.place(x= 100, y=100,width=300)
        lbLog = tk.Label(janela, text='Logadouro: ')
        lbLog['bg'] = '#F2F2F2'
        lbLog.place(x = 25, y=100)

        bairro = tk.Entry(janela)
        bairro.place(x= 100, y=150,width=300)
        lbBairro = tk.Label(janela, text='Bairro: ')
        lbBairro['bg'] = '#F2F2F2'
        lbBairro.place(x = 25, y=150)

        cidade = tk.Entry(janela)
        cidade.place(x= 100, y=200,width=300)
        lbCity = tk.Label(janela, text='Cidade: ')
        lbCity['bg'] = '#F2F2F2'
        lbCity.place(x = 25, y=200)

        estado = tk.Entry(janela)
        estado.place(x= 100, y=250,width=300)
        lbState = tk.Label(janela, text='Estado: ')
        lbState['bg'] = '#F2F2F2'
        lbState.place(x = 25, y=250)

        btProcuraCep = tk.Button(janela, text = "Procurar",command = procura_cep )
        btProcuraCep.place(x = 170, y=280)

        btConfirmar = tk.Button(janela, text = "Confirmar")
        btConfirmar.place(x = 250, y=280)

        btVoltar = tk.Button(janela,text = "Voltar")
        btVoltar.place(x = 340, y=280)

        janela.geometry('450x350')
        janela.mainloop()