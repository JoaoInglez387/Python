cont = 1

while True:
    num = int(input('Digite um número maior que 1 e positivo: '))

    if num < 2:
        print('Número menor que 1, digite novamente!')
        continue
    break
while True:
    print(cont)
    if num <= cont:
        break      
    cont += 1

#-------------------------------------------------------------------

while True:
    num = int(input('Digite um número maior que 1 e positivo: '))

    if num > 1:
        break
cont = 1
while cont <= num:
    print(cont)
    cont += 1

#------------------------------------------------------------------
while True:
    num = int(input('Digite um número maior que 1 e positivo: '))

    if num > 1:
        break
cont = 1
for i in range(1,(num+1)):
    print(i)