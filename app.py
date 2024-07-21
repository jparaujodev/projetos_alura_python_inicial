from modelos.restaurante import Restaurante
from modelos.restaurante import Avaliacao

restaurante_chines =  Restaurante('Xininha', 'Chinês','2000')
restaurante_brasil = Restaurante('BraizlianFood', 'Br','2016')

restaurante_brasil.receber_avaliacao(Avaliacao('João', 1.5))
restaurante_brasil.receber_avaliacao(Avaliacao('pedrinho', 2))
restaurante_brasil.receber_avaliacao(Avaliacao('aline', 3.5))


def main():
    Restaurante.listar_restaurantes()
    

if __name__ == '__main__':
    main()
