num = int(input('Digite um numero: '))
cont = 1
res = 1
if num == 1 or num == 0:
    print('1')
elif num > 1:
    while cont <= num:
        res = res * cont
        print(f'cont{cont}')
        print (f'res{res}')
        cont += 1
else:
    print('Impossivel de calcular')