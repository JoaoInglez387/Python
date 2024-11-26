valor_a = 0
valor_b = 0
valor_c = 0

def recepcao():
    global valor_a, valor_b, valor_c
    while True:
        valor_a = input('Digite a medida de a: ')
        valor_b = input('Digite a medida de b: ')
        valor_c = input('Digite a medida de c: ')

        try:
            valor_a = float(valor_a)
            valor_b = float(valor_b)
            valor_c = float(valor_c)
            if (valor_a and valor_b and valor_c)>0:
                break
            else:
                print('Um ou mais valores digitados são menores do que zero')
        except:
            print('Valor digitado contem letra!')   

def verifica_valor():
    if valor_a + valor_b > valor_c and valor_a + valor_c > valor_b and valor_b + valor_c > valor_a:
        return True
    else:
        return False

def tipo_triangulo():
    if valor_a  == valor_b == valor_c:
        return 'Seu Triângulo é um Triângulo Equilátero'
    elif valor_a == valor_b or valor_a == valor_c or valor_c == valor_b:
        return 'Seu Triângulo é um Triângulo Isósceles'
    else:
        return 'Seu Triângulo é um Triângulo Escaleno'
    
recepcao()
if verifica_valor():
    print(tipo_triangulo())
else:
    print('Os valores informados não representam as medidas de um triângulo')