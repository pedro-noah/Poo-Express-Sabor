from modelos.restaurantes import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('Praca', 'Gourmet')
bebida_suco = Bebida('Suco de Melancia', 5.0, 'G')
prato_pao = Prato('Pao', 2.0, 'Pao de entrada')

restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_pao)




def main():
    """
    O main do projeto
    """
    print(bebida_suco)
    print(prato_pao)


if __name__ == '__main__':
    main()
    