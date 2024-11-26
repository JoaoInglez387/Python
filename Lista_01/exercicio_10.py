def recepecao():
    while True:
        tipo_moeda = input('Escolha qual tipo de moeda:\
            \n0 - Real (R$)\
            \n1 - Dolar (U$)\
            \n2 - Euro (€)\
            \n>>>> ')
        try:
            tipo_moeda = int(tipo_moeda)
        except:
            print('Não foi uma opção valida! Pois contém letra')
            print()
        else:
            break
            
    moeda = ['R$', 'U$', '€']
    
    if tipo_moeda == 0:
        while True:
            quantidade = input(f'Digite o valor que deseja: {moeda[0]}').replace(',', '.')
            
            try:
                quantidade = float(quantidade)
            except:
                print('Não foi uma opção valida! Pois contém letra')
                print()
            else:
                if quantidade < 0:
                    print('Não é possivel numero negativo!')
                    print()
                else:
                    break    
      
    elif tipo_moeda == 1:
        while True:
            quantidade = input(f'Digite o valor que deseja: {moeda[1]}')
            try:
                quantidade = float(quantidade)
            except:
                print('Não foi uma opção valida! Pois contém letra')
                print()
            else:
                if quantidade < 0:
                    print('Não é possivel numero negativo!')
                    print()
                else:
                    break
                  
    elif tipo_moeda == 2:
        while True:
            quantidade = input(f'Digite o valor que deseja: {moeda[2]}')
            try:
                quantidade = float(quantidade)
            except:
                print('Não foi uma opção valida! Pois contém letra')
                print()
            else:
                if quantidade < 0:
                    print('Não é possivel numero negativo!')
                    print()
                else:
                    break   
    else:
        print('Não foi uma opção valida!')

    return [moeda[tipo_moeda], quantidade]
    
def conversor(dados_moeda):
    tipo_class = ['BRL', 'USD', 'EUR', 'R$', 'U$', '€']
    
    while True:
        converter = input('Converter para qual tipo de moeda:\
            \n0 - USD\
            \n1 - EUR\
            \n2 - BRL\
            \n>>>> ') 
        try:
            converter = int(converter)
        except:
            print('Não foi uma opção valida! Pois contém letra')
            print()
        else:
            break
    

    if dados_moeda[0] == tipo_class[3]:
        if converter == 0:
            return f'Converte {tipo_class[0]} para {tipo_class[1]}:\
            \n{dados_moeda[0]}{dados_moeda[1]:.2f} = {tipo_class[4]}{dados_moeda[1] * 0.2025:.2f}'
            
        elif converter == 1:
            return f'Converte {tipo_class[0]} para {tipo_class[2]}:\
            \n{dados_moeda[0]}{dados_moeda[1]:.2f} = {tipo_class[5]}{dados_moeda[1] * 0.1867:.2f}'
        
        elif converter == 2:
            return f'Converte {tipo_class[0]} para {tipo_class[0]}\
            \n{dados_moeda[0]}{dados_moeda[1]:.2f} = {dados_moeda[0]}{dados_moeda[1]:.2f}'
        
        else:
            return 'Não é uma opção valida!'
        
        
    elif dados_moeda[0] == tipo_class[4]:
        if converter == 1:
            return f'Converte {tipo_class[1]} para {tipo_class[2]}:\
            \n{dados_moeda[0]}{dados_moeda[1]} = {tipo_class[5]}{dados_moeda[1] * 0.9220}'
            
        elif converter == 2:
            return f'Converte {tipo_class[1]} para {tipo_class[0]}:\
            \n{dados_moeda[0]}{dados_moeda[1]} = {tipo_class[3]}{dados_moeda[1] * 4.9392:.2f}'
            
        elif converter == 0:
            return f'Converte {tipo_class[0]} para {tipo_class[0]}\
            \n{dados_moeda[0]}{dados_moeda[1]} = {dados_moeda[0]}{dados_moeda[1]}'
        else:
            return 'Não é uma opção valida!'
        
        
    else:
        if converter == 0:
            return f'Converte {tipo_class[3]} para {tipo_class[1]}:\
            \n{dados_moeda[0]}{dados_moeda[1]} = {tipo_class[4]}{dados_moeda[1] * 1.0847:.2f}'
            
        elif converter == 2:
            return f'Converte {tipo_class[3]} para {tipo_class[0]}:\
            \n{dados_moeda[0]}{dados_moeda[1]} = {tipo_class[3]}{dados_moeda[1] * 5.3565:.2f}'
            
        elif converter == 1:
            return f'Converte {tipo_class[1]} para {tipo_class[1]}\
            \n{dados_moeda[0]}{dados_moeda[1]} = {dados_moeda[0]}{dados_moeda[1]}'
        else:
            return 'Não é uma opção valida!'
        
        
while True:
    print(conversor(recepecao()))
    print()
    retornar = input('Deseja continuar a conversão:\
         \n S \ N \
        \n>>>> ').upper()
    
    if retornar[0] != 'S':
        break