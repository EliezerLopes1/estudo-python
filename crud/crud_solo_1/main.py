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

# CREATE

nome_do_jogo = "League of Legends"
valor = 0

comando = f'INSERT INTO loja_gamer (nome_do_jogo, VALOR) VALUES ("{nome_do_jogo}", {valor})'
cursor.execute(comando)
conexao.commit()

# Read

comando = 'SELECT * FROM loja_gamer'
cursor.execute(comando)
resultado = cursor.fetchall()
print(resultado)

# Update

nome_do_jogo = "LOL"
valor = 100

comando = f'UPDATE loja_gamer SET nome_do_jogo = "{nome_do_jogo}" WHERE valor = {valor}'
cursor.execute(comando)
conexao.commit()

# # Delete

id = 1

comando = f'DELETE FROM loja_gamer WHERE ({id})'

cursor.execute(comando)
conexao.commit()

cursor.close()
conexao.close()