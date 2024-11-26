cont = 0

while True:
    num = int(input('Digite um numero: '))

    if num <= 0:
        print('Fim do codigo!')
        break

    if num >= 100 and num <= 200:
        cont += 1
        continue

print(f'Foram digitado {cont}!')