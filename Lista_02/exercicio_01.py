def main():
    try:
        resultado = numero + 10
    except NameError:
        print('Ocorreu um erro na aplicação referente ao nome da variavel')
        print()
        
        while True:
            resultado = input('Digite um numero: ')
            try:
                resultado = float(resultado)
                resultado = resultado + 10
            except:
                print('Valor digitado contem letra! Digite novamente')
                print()          
            else:
                print(resultado)
                print()
                break
    except:
        print('Ocorreu um algum erro')
    else:
        print(resultado)
    finally:
        print('Aplicação finalizada')
    
main()

#------------------------------------------------------------------------------------------
def main():
    try:
        resultado = numero + 10
    except NameError:
        print('Ocorreu um erro na aplicação referente ao nome da variavel')
        print()
    except:
        print('Ocorreu um algum erro')
    else:
        print(resultado)
    finally:
        print('Aplicação finalizada')
    
main()