from abc import ABC, abstractclassmethod

class Conta(ABC):
    numero = 0
    
    def __init__(self, cliente, agencia, saldo = 0):
        self.cliente = cliente
        Conta.numero += 1
        self.numero = Conta.numero
        self.agencia = agencia
        self.saldo = saldo
      
    
    @abstractclassmethod
    def sacar(self, valor):
        pass   
            
            
    def depositar(self, valor) -> None:
        try:
            valor = float(valor)
        except:
            print('Erro, contem letra')
        else:
            if valor < 0:   
                print('Erro, deposito invalido')
                return False
            else:
                print('Depositado com sucesso!')
                self.saldo += valor
                return True
            
    def transferir(self, valor, conta_destino):
        try:
            valor = float(valor)
        except:
            print('Erro, digite um valor valido')
        else:
            if self.sacar(valor):
                conta_destino.depositar(valor)
                print('Transferencia realizada com sucesso')
                return True
            else:
                print('Erro, transferencia não realizada')