def numeros_pares(*num):
    cont = 0
    
    for i in num:
        if i % 2 == 0:
            cont += 1
        
    return f'Foram digitados {cont} numeros pares'

print(numeros_pares(int(input('Digite um numero: ')), int(input('Digite o segundo numero: '))))

#------------------------------------------------------------

def numero_pares(*num):
    cont = 0
    
    for i in num:
        if i % 2 == 0:
            cont += 1
        
    return f'Foram digitados {cont} numeros pares'

print(numero_pares(1,2,3,4,5,6))