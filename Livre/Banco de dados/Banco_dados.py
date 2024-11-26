# CRUD
# create
# read
# update
# delete

import mysql.connector

conexao = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='Suportedado69',
    database='bdyoutube',
)

# CRUD
def CREATE():
    cursor = conexao.cursor()
    nome_produto = "chocolate"
    valor = 15
    comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'

    cursor.execute(comando)
    conexao.commit()  # editar o banco de dados
    
def READ():
    cursor = conexao.cursor()
    comando = f'SELECT * FROM vendas'
    cursor.execute(comando)
    
    resultado = cursor.fetchall() 

    cursor.close()
    conexao.close()
    
    return resultado

def UPDATE():
    cursor = conexao.cursor()
    
    valor =  6
    nome_produto = "todynho"
    
    comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
    
    cursor.execute(comando)
    conexao.commit()

    cursor.close()
    conexao.close()
    
def DELETE():
    cursor = conexao.cursor()
    
    valor =  6
    nome_produto = "todynho"
    
    comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
    
    cursor.execute(comando)
    conexao.commit()

    cursor.close()
    conexao.close()
    