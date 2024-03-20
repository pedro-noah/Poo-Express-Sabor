from modelos.restaurantes import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('Praca', 'Gourmet')
bebida_suco = Bebida('Suco de Melancia', 5.0, 'G')
prato_pao = Prato('Pao', 2.0, 'Pao de entrada')




def main():
    """
    O main do projeto
    """
    print(bebida_suco)
    print(prato_pao)


if __name__ == '__main__':
    main()
    