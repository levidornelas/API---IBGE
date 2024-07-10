import psycopg2 

DATABASE = 'senac'
PORT = ''
USER = 'postgres'
PASSWORD = '' 
HOST = 'localhost'

def conect_to_database():
  try:
    conexao = psycopg2.connect(
                          database = DATABASE,
                          user = USER,
                          password = PASSWORD,
                          host = HOST,
                          port = PORT
    )

    connection = conexao.cursor()
    connection.execute('SELECT version();')
    db_versao = connection.fetchone()
    connection.close()
    conexao.close()

    return(f'Conectado ao PostgreSQL! versão: {db_versao}')
  
  except Exception as e:  
    return(f'Ocorreu um erro ao se conectar com o banco: {e}')

def register_users(cep, rua, bairro, cidade, estado):
    try:
        # Conexão ao banco de dados PostgreSQL
        connection = psycopg2.connect(
            database=DATABASE,
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT
        )
        cursor = connection.cursor()
        # Inserir os dados do endereço:
        inserir_sql = """INSERT INTO api (cep, rua, bairro, cidade, estado) VALUES ( %s, %s, %s, %s, %s)"""
        gravar_insert = (cep, rua, bairro, cidade, estado)
        cursor.execute(inserir_sql, gravar_insert)
        connection.commit() #garantir que todas as alterações sejam refletidas permanentemente no banco.
        cursor.close()
        connection.close()
        return "Endereço cadastrado com sucesso!"
      
    except Exception as e:
        return "Erro ao cadastrar endereço. Por favor tente novamente."
