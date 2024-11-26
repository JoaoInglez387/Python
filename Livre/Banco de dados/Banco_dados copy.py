#CRUD
#create
#read
#update
#delete

import mysql.connector

conexao = mysql.connector.connect(
    host ='127.0.0.1',
    user = 'root',
    password = 'Suportedado69',
    database = 'bdyoutube',
)

cursor = conexao.cursor()

#CRUD
comando = ''
cursor.execute(comando)
conexao.commit() # editar o banco de dados
resultado = cursor.fetchall() #ler o banco de dados

cursor.close()
conexao.close()


# CRUD
nome_produto = "chocolate"
valor = 15
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'

cursor.execute(comando)
conexao.commit()  # editar o banco de dados
# resultado = cursor.fetchall() #ler o banco de dados

cursor.close()
conexao.close()
