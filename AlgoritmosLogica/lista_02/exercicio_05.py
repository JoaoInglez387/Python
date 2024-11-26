num = int(input('Digite seu número: '))
if (num%3 == 0 and num%7 == 0):
    print('Múltiplo de 3 e de 7')
elif num % 3 == 0:
    print('Múltiplo de 3')
elif num % 7 == 0:
    print('Múltiplo de 7')
else:
    print('Não é múltiplo de nenhum')