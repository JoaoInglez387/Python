# Nomes: João Gabriel Soares Inglez / Marcos Vinícius Siqueira Lopes Cassimiro
# Turma: 1° A Informática
# Titulo: Software de pagamento de prestações

def recepecao():
    while True:
        vlr_prestacao = input('Digite o valor da prestação:\n>>>> R$').replace(',','.')
        try:
            vlr_prestacao = float(vlr_prestacao)
        except:
            print('Erro! A variavel contém letra ou simbolo.\
                \nDigite novamente!')
            continue
        else:
            if vlr_prestacao > 0:
                break
            else:
                print('Erro! O numero digitado não pode ser menor que zero\
                    \nDigite valores numéricos superiores a 0')
                continue
        
    while True:
        nr_dias_atraso = input('Digite o numero de dias de atraso:\n>>>> ')
        try:
            nr_dias_atraso = int(nr_dias_atraso)
        except:
            print('Erro! O valor contém letra simbolo.\nDigite novamente!')
            continue
        else:
            if nr_dias_atraso >= 0:
                break
            else:
                print('Erro! O valor não pode ser negativo.\
                    \nDigite numero inteiro superiro ou igual a zero')
                continue

    return vlr_prestacao, nr_dias_atraso 

def calculo_prestacao(dados):
    if dados[1] == 0:
        vlr_a_pagar = dados[0]
        return f'O valor a ser pago é de R${vlr_a_pagar:.2f}'
    else:
        vlr_a_pagar = dados[0] + ((5 + dados[1])/100 * dados[0])
        return f'O valor da prestacao é de R${vlr_a_pagar:.2f}'

    
while True:
    print(calculo_prestacao(recepecao()))
    
    pergunta = input('Você deseja continuar a operação?\
            \nSim / Não\
                \n>>>> ').upper()
    
    if pergunta == 'SIM':
        continue
    else:
        print('Fim do Programa!')
        break