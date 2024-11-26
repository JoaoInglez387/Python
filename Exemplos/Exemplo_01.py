def nome_pessoal(name):
    print(f'Bom dia, {name}!')
    
#nome_pessoal(input('Digite seu nome: '))

#-----------------------------------------

def nome_pessoal(name):
    print(f'Bom dia, {name}!')
    
#nome = input('Digite seu nome: ')
#nome_pessoal(nome)

#------------------------------------------

def recepção_usuario(name, turno):
    if turno == 'matutino': 
        print(f'Bom dia, {name}!')
    elif turno == 'vespertino':
        print(f'Boa tarde, {name}!')  
    elif turno == 'noturno':
        print(f'Boa noite, {name}!')
    else:
        print('Turno invalido, digite um turno valido!')

#recepção_usuario(input('Digite seu nome: '), input('Digite seu turno: '))

#-------------------------------------------------------------------------

def recepção_usuario(name: str = '', turno: str = ''):
    if turno.lower() == 'matutino':
        print(f'Bom dia, {name}!')
    elif turno.lower() == 'vespertino':
        print(f'Boa tarde, {name}!')  
    elif turno.lower() == 'noturno':
        print(f'Boa noite, {name}!')
    else:
        print('Turno invalido, digite um turno valido!')

#recepção_usuario(input('Digite seu nome: '), input('Digite seu turno: '))

#--------------------------------------------------------------------------------------------
def idade_usuario(idade):
    try:
        idade = int(idade)
    except:
        return('Idade invalida')
    
    if idade >= 18:
        return 'Maior de idade!'
    else:
        return 'Menor de idade!'

print(idade_usuario(input('Digite sua idade: ')))