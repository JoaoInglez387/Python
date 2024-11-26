'''Codigo com correção e obs:'''

def calculo(num_1: float, num_2: float, operação: str):
    verfica_num = [str(num) for num in range(10)]
    
    for i in num_1:
        if verfica_num.count(i) == 0:
            return 'Numero Inválido!'

    for n in num_2:
        if verfica_num.count(n) == 0:#nesta linha você estava testando a variável "i"
            return 'Numero Inválido!'
    
    num_1 = float(num_1)
    num_2 = float(num_2)
    #a indentação das linhas abaixo estava errada    
    if operação.lower() == 'soma' or operação == '+': 
        return f'Calculo: {num_1} + {num_2} = {num_1+ num_2}'
    elif operação.lower() == 'subtração' or operação == '-':
        return f'Calculo: {num_1} - {num_2} = {num_1 - num_2}'
    elif operação.lower() == 'multiplicação' or operação == '*':
        return f'Calculo: {num_1} x {num_2} = {num_1 * num_2}'
    elif operação.lower() == 'divisão' or operação == '/':
        return f'Calculo: {num_1} / {num_2} = {num_1 / num_2}'
    
print(calculo(input('Digite seu primeiro numero: '), input('Digite seu segundo numero: '), input('Digite sua operação: ')))

#--------------------------------------------------------------------------------------------------------------------------------------
'''Codigo sem correção '''

def calculo(num_1: float, num_2: float, operação: str):
    verfica_num = [str(num) for num in range(10)]
    
    for i in num_1:
        if verfica_num.count(i) == 0:
            return 'Numero Inválido!'

    for n in num_2:
        if verfica_num.count(i) == 0:#nesta linha você estava testando a variável "i" o certo é "n"
            return 'Numero Inválido!'
    
        num_1 = float(num_1)
        num_2 = float(num_2)

    #a indentação das linhas abaixo estava errada
      
        if operação.lower() == 'soma' or operação == '+':
            return f'Calculo: {num_1} + {num_2} = {num_1+ num_2}'
        elif operação.lower() == 'subtração' or operação == '-':
            return f'Calculo: {num_1} - {num_2} = {num_1 - num_2}'
        elif operação.lower() == 'multiplicação' or operação == '*':
            return f'Calculo: {num_1} x {num_2} = {num_1 * num_2}'
        elif operação.lower() == 'divisão' or operação == '/':
            return f'Calculo: {num_1} / {num_2} = {num_1 / num_2}'
    
print(calculo(input('Digite seu primeiro numero: '), input('Digite seu segundo numero: '), input('Digite sua operação: ')))