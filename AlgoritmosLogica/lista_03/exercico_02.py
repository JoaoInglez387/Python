while True:
    n_01 = float(input('Digite seu primeiro numero: '))
    n_02 = float( input('Digite seu segundo numero: '))
    print(f'{n_01 + n_02}')

    pergunta = input('Deseja continuar a aplicação? s/n\n')
    if pergunta == 's':
        continue
    else:
        print('Finalizado a aplicação!'),
        break

continuar = 's'
while continuar == 's':
    n_01 = float(input('Digite seu primeiro numero: '))
    n_02 = float( input('Digite seu segundo numero: '))
    print(f'{n_01 + n_02}')
    continuar = input('Deseja continuar a aplicação? s/n\n')
