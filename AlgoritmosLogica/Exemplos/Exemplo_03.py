media = int(input('Digite sua média: '))
if media >= 60:
    print('Estou aprovado!')
    print('Parabéns')
    if media > 90:
        print('Você é fenomenal!')
elif media >= 17:
    print('Estou no Exame Final!')
else:
    print('Se lascou!')
print('Fim do programa!')