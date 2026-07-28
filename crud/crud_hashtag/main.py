import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

conexao = mysql.connector.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_NAME'),
)

cursor = conexao.cursor()

# CRUD

# nome_produto = "toddynho"
# valor = 3

# comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
# cursor.execute(comando)
# conexao.commit()

# READ

# comando = 'SELECT * FROM vendas'
# cursor.execute(comando)
# resultado = cursor.fetchall()
# print(resultado)

# UPDATE

# nome_produto = "toddynho"
# valor = 5

# comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
# cursor.execute(comando)
# conexao.commit()

# DELETE

# nome_produto = "toddynho"

# comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
# cursor.execute(comando)
# conexao.commit()

cursor.close()
conexao.close()
