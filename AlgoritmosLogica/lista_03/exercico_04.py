while True:
    nome = input('Digite seu nome: ')
    senha = input('Digite sua senha: ')

    if nome == 'ALUNO' and senha == 'Lógic@2023':
        print('Usuário autenticado com sucesso!')
        break
    else:
         print('Nome do usuário ou Senha estão incorretos, Por favor digite novamente!')
         continue