class Conta:
    def __int__(self, titular, numero, saldo):
        
        self.saldo = 0
        self.numero = numero
        self.titular = titular
        
    @property 
    def saldo(self):
        return self.get_saldo
    
    @saldo.setter
    def set_nome(self, saldo):
        if (saldo < 0):
            print("o saldo não pode ser negativo")
        else:
            self._saldo = saldo