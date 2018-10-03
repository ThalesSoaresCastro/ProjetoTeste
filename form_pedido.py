from tkinter import *

class Form_pedido:

    def interface(self):

        janelaPedido = Tk()
        janelaPedido['bg'] = '#F2F2F2'
        janelaPedido.title('Pedido')

        lbCardapio = Label(janelaPedido, 'Escolha um sabor:')
        lbCardapio.pack(side= LEFT)


        janelaPedido.geometry('500x500')
        janelaPedido.mainloop()