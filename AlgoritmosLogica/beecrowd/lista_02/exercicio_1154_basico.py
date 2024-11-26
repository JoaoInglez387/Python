soma_idade = 0
quantidade_idade = 0

while True:
    idade = float(input())
    if idade <= 0:
        break

    soma_idade += idade
    quantidade_idade += 1

if quantidade_idade > 0:
    media = soma_idade / quantidade_idade
    print("{:.2f}".format(media))