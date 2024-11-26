cont = 0

while True:
    num = int(input('Digite seu numero: '))
    par = num % 2==0
    
    if num >= 0 and par:
        print(f'Seu numero é par: {num}')
        cont += 1
        continue
    
    else:
        print(f'Seu numero é impar: {num} ')
        print(f'O total de numeros positivos e pares lidos foi: {cont}')
        break