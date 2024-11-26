peso_peixe = float(input('Digite o peso dos peixe: '))
if peso_peixe > 50:
    excesso = peso_peixe - 50
    print(f'O peso total é {peso_peixe}kg\
        \nconteém excesso de peso de {excesso:.3f}kg\
        \no valor da multa será R$ {excesso*4:.2f}')
else:
    print(f'Está tudo ok o peso é de: {peso_peixe:.2f}kg não contém excesso')