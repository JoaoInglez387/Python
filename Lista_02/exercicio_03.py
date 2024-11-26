def main():
    print('Incio do main')
    funcao_01()
    print('Fim do main')
    
def funcao_01():
    print('Incio da função 01')
    funcao_02()
    print('Fim da função 01')
    
def funcao_02():
    print('Incio da função 02')

    try:
        lista = range(10)
        for i in range(11):
            print(lista[i])
        
    except IndexError:
        print('Erro! A indice inserido inexistente')
        
    else:
        print('Fim da função 02')
    
main()

#-------------------------------------------------------------------------

def main():
    print('Incio do main')
    funcao_01()
    print('Fim do main')
    
def funcao_01():
    print('Incio da função 01')
    funcao_02()
    print('Fim da função 01')
    
def funcao_02():
    print('Incio da função 02')
    lista = range(10)
    for i in range(11):
        try:
            print(lista[i])
                
        except IndexError:
            print('Erro! A indice inserido ele não esta disponivel')
            
    print('Fim da função 02')
    
main()