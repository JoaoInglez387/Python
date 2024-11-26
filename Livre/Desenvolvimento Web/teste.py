def recepeção():
    print('Bem vindo ao Gerenciador de Tarefas')

    while True:
        usario_tarefa = input('O que vc gostaria de fazer no Gereciador de Tarefa:\
                            \n1 - Adicionar uma Tarefa (1)\
                            \n2 - Ver a lista de Tarefa (2)\
                            \n3 - Marca como concluida tarefa (3)\
                            \n4 - Fechar o Gerenciador (4)\
                            \n>>>>> ')

        try:
            usario_tarefa = int(usario_tarefa)
        except:
            print('Erro!!\nA variavel contém letra ou simbolo. Digite um valor valido!')
        else:
            if usario_tarefa not in (1, 2, 3, 4):
                print('Erro! Opção não valida digite uma opção valida')
            else:
                break


print(recepeção())
