idade = int(input('Digite sua idade: '))
titulo = input('Você possui titulo: ')
if (idade == 16 or idade == 17 or idade > 70) and titulo =='sim':
    print('Seu voto é facultativo, mas sua participação é importante')
elif idade > 18 and idade < 70 and titulo =='sim':
    print('Seu voto é obrigatório, participe')
elif (idade < 16 or idade > 70) and titulo =='não':
    print('Você não pode votar')
elif idade > 18 and idade < 70 and titulo == 'não':
    print(f'Regularize a situação cadastral do seu título o mais rápido possível')