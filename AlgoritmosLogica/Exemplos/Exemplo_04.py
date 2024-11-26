nota = int(input('Digite um numero: '))
while (nota < 0 or nota > 100):
    print('Nota inválida!')
    nota = int(input('Digite uma nota entre zero e cem: '))
print('Nota aceita. A aplicação será finalizado!')

num = 1
while num >= 1:
    print(num)
    num += 1

num = 1
while True:
    print(num)

num = 0
while num <= 10:
    print(num)
    num += 1
    if num == 5:
        continue
    print(num)