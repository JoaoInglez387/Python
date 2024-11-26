cont = 0

while True:
    num = int(input('Digite um numero: '))

    if num < 0:
        print('Numero negativo ou abaixo de 0!')
        continue

    print(num ** 0.5)
    cont += 1
    
    if cont == 10:
        break