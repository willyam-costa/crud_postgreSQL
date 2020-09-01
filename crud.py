# Importa o driver Python para PostgreSQL
import psycopg2

# cria a conexão com as credenciais do banco de dados do postgres
try:
    connection = psycopg2.connect(
        user="postgres",
        password="sua senha", #bote a senha do seu usuario do PostgreSQL
        host="localhost",
        port="5432", #essa é a porta padrão do postgres
        database="nome da sua tabela" #coloque o nome da sua tabela
    )

    # Crie um objeto de conexão do cursor para uma instância PostgreSQL e imprima as propriedades da conexão.
    cursor = connection.cursor()
    print(connection.get_dsn_parameters(), "\n")

    # Exibe o cursor instalado da versão PostgreSQL
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("Você está conectado ao - ", record, "\n")

#Lidar com o erro gerado pelo comando que é útil ao usar Python ao trabalhar com PostgreSQL 
except(Exception, psycopg2.Error) as error:
    print("Erro ao conectar ao banco de dados PostgreSQL", error)
    connection = None

# fecha a conexão com o banco
finally:
    if connection != None:
        cursor.close()
        connection.close()
        print("A conexão com o PostgreSQL foi encerrada.")