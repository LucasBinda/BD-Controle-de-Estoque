import oracledb  # ou import cx_Oracle como alternativa

# Cria conexão
conn = oracledb.connect(
    user="SYSTEM",           # user you want to use
    password="lab@Database", # user password
    dsn="localhost:1522/XE"  #
)

# Cria cursor para executar queries
cur = conn.cursor()

# Teste: listar tabelas do usuário
cur.execute("SELECT table_name FROM user_tables")
for row in cur.fetchall():
    print(row)

# Fechar cursor e conexão
cur.close()
conn.close()
