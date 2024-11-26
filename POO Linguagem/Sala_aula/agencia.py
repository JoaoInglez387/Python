from banco import Banco

class Agencia:
    def __init__(self, numero):
        self.numero = numero
        banco = Banco('0001','Nubank')
        self.banco = banco