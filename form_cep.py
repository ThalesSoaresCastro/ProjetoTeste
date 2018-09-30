from tkinter import *
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


        janela = Tk()
        janela['bg'] = '#F2F2F2'
        janela.title("Endereco")

        lbJanela = Label(janela, text = 'Cadastro de Endereco')
        lbJanela['bg'] = '#F2F2F2'
        #lbJanela.place(x = 170, y = 25)
        lbJanela.pack(side=TOP)


        cep = Entry(janela)
        cep.place(x= 100, y=50,width=100)
        lbCep = Label(janela, text='CEP: ')
        lbCep['bg'] = '#F2F2F2'
        lbCep.place(x = 25, y=50)

        logadouro = Entry(janela)
        logadouro.place(x= 100, y=100,width=300)
        lbLog = Label(janela, text='Logadouro: ')
        lbLog['bg'] = '#F2F2F2'
        lbLog.place(x = 25, y=100)

        bairro = Entry(janela)
        bairro.place(x= 100, y=150,width=300)
        lbBairro = Label(janela, text='Bairro: ')
        lbBairro['bg'] = '#F2F2F2'
        lbBairro.place(x = 25, y=150)

        cidade = Entry(janela)
        cidade.place(x= 100, y=200,width=300)
        lbCity = Label(janela, text='Cidade: ')
        lbCity['bg'] = '#F2F2F2'
        lbCity.place(x = 25, y=200)

        estado = Entry(janela)
        estado.place(x= 100, y=250,width=300)
        lbState = Label(janela, text='Estado: ')
        lbState['bg'] = '#F2F2F2'
        lbState.place(x = 25, y=250)

        btProcuraCep = Button(janela, text = "Procurar",command = procura_cep )
        btProcuraCep.place(x = 170, y=280)

        btConfirmar = Button(janela, text = "Confirmar")
        btConfirmar.place(x = 250, y=280)

        btVoltar = Button(janela,text = "Voltar")
        btVoltar.place(x = 340, y=280)

        janela.geometry('450x350')
        janela.mainloop()