cont = 0
n_multiplo = 0

for i in range(10):
    num = int(input('Digite um número: '))
    if num % 5 == 0:
        print('Esse número é múltiplo de 5')
        cont += 1
    else:
        print('Esse número não é múltiplo de 5')
        n_multiplo += 1
        
print(f'Foram digitados {cont} números que são múltiplos de 5!\
    \nE {n_multiplo} números que não são múltiplo de 5!')