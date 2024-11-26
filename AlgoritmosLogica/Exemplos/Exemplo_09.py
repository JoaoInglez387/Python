#Lista Range

inicio = 1
saida = 11
res = range(inicio, saida)
#-----------------------------

print(list(range(1,11)))
print(list(range(1,11,2)))

#-----------------------------
#Loop For

for i in range(5):
    print(i)

for i in range(1,5):
    print(i)

for i in range(1,5,1):
    print(i)

#-----------------------------------
lista = [0,1,2,3,4]
for cont in lista:
    print(cont)
    print('repetiu')

for cont in range(5):
    print(cont)
    print(f'Repetiu a {(cont+1)}ª vez')

#-------------------------------------------------
while True:
    num = int(input('Digite um número maior que 1 e positivo: '))

    if num > 1:
        break
cont = 1
for i in range(1,(num+1)):
    print(i)

#--------------------------------------
print(list(range(1,num+1)))