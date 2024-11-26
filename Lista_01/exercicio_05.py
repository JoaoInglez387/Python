def numeros_positivo(*num):
    cont = 0
    
    for i in num:
        if i > 0:
            cont += 1
        
    return f'Foram digitados {cont} numeros positivos'

print(numeros_positivo(int(input('Digite um numero: ')), int(input('Digite o segundo numero: '))))

#-------------------------------------------------------------

def numero_positivo(*num):
    cont = 0
    
    for i in num:
        if i > 0:
            cont += 1
        
    return f'Foram digitados {cont} numeros positivos'

print(numero_positivo(-2,-1,0,1,2,3,4))