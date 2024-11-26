class cliente():
    def __init__(self, nome, cpf, endereco) -> None:
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco


class celular():
    def __init__(self, marca, valor: float) -> None:
        self.marca = marca
        self.valor = valor


clientes = []
celulares = []


def criar_cliente():
    clientes.append(cliente('João', '114419649-54', 'Vilhena'))
    clientes.append(cliente('Teste', '1964945-15', 'Cacoal'))


def print_cliente():
    for n, i in enumerate(clientes):
        print(f'Id: {n} | Nome: {i.nome} | CPF: {i.cpf} | Endereco: {i.endereco}')


celular_1 = celular('Xiomi', 1600)
celular_2 = celular('Sansugm', 1800)
celular_3 = celular('Positivo', 800)

print(celular_1.marca)


criar_cliente()
print_cliente()
