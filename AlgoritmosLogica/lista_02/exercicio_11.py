num_01 = float(input('Digite seu primeiro número: '))
num_02 = float(input('Digite seu segundo número: '))
num_03 = float(input('Digite seu terceiro número: '))
num_04 = float(input('Digite seu quarta número: '))
if num_01 >= num_02 and num_01 >= num_03 and num_01 >= num_04:
    print(f'O maior número é: {num_01}')
elif num_02 >= num_03 and num_02 >= num_04:
    print(f'O maior número é: {num_02}')
elif num_03 >= num_04:
    print(f'O maior número é: {num_03}')
else:
    print(f'O maior número é: {num_04}')