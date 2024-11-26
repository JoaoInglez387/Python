from cliente import Cliente
from agencia import Agencia
from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca
import os

clientes = []
contas = []
agencias = []

def criar_clientes():
    # Instancia três objetos da classe cliente
                        
    clientes.append(Cliente('João Gabriel Soares Inglez', '052.150.531-71', '(69)9 3321-2464', 'Av. Barraco do macaco, N° 4823, Vilhena'))
    clientes.append(Cliente('Marcos Guilherme olivera', '026.758.126-34', '(69)9 7964-4124', 'Av. E o pix nada ainda, N° 2453, Vilhena'))
    clientes.append(Cliente('João Pretinho', '974.720.441-30', '(69)9 4212-1231', 'Av. Devedor, N° 5845, Vilhena'))
    clientes.append(Cliente('João Gurini', '944.930.751-93', '(69)9 9472-9731', 'Av. jardim da vida, N° 6245, Vilhena'))
    clientes.append(Cliente('João Vini', '813.031.631-01', '(69)9 7413-6413', 'Av. casada do sol, N° 5972, Vilhena'))
    clientes.append(Cliente('Nathan Grigo', '813.031.631-01', '(69)9 1392-6347', 'Rua viuva de flor, N° 2643, Vilhena'))

def print_clientes():
    # Imprime os atributos nome e cpf dos clientes
    
    for n, i in enumerate(clientes):
        print(f'ID: {n} - Cliente: {i.nome} - CPF: {i.cpf}')

def criar_conta():
    # Instancia três objetos da classe conta
    
    agencia = Agencia('0001')
    
    contas.append(ContaCorrente(clientes[0], agencia, 10000, 1000))
    contas.append(ContaCorrente(clientes[1], agencia))
    contas.append(ContaCorrente(clientes[2], agencia, 1200,500))
    contas.append(ContaPoupanca(clientes[3], agencia, 5200))
    contas.append(ContaPoupanca(clientes[4], agencia, 1200))
    contas.append(ContaPoupanca(clientes[5], agencia, 1000))

def print_contas():
    for i in contas:
        if type(i) == ContaCorrente:
            print(f'Número da agência: {i.agencia.banco.numero} | Nome do Banco: {i.agencia.banco.nome} | Tipo de conta: Conta Corrente\
            \nNome do Cliente: {i.cliente.nome} | Número da Conta: {i.numero}\
            \nSaldo da conta: R$ {i.saldo:.2f} \nLimite: R${i.limite:.2f} '.replace('.',','))
            print('-------------------------------------------------------------------------------------------')
            print()
            
        else:
            print(f'Número da agência: {i.agencia.banco.numero} | Nome do Banco: {i.agencia.banco.nome} | Tipo de conta: Conta Poupança\
            \nNome do Cliente: {i.cliente.nome} | Número da Conta: {i.numero}\
            \nSaldo da conta: R$ {i.saldo:.2f}'.replace('.',','))
            print('-------------------------------------------------------------------------------------------')
            print()
     
        
def encontrar_contas():
    while True:
        print_contas()
        numero = int(input('Digite o numero da conta: '))
        for conta in contas:
            if conta.numero == numero:
                return conta 
        print('Conta não encontrada!')
        
        
def main():
    criar_clientes()
    criar_conta()
    conta = encontrar_contas()
    
    while True:
        print()
        print(f'Bem vindo')
        try:
            recepecacao = int(input('Escolha uma opção:\
            \n (1) - Cadastrar cliente\
            \n (2) - Cadastrar conta\
            \n (3) - Mostra os clientes\
            \n (4) - Mostra as contas\
            \n (5) - Sacar\
            \n (6) - Depositar\
            \n (7) - Transfeir\
            \n (8) - Sair \
            \n>>>>> '))
            
            os.system('cls')
        except:
            print('Erro') 
        else:
            if recepecacao == 1:
                pass
            elif recepecacao == 2:
                pass
            elif recepecacao == 3:
                print_clientes()
                
            elif recepecacao == 4:
                print_contas()
                
            elif recepecacao == 5:
                encontrar_contas()
                
                valor = float(input('Digite o valor deseja sacar da conta: ').replace(',','.'))
                conta.sacar(valor)
                
            elif recepecacao == 6:
                encontrar_contas()
                
                valor = float(input('Digite o valor desejado depositar na conta: ').replace(',','.'))
                conta.depositar(valor)
                
            elif recepecacao == 7:
                destinatario = encontrar_contas()
            
                valor = float(input('Digite o valor da transferencia: ').replace(',','.'))
                conta.transferir(valor, destinatario)
                
            elif recepecacao == 8:
                break
            else:
                print('Erro')

main()
