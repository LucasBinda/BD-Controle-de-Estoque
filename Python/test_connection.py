from connection.database import DatabaseConnection

if __name__ == '__main__': # teste de conexão
    db = DatabaseConnection() # instancia a classe
    conexao = db.conectar()
    print("Conexão com o banco de dados Bem Sucedida!")
