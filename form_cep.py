import tkinter as tk
from form import *

class Form_cep:

    def interface(self):
        
        janela = tk.Tk()
        janela.title("Endereco")

        

def main():

    def bt_click():
        #janelinha = tk.Tk()
        #janelinha.title("Janelinha invocada")
        lb["text"] = "funcionou!!"


    janela = tk.Tk()
    janela.title("teste de titulo")
    #janela["bg"] = "red"
    #lb = tk.Label(janela,text = "Teste de Label")
    
    lb = tk.Label(janela, text = "teste do Label")
    lb.place(x=100,y=150)    

    bt = tk.Button(janela, width=20, text="OK", command = janelaTest )
    
    #gerenciador de layout place
    bt.place(x = 100, y = 100)
    #lb.place(x=100, y=100)

    #gerenciador de layout
    
    #gerenciador de layout
   
    janela.geometry("800x400")

    janela.mainloop()

def janelaTest():
    Form().janela()
