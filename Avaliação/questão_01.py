cont = 0
aprova = 0
reprova = 0
media = 0

aluno = int(input('Digite o numero de alunos: '))

while True:
    nota = int(input('Digite sua nota: '))
    media += nota

    if nota >= 60:
        print('Aluno  foi Aprovado!')
        cont += 1
        aprova += 1
    else:
        print('Aluno foi Reprovado!')
        cont += 1
        reprova += 1

    if cont == aluno:
        print(f'Foram aprovados {aprova} alunos\nE {reprova} alunos reprovados\
        \nTendo a média geral da turma de {media/aluno:.0f}')
        break
    else:
        continue