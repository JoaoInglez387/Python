nm_usuario = input('Digite seu id: ')
senha_usuario = input('Digite sua senha: ')
if nm_usuario == 'aluno' and senha_usuario == 'ifro':
    print('Usuário autenticado com sucesso!')
else:
    print('Falha na autenticação!')