from modelos.avaliacao import Avaliacao
class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria): 
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self.avaliacao = []
        Restaurante.restaurantes.append(self)
        
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'NOME'.ljust(25)} | {'CATEGORIA'.ljust(25)} | {'AVALIACAO'.ljust(25)} |{'STATUS'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes.ljust(25))} |{restaurante.ativo}')
            
    @property
    def ativo(self):
        return '✓' if self._ativo else '✕'    
    
    def alternar_estado(self):
        self._ativo = not self._ativo
        
    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self.avaliacao.append(avaliacao)
      
    @property    
    def media_avaliacoes(self):
        if not self.avaliacao:
            return 0
        soma_das_notas = sum(avaliacao._nota for avaliacao in self.avaliacao)
        quantidade_das_notas = len(self.avaliacao)
        media = round(soma_das_notas / quantidade_das_notas, 1)
        return media














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

