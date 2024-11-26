from conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, cliente, agencia, saldo=0):
        super().__init__(cliente, agencia, saldo)
        
    def sacar(self,valor: float) -> bool:    
        try:
            valor = float(valor)
        except:
            print('Erro, contem letra')
        else:
            if valor < 0 or valor > self.saldo:   
                print('Erro, saldo indisponivel')
                return False
            else:
                print('Saquei com sucesso!')
                self.saldo -= valor
                return True