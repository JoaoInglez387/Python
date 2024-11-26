class Main:
    pass

print("Testando novo projeto")

from Cliente import cliente

from Conta import Conta

c1 = cliente("João", "11415-1125")
conta = Conta(c1.nome, 6565, 0)

print(conta.titular, 'Numero: ', conta.numero, 'Seu saldo: ', conta.saldo)