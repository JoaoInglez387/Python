com_produto = [[], [], []]

for i in range(5):
    produto = input('Digite um nome de produto: ')
    quantia = int(input('Digite a quantidade: '))
    preço = float(input('Digite o preço do produto: R$'))

    com_produto[0].append(produto)
    com_produto[1].append(preço)
    com_produto[2].append(quantia)
   
total = 0 
for n in range(5):
    total += print(com_produto[1][n] * com_produto[2][n])
    print(com_produto[1][n] * com_produto[2][n])

print(f'O total geral do preço dos produtos é de R${total}')   


#------------------------------------------------------------

com_produto = [[], [], []]

for i in range(5):
    com_produto[0].append(input('Digite um nome de produto: '))
    com_produto[1].append(float(input('Digite o preço do produto: R$')))
    com_produto[2].append(int(input('Digite a quantidade: ')))
   
total = 0 
for n in range(5):
    total += print(com_produto[1][n] * com_produto[2][n])
    print(com_produto[1][n] * com_produto[2][n])

print(f'\nO total geral do preço dos produtos é de R${total}')  