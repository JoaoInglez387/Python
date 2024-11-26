def nome_completo(nome):
    conta_name = nome.split()[0]
    
    if conta_name.isalpha() == True:
        return f'Nome {conta_name} contem só letras'
    else:
        return 'Erro! Não está contido apenas por letras!'
    
print(nome_completo(input('Digite seu nome: ')))