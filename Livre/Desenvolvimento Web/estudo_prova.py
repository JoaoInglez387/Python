def ler_valores():
    while True:
        try:
            preço_base_prod = float(input('Digite o preço do produto: '))
            desconto = int(input('Parabéns!!! Você ganhou dois descontos, um de 10%, e outro de 15%. Qual vai querer usar agora? OBS(digite só o número, já a porcentagem não precisa): '))
            if desconto == 10 or desconto == 15:
                break
        except:
            print('Ocorreu algum erro, digite os dados novamente.')
    return preço_base_prod, desconto

def calcular_preço_final(dados):
    c = dados[0] - (dados[0] * dados[1]/100)
    return f'{c:.2f}'

while True:
    print(calcular_preço_final(ler_valores()))
    continuar = input('Deseja continuar: ').upper()
    if continuar == 'S':
        continue
    else:
        break
    
#----------------------------------------------------------------------------------
def ler_valor():
    while True:
        try:
            preco_do_produto = float(input('Digite o preço do produto: '))
            desconto = int(input('Parabéns!! Você ganhou dois tipos de desconto, um de 10%, e outra de 15%.\
            \nQual vai querer usar agora: '))
            if desconto == 10 or 15:
                break
        except:
            print('Ocorreu um erro, digite novamnete os dados.')
            continue
        
    return preco_do_produto, desconto

def calcular_preco(dados):
    c = dados[0] - (dados[0] * dados[1]/100)
    return f'{c:.2f}'

while True:
    print(calcular_preco(ler_valor()))
    
    pergunta = input('Deseja continuar?\
        \nS / N\
            \n>>> ').upper()
    
    if pergunta == 'S':
        continue
    else:
        break