# no terminal coloca pip install mysql-connector-python

import mysql.connector

conexao = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='12345',
    database='teste_01',
)
cursor = conexao.cursor()

def cread():
    conexao = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='12345',
        database='teste_01',
    )
    cursor = conexao.cursor()

    nome_da_tarefa = input('Digite sua terefa:')

    data = input('Digte que horas sera realizada: ')

    comando = f'INSERT INTO teste_agenda1 (nome_da_tarefa, data) VALUES ("{nome_da_tarefa}", "{data}")'

    cursor.execute(comando)

    conexao.commit()

    cursor.close()
    conexao.close()
    return'Alterações feita com sucesso'

def read():
    conexao = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='12345',
        database='teste_01',
    )
    cursor = conexao.cursor()

    comando = f'SELECT * FROM teste_agenda1'

    cursor.execute(comando)

    resultado = cursor.fetchall()
    resultado=str(resultado)
    resultado=resultado.replace('(', '\n')
    resultado=resultado.replace(')', '')
    resultado=resultado.replace("'",'')
    resultado=resultado.replace('[','')
    resultado=resultado.replace(']','')
    cursor.close()
    conexao.close()
    return resultado

def updata():
    conexao = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='12345',
        database='teste_01',
    )
    cursor = conexao.cursor()
    idteste_agenda1 = int(input('\nQual é o número da atividade que deseja modificar?'))
    try:
        nome_da_tarefa = input('\nAdicione a mudança na descrição de sua tarefa, caso não queira fazer nenhuma aperte enter')

        data = input('\nFaça sua modificação na hora de realização de suaq atividade, caso não quewira aperte enter.')
        if data != '':
            comando = f'UPDATE teste_agenda1 SET data = "{data}" WHERE idteste_agenda1 = "{idteste_agenda1}"'
            cursor.execute(comando)
        if nome_da_tarefa != '':
            comando=f'UPDATE teste_agenda1 SET nome_da_tarefa = "{nome_da_tarefa}" WHERE idteste_agenda1 = "{idteste_agenda1}"'
            cursor.execute(comando)
        conexao.commit()
        cursor.close()
        conexao.close()
        return'Alterações feita com sucesso'
    
    except:
        return'Nenhuma alteração foi feita'
    


def delete():
    conexao = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='12345',
        database='teste_01',
    )
    cursor = conexao.cursor()

    idteste_agenda1 = int(input('\nDigite o numero da tarefa: '))

    comando = f'DELETE FROM teste_agenda1 WHERE idteste_agenda1= "{idteste_agenda1}"'

    cursor.execute(comando)

    conexao.commit() 

    cursor.close()
    conexao.close()
    return'Alterações feita com sucesso'


while True:
    print('Qual função deseja fazer?\n1 = Adicionar tarefa\n2 = mostrar atividades\n3 = retirar atividades\n4 = Atualizar tarefa\n')
    per=input('Qual função deseja fazer?')
    if per=='1':
        print(cread())
    elif per == '2':
        print(read())
    elif per == '3':
        print(delete())
    elif per == '4':
        print(updata())
