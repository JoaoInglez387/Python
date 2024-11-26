def main():
    print('Vamos dividir!')
    while True:
        x = input('Digite o primero valor: ')
        try:  
            x = int(x)
        except:
            print('Erro! o variavel contem letra!\nDigite novamente')
            continue
        else:
            if x == 0:
                print('Erro! não é possivel dividir por zero\nDigite novamente!')
                continue
            else:
                break
        
    while True:
        y = input('Digite o segundo valor: ')
        try:
            y = int(y)
        except:
            print('Erro! o variavel contem letra!\nDigite novamente')
            continue
        else:
            if y == 0:
                print('Erro! não é possivel dividir por zero\nDigite novamente!')
                continue
            else:
                break
        
        
    r = x/y
    print(f'O resultado da divisão é {r}')
    
main()

#--------------------------------------------------------------------------------

def main():
    print('Vamos dividir!')
    while True:
        x = input('Digite o primero valor: ')
        y = input('Digite o segundo valor: ')
        
        try:
            x = int(x)
            y = int(y)
            
        except:
            print('Erro! o variavel contem letra e simbolo!\nDigite novamente')
            continue
        else:
            if x == 0 or y == 0:
                print('Erro! não é possivel dividir por zero\nDigite novamente!')
                continue
            else:
                break
        
    r = x/y
    
    print(f'O resultado da divisão é {r}')
    
main()

#-----------------------------------------------------------------------------------------

def main():
    print('Vamos dividir!')
    
    while True:
        x = input('Digite o primero valor: ')
        try:  
            x = int(x)
        except ValueError:
            print('Erro! o variavel contem letra!\nDigite novamente')
            continue
        except ZeroDivisionError:
            print('Erro! não é possivel dividir por zero\nDigite novamente!')
            continue
        else:
            break
        
    while True:
        y = input('Digite o segundo valor: ')
        try:
            y = int(y)
        except ValueError:
            print('Erro! o variavel contem letra!\nDigite novamente')
            continue
        except ZeroDivisionError:
            print('Erro! não é possivel dividir por zero\nDigite novamente!')
            continue
        else:
            break
        
    r = x/y
    
    print(f'O resultado da divisão é {r}')
    
main()
