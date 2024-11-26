def numero(num):
        if num > 0:
            return "P"
        elif num < 0:
            return 'N'
        else:
            return 'Z'
    
print(numero((int(input('Digite um numero: ')))))