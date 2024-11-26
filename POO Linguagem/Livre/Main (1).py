from Cliente import cliente

clientes = []

def cadastro_cliente():
        clientes.append(cliente('Nome do cliente','CNPJ ou CPF','Nome fantasia'))
     
def print_clientes():
    for n, i in enumerate(clientes):
        print(f'ID: {n} - Cliente: {i.nome} - CNPJ ou CPF: {i.cnpj_cpf} - Nome fantasia: {i.nome_fantasia}')
        print()
        
def print_verificacao():
    for n, i in enumerate(clientes):
        print(f'ID: {n} - Cliente: {i.nome} - CNPJ ou CPF: {i.cnpj_cpf} - Nome fantasia: {i.nome_fantasia} - Verificacao: {i.verificacao}')
        print()
        
def print_geral():
    cadastro_cliente()
    
    while True:
        print(f'Bem vindo')
        try:
            recepecacao = int(input('Escolha uma opção:\
            \n (1) - Cadastrar cliente\
            \n (2) - Mostra os clientes\
            \n (3) - Verificação\
            \n (4) - Sair \
            \n>>>>> '))
        except:
            print('Erro')
        else:
            if recepecacao == 1:
                pass
            elif recepecacao == 2:
                print_clientes()
            elif recepecacao == 3:
                print_verificacao()
            elif recepecacao == 4:
                break
            else:
                print('Erro')
        
print_geral()