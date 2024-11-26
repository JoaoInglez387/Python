cont = 0
soma = 0

while True:
    num = int(input('Digite seu numero: '))
    impar = num % 2==1
    
    if impar:
        cont += 1
        soma += num
        print(f'Seu numero é impar: {num}')
        continue

    else:
        print(f'O total de numeros impar lidos foi: {cont}')
        if soma == 0:
            media = 0
        else:
            media = soma / cont
        print(f'A media dos numeros digitado foi: {media}')
        break