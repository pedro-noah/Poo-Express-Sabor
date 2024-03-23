from modelos.restaurantes import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('Praca', 'Gourmet')
bebida_suco = Bebida('Suco de Melancia', 5.0, 'G')
bebida_suco.aplicar_desconto()
prato_pao = Prato('Pao', 2.0, 'Pao de entrada')
prato_pao.aplicar_desconto()
sobremesa_sorvete = Sobremesa('Sorvete de Baunilha', 13.0, 'Gelado', 'Grande')
sobremesa_sorvete.aplicar_desconto()

restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_pao)
restaurante_praca.adicionar_no_cardapio(sobremesa_sorvete)




def main():
    """
    O main do projeto
    """
    restaurante_praca.exibir_cardapio


if __name__ == '__main__':
    main()
    