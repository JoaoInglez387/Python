num_01 = float(input('Digite o primeiro número: '))
num_02 = float(input('Digite o segundo número: '))
num_03 = float(input('Digite o terceiro número: '))
if num_01 <= num_02 and num_02 <=num_03:
    print(f'A ordem crescente é:\
        \n1° {num_01}\
        \n2° {num_02}\
        \n3° {num_03}')
elif num_01 <= num_03 and num_03 <=num_02:
    print(f'A ordem crescente é:\
        \n1° {num_01}\
        \n2° {num_02}\
        \n3° {num_03}')
elif num_02 <= num_03 and num_03 <=num_01:
    print(f'A ordem crescente é:\
        \n1° {num_01}\
        \n2° {num_02}\
        \n3° {num_03}')
elif num_03 <= num_02 and num_02 <=num_01:
    print(f'A ordem crescente é:\
        \n1° {num_01}\
        \n2° {num_02}\
        \n3° {num_03}')
elif num_02 <= num_01 and num_01 <=num_03:
    print(f'A ordem crescente é:\
        \n1° {num_01}\
        \n2 {num_02}\
        \n3° {num_03}')
elif num_03 <= num_02 and num_02 <=num_01:
    print(f'A ordem crescente é:\
        \n1° {num_01}\
        \n2° {num_02}\
        \n3° {num_03}')