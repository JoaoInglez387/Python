nome = input('Digite seu nome: ')

while True:
    sexo = input('Digite seu sexo: ')
    if sexo == 'M' or sexo == 'F':
        break
    else:
        print('Dados inválidos!')

print('Dados Validos!')