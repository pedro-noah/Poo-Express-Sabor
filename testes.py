class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self.ativo = False
        
        
    def __str__(self):
        return f'O titular {self.titular} tem {self.saldo} de saldo.'
    
    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo
    
    @classmethod
    def ativar_conta(cls, conta):
        if conta.ativo == False:
            conta.ativo = True
            print('Conta ativada!')
        else:
            print('Ja esta ativado...')
        
        
    
conta1 = ContaBancaria(23, 763.5)
conta2 = ContaBancaria(33, 2344.43)
print(conta1)
print(conta2)
ContaBancaria.ativar_conta(conta1)
        
            
        
        