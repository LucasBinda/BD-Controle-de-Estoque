from Python.connection.database import DatabaseConnection
import os

class createTables :

    def create_tables(self):
        """
        executa o script SQL para criar as tabelas
        """
        try:
            # caminho para o arquivo SQL
            sql_path = "sql/create_tables.sql"

            # verifica se o arquivo existe
            if not os.path.exists(sql_path):
                print(f"Erro: Arquivo {sql_path} não encontrado!")
                return False

            # le o conteúdo do arquivo
            with open(sql_path, 'r', encoding='utf-8') as f:
                query_create = f.read()

            db = DatabaseConnection()
            db.conectar()

            # divide os comandos por ;
            commands = [cmd.strip() for cmd in query_create.split(';') if cmd.strip()]


            # executa cada comando DDL
            for i, command in enumerate(commands, 1):
                if command:  # Ignora strings vazias
                    print(f"Executando comando {i}: {command[:50]}...")
                    try:
                        db.executarDDL(command)
                        print(f"✓ Comando {i} executado com sucesso")
                    except Exception as e:
                        print(f"✗ Erro no comando {i}: {e}")

            print("Tabelas criadas com sucesso!")
            return True

        except Exception as e:
            print(f"Erro durante criação das tabelas: {e}")
            return False

    def insert_initial_data(self):
        """
        executa o script SQL para inserir dados iniciais
        """
        try:
            # caminho para o arquivo SQL
            sql_path = "sql/inserir_dados_iniciais.sql"

            # verifica se o arquivo existe
            if not os.path.exists(sql_path):
                print(f"Erro: Arquivo {sql_path} não encontrado!")
                return False

            # le o conteúdo do arquivo
            with open(sql_path, 'r', encoding='utf-8') as f:
                query_insert = f.read()


            db = DatabaseConnection()
            db.conectar()

            # divide os comandos por ponto e vírgula
            commands = [cmd.strip() for cmd in query_insert.split(';') if cmd.strip()]

            print("Inserindo dados iniciais...")

            # executa cada comando DML
            for i, command in enumerate(commands, 1):
                if command and command.upper() != 'COMMIT':  # Ignora strings vazias e COMMIT
                    print(f"Inserindo dados {i}: {command[:50]}...")
                    try:
                        db.executarDML(command)
                        print(f"✓ Dados {i} inseridos com sucesso")
                    except Exception as e:
                        print(f"✗ Erro ao inserir dados {i}: {e}")

            # faz commit final de tudo
            db.executarDML("COMMIT")
            print("Dados iniciais inseridos com sucesso!")
            return True

        except Exception as e:
            print(f"Erro durante inserção de dados: {e}")
            return False

    def run(self): # função principal que executa todo o processo
        print("INICIANDO CRIAÇÃO DO BANCO DE DADOS")

        # cria as tabelas
        if not self.create_tables():
            print("Falha na criação das tabelas. Abortando...")
            return

        # insere dados iniciais
        if not self.insert_initial_data():
            print("Falha na inserção de dados iniciais.")
            return

        print("BANCO DE DADOS CONFIGURADO COM SUCESSO")