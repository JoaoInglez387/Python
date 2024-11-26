nome_capital = input('Qual é a Capital do Brasil? ')

while nome_capital != 'Brasilia':
        print('Resposta errada!')
        nome_capital = input('Digite novamente: ')

print('Resposta certa!',nome_capital)

while True:
    capital_brasil = input('Qual é a Capital do Brasil? ')
    if capital_brasil == 'Brasilia' or capital_brasil == 'Brasília:':
        break
    else:
        print('Resposta Errada!')
print('Resposta certa!')

n = int(input())
cont = 1
while cont <= 10:
    print(f'{cont} x {n} = {cont * n}')
    cont += 1