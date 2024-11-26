from conta import Conta

class ContaCorrente(Conta):
    def __init__(self, cliente, agencia, saldo=0, limite = 100.00) -> None:
        super().__init__(cliente, agencia, saldo)
        self.__limite = limite
        
    def sacar(self, valor):
        try:
            valor = float(valor)
        except:
            print('Erro, contem letra')
        else:
            if valor <= 0:
                print('Erro, valor invalido')
                return False
            elif valor > self.saldo + self.__limite:
                print('Erro, saldo indisponivel')
                return False
            else:
                print('Saquei com sucesso!')
                self.saldo -= valor
                return True
            
    @property
    def limite(self):
        return self.__limite