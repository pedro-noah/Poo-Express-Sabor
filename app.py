from modelos.restaurantes import Restaurante

restaurante_praca = Restaurante('Praca', 'Gourmet')
restaurante_praca.receber_avaliacao('Noah', 10)
restaurante_praca.receber_avaliacao('Livia', 3)



def main():
    """
    O main do projeto
    """
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()
    