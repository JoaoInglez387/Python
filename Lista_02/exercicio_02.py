def divisão(a, b):
    try:
        resultado = a / b
    except TypeError:
        print('O valor ele não é numero!')
        print()
        
        while True:
            resultado = input('Digite um numero: ')
            try:
                resultado = float(resultado)
                resultado = a / resultado
            except:
                print('Erro! valor com tem letra! Digite novamente')
            else:
                return resultado
                break 
    else:
        return resultado

print(divisão(10, 2))
print(divisão(10, '2'))