import webbrowser as web
import random as rand

print('------------------')
print('    MEUS SITES !  ')
print('------------------')

#-----------------------------------------------------------------------------------------------

def randomica():
    ran = rand.randint(1, 4)
    if ran == 1:
        web.open('https://www.google.com.br/')
    elif ran == 2:
         web.open('https://www.youtube.com/')
    elif ran == 3:
        web.open('https://discord.com/channels/852739617287176234/852739617287176241')
    elif ran == 4:
        web.open('https://web.whatsapp.com/')

#-------------------------------------------------------------------------------------------------

def main():
    while True:
        print(f'Digite uma das opções de sites que você gostaria de acessar:\
        \nGoogle (1)\
        \nYoutube (2)\
        \nDiscord (3)\
        \nZap (4)\
        \nEscolher site aleatorio (5)\
        \nSair (6)')
        x = int(input('>>>> '))

#-----------------------------------------------------------------------------------------------   
    
        if x == 1:
            web.open('https://www.google.com.br/')
            conti = input(f'Deseja continuar?\nS / N \n>>>> ')
            if conti.upper() == 'S':
                print()
                continue
            else:
                break

#----------------------------------------------------------------------------------------------- 

        elif x == 2:
            web.open('https://www.youtube.com/')
            conti = input(f'Deseja continuar?\nS / N \n>>>> ')
            if conti.upper() == 'S':
                print()
                continue
            else:
                break

#----------------------------------------------------------------------------------------------- 

        elif x == 3:
            web.open('https://discord.com/channels/852739617287176234/852739617287176241')
            conti = input(f'Deseja continuar?\nS / N \n>>>> ')
            if conti.upper() == 'S':
                print()
                continue
            else:
                break

#----------------------------------------------------------------------------------------------- 

        elif x == 4:
            web.open('https://web.whatsapp.com/')
            conti = input(f'Deseja continuar?\nS / N \n>>>> ')
            if conti.upper() == 'S':
                print()
                continue
            else:
                break
    
#----------------------------------------------------------------------------------------------- 

        elif x == 5:
            randomica()
            print()

#----------------------------------------------------------------------------------------------- 

        elif x == 6:
            sair = input(f'Tem certeza que quer sair!\nS / N \n>>>> ')
            if sair.upper() == 'S':
                break
            elif sair.upper() == 'N':
                print()
                continue
            else:
                print('Opção invalida, por favor digite uma opção valida!')
                print()
                continue

#----------------------------------------------------------------------------------------------- 

        else:
            print('Opção invalida, por favor digite uma opção valida!')
            print()
main()