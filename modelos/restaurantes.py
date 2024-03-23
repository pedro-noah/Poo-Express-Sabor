from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    """Representa um restaurante e suas características."""

    restaurantes = []

    def __init__(self, nome, categoria):
        """
        Inicializa uma instância de Restaurante.

        Parâmetros:
        - nome (str): O nome do restaurante.
        - categoria (str): A categoria do restaurante.
        """
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        """Retorna uma representação em string do restaurante."""
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        """Exibe uma lista formatada de todos os restaurantes."""
        print(f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliação".ljust(25)} | {"Status"}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        """Retorna um símbolo indicando o estado de atividade do restaurante."""
        return '⌧' if self._ativo else '☐'
    
    def alternar_estado(self):
        """Alterna o estado de atividade do restaurante."""
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        """
        Registra uma avaliação para o restaurante.

        Parâmetros:
        - cliente (str): O nome do cliente que fez a avaliação.
        - nota (float): A nota atribuída ao restaurante (entre 1 e 5).
        """
        if 0 < nota <= 5: 
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        """Calcula e retorna a média das avaliações do restaurante."""
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media
        
    def adicionar_no_cardapio(self, item):
        '''Adicina os itens no cardapio do restaurante.'''
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)
    
    @property        
    def exibir_cardapio(self): 
        print(f'Cardapio do Reetaurante {self._nome}\n')
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'):
                mensagem = f'{i}. Nome: {item._nome} | Preco: R${item._preco} | Descricao: {item.descricao}'
                print(mensagem)
            else:
                mensagem = f'{i}. Nome: {item._nome} | Preco: R${item._preco} | Tamanho: {item.tamanho}'
                print(mensagem)
                
            
        











'''
Estudo de Exemplo de uma classe chamada Pessoa:
class Pessoa:
    pessoas = []
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        Pessoa.pessoas.append(self)
        
    def __str__(self):
        return f'{self.nome} tem {self.idade} anos e trabalha de {self.profissao}'
    
    @classmethod
    def listar_pessoas(cls):
        for pessoa in cls.pessoas:
            print(pessoa.nome)
            
    @classmethod
    def aniversario(cls, pessoa):
        pessoa.idade += 1
        
    @classmethod
    def saudacao(cls, pessoa):
        print(f'Seja Bem vindo(a) {pessoa.nome}')
    
pessoa1 = Pessoa('Paulo', 22, 'Padeiro')
print(pessoa1)
Pessoa.listar_pessoas()
Pessoa.aniversario(pessoa1)
print(pessoa1)
Pessoa.saudacao(pessoa1)

OU

class Pessoa:
    def __init__(self, nome='', idade=0, profissao=''):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'{self.nome}, {self.idade} anos, {self.profissao}'

    @property
    def saudacao(self):
        if self.profissao:
            return f'Olá, sou {self.nome}! Trabalho como {self.profissao}.'
        else:
            return f'Olá, sou {self.nome}!'

    def aniversario(self):
        self.idade += 1
'''

