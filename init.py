from consulta_cep import *

def main():
    #print(Consulta_cep().consulta('12235750'))

    #print(Consulta_cep().rua('12235750'))
    
    endereco = Consulta_cep().consulta('12235750')
    print(endereco)



if __name__ == '__main__':
    main()