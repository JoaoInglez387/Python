saldo = 1000.00


print('Bem vindo Usuario\n')
while True:

    op_1 = int(input('Escolha uma opção abaixo:\n\
        (1) Consultar saldo\n\
        (2) Efetuar saque\n\
        (3) Efetuar depósito\n\
        (4) Sair\n\
        \nDigite sua opção: '))

    if op_1 == 1:
        print(f'Seu saldo é de saldo R$ {saldo:.2f}')
        pergunta = input('Deseja voltar ao menu inciar? S / N\n')
        if pergunta.upper() == 'S':
            continue
        else:
            break
 # ---------------------------------------------------------------------------------
    if op_1 == 2:
        sacar = float(input('Quantos vc deseja sacar?\nR$ '))

        if sacar > saldo:
            print('Não é possivel sacar um valor acima do seu saldo')

            pergunta = input('Deseja voltar ao menu inciar? S / N\n')
            if pergunta.upper() == 'S':
                continue
            else:
                break

        saldo -= sacar
        print(
            f'Vc sacou R$ {sacar:.2f} Seu saldo é de saldo é de R$ {saldo:.2f}')

        pergunta = input('Deseja voltar ao menu iniciar? S / N\n')
        if pergunta.upper() == 'S':
            continue
        else:
            break
# ---------------------------------------------------------------------------------

    if op_1 == 3:
        deposito = float(input('Quantos vc deseja depositar?\nR$ '))
        saldo += deposito
        print(
            f'Vc depositou R$ {deposito:.2f} Seu saldo é de saldo é de R$ {saldo:.2f}')

        pergunta = input('Deseja voltar ao menu iniciar? S / N\n')
        if pergunta.upper() == 'S':
            continue
        else:
            break
# ---------------------------------------------------------------------------------
    if op_1 == 4:
        break
    else:
        print('Operação Invalida!')
