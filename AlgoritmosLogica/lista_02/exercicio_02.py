casqui = float(input('Número de casquinha: '))
if casqui > 12:
    print(f'Valor total: R${casqui*2.50:.2f}')
elif casqui > 0:
    print(f'Valor total: R${casqui*3.00:.2f}')
else:
    print('Não é possível comprar a quantidades negativas de casquinhas')