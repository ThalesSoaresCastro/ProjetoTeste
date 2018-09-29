import  pycep_correios

class Consulta_cep:
    
    def consulta(self,val):
        endereco = pycep_correios.consultar_cep(val)
        return endereco
    
