import json
import oracledb
from pandas import DataFrame
from pathlib import Path
import pandas as pd
###############################################################
#
#
# Classe que conecta com o driver do banco de dados Oracle
# Documentação usada:
# https://python-oracledb.readthedocs.io/en/latest/user_guide/connection_handling.html
# https://python-oracledb.readthedocs.io/en/latest/user_guide/sql_execution.html
# https://python-oracledb.readthedocs.io/en/latest/user_guide/plsql_execution.html
#
###############################################################
class DatabaseConnection:
    def __init__(self, config_file='config/config.json'):
        self.config_file = config_file
        self.config = self._carregar_config()
        self._connection = None
        self._cur = None
        #configurando o pandas
        self.configurar_pandas()

    def configurar_pandas(self):
        pd.set_option('display.max_columns', None)          # Mostra TODAS as colunas
        pd.set_option('display.width', None)                # largura ilimitada
        pd.set_option('display.max_colwidth', None)         # larguma maxima das colunas
        pd.set_option('display.expand_frame_repr', False)   # não quebrar linhas

    def sqlToDataFrame(self, query:str) -> DataFrame: # retorna um modelo de dados da biblioteca Pandas
        self._cur.execute(query)
        rows = self._cur.fetchall()
        return DataFrame(rows, columns=[col[0].lower() for col in self._cur.description])


    def sqlToMatrix(self, query:str) -> tuple: # retorna o query em formado de matrix
        self._cur.execute(query)
        rows = self._cur.fetchall()
        matrix = [list(row) for row in rows]
        columns = [col[0].lower() for col in self._cur.description]
        return matrix, columns

    def executarDDL(self, query:str): # esse metodo executa uma query especifica que for passada, serve para (CREATE TABLE, DROP TABLE, ALTER TABLE)
        self._cur.execute(query)


    def executarDML(self, query): # esse metodo executa uma query especifica que for passada, serve para (INSERT, UPDATE, DELETE)
        self._cur.execute(query)
        self._connection.commit() # TO-DO perigoso para os recursos do sistema, remover e fazer manualmente


    def conectar(self):  # estabelece conexão com o banco de dados
        self._validar_config()
        db_config = self.config['database']
        try:
            self._connection = oracledb.connect(
                user=db_config['username'],
                password=db_config['password'],
                dsn=self._get_connection_string()
            )
            self._cur = self._connection.cursor()
            return self._cur
        except Exception as e:
            print(f"Erro ao conectar, cheque suas credenciais no arquivo config.json: {e}")
            return None


    def desconectar(self): # fecha a conexão com o banco
        if self._connection is not None:
            self._connection.close()
            self._connection = None
            self._cur = None



    def _carregar_config(self): # retorna os dados do arquivo config.json com as credenciais do banco de dados
        config_path = Path(__file__).parent / self.config_file

        if not config_path.exists():
            self._criar_config_template(config_path)
            raise FileNotFoundError(f"""
            Arquivo {self.config_file} não encontrado!
            gerando modelo padronizado;
            
            PASSO A PASSO de configuração:
            1. Edite 'Python/config/config.json' com suas credenciais reais
            2. Use SOMENTE service_name OU sid (deixe o outro como null) e não remova "" de onde elas 
            3. Apos configurar rode o programa novamente, para checar se está tudo correto
            """
            )

        with open(config_path, 'r', encoding='utf-8') as file:
            return json.load(file)


    def _criar_config_template(self,config_path): # Cria o template de conexão (pasta config e arquivo config.json)
        config_path.parent.mkdir(parents=True, exist_ok=True)
        modelo = {
            "database": {
                "username": "seu_usuario",
                "password": "sua_senha",
                "host": "localhost",
                "port": 1521,
                "service_name": "XE",
                "sid": None
            }
        }
        with open(config_path, 'w', encoding='utf-8') as file:  # cria e escreve o json
            json.dump(modelo, file, ensure_ascii=False, indent=4)


    def _validar_config(self): # validação se está preenchido a categoria 'service_name' OU 'sid'
        db_config = self.config['database']
        if not db_config.get('service_name') and not db_config.get('sid'):
            raise ValueError("""
            ERRO: Deve especificar service_name ou sid no arquivo de configuração. 
            service_name tem prioridade de uso se ambos estiverem preenchidos.
            
            Exemplo com service name:
            "service_name": "XE",
            "sid": null
            
            Exemplo com sid:
            "service_name": null,
            "sid": "XE"
            """)

    def _get_connection_string(self): # retorn dsn string
        self._validar_config()

        db_config = self.config['database']
        host = db_config['host']
        port = db_config['port']

        # Prioriza service_name sobre sid
        if db_config.get('service_name'):
            return f"{host}:{port}/{db_config['service_name']}"
        else:
            return f"{host}:{port}:{db_config['sid']}"