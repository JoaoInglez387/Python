def somar_numeros(n1, n2):
    soma = n1 + n2
    print(f'{n1} + {n2} = {soma}')

print('Fique Atento!')
somar_numeros(1,3)
somar_numeros(10,50)

print()
#------------------------------------------------------------

def somar_numeros(n1, n2):
    soma = n1 + n2
    return soma

print('Fique Atento!')
s1 = somar_numeros(1,3)
s2 = somar_numeros(10,50)
print(s1, s2)

print()
#-------------------------------------------------------------

def somar_numeros(n1, n2):
    soma = n1 + n2
    print(type(soma))
    return f'\nSoma: {soma}'

print('Fique Atento!')
s1 = somar_numeros('a','b')
s2 = somar_numeros(10,50)
print(s1, s2)

print()
#------------------------------------------------------------

def somar_numeros(n1, n2):
    soma = n1 + n2
    return soma

print('Fique Atento!')
v1 = int(input('Digite um numero: '))
v2 = int(input('Digte um numero: '))
#print(somar_numeros(int(v1),int(v2)))
print(somar_numeros(v1,v2))

print()
#---------------------------------------------

def somar_numeros(n1, n2):
    global soma
    soma = n1 + n2
    print(f'Soma: {soma}')

soma = 10
print('Fique Atento!')
print(soma)
somar_numeros(1,3)

print()