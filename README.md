<h1 align="center"> Controle de Estoque </h1>

Programa de Controle de estoque usando banco de dados Oracle com SQL e manipulação de Banco de dados com Python

![](https://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge)

## Pre-requisitos
- Python
- Oracle Database
## Instalação bibliotecas Python
Abra o terminal e acesse o diretorio do programa.

[BD-Controle-de-Estoque]()

instale as  bibliotecas necessarias com o comando:
```
pip install -r requirements.txt
```
## Como executar o programa:



Você pode testar a conexão entre o programa e o Banco de Dados executando o arquivo test_connection.py pelo terminal exemplo abaixo:
```
python Python/test_connection.py
```
    
- depois da primeira execução do programa pelo teste ou pelo metodo principal, ele vai dar um "erro" e notificar da criação do arquivo de conexão com o banco de dados.


ele vai pedir para você colocar as credenciais do seu banco de dados em [config](Python/connection/config/config.json):
```
Python/connection/config/config.json
```

- Lembre-se de dar
```

```


Execute o programa pelo terminal de comandos com:
```
python Python/Main.py
```

[Main](Python) localização do arquivo principal do aplicativo.


## Explicação da organização do Projeto:

Pasta Diagrams é a pasta com toda documentação dos diagramas sql

Pasta Python contem o programa funcional escrito em python.