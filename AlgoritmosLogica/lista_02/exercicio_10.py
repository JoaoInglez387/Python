from math import sqrt
a = int(input('Digite o valor A: '))
b = int(input('Digite o valor B: '))
c = int(input('Digite o valor C: '))
delta = b*b - 4 * a* c
if delta == 0:
    x = (-1*b + sqrt(delta))/(2*a)
    print(f'A equação possui apenas uma raiz, tendo o resultado{x}')
elif delta > 0:
    x_1 = (-1*b + sqrt(delta))/(2*a)
    x_2 = (-1*b - sqrt(delta))/(2*a)
    print(f'A equação possui duas raizes, a primeira raiz é {x_1}\
        e a segunda raiz é {x_2}')
elif delta <= 0:
    print(f'Delta negativo {delta}. A equação não possui nenhuma raiz')