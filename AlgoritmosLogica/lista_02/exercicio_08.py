compra = float(input('Digite quantos custou a compra: '))
pagamento = input('Qual a forma de pagamento: ')
if pagamento =='a vista':
    print(f'O valor da compra foi de R$ {compra:.2f} terá um desconto de com total R${compra*(100-5)/100:.2f}')
elif pagamento == 'parcelado em 3X':
    print(f'O valor da compra foi de R$ {compra:.2f} séra parcelado 3X com total de R$ {compra:.2f}')
elif pagamento == 'parcelado em 5X':
    print(f'O valor da compra foi de R$ {compra:.2f} será parcelado em 5X terá um acréscimo de R$ {compra*(100+2)/100:.2f}')
elif pagamento == 'parcelado em 10X':
    print(f'O valor da compra foi de R$ {compra:.2f} será parcelado em 10X terá um acréscimo de R$ {compra*(100+8)/100:.2f}')