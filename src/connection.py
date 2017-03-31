import cx_Oracle

# Dados de Acesso ao Banco
host = ''
user = ''
passwd = ''
port = ''
service = ''


# Abre a Conexao
def connect():
    print '--- Starting Database Connection ---'
    return cx_Oracle.connect(user + '/' + passwd + '@' + host + ':' + port + '/' + service)


# Fecha a Conexao
def close(conn):
    print '--- Closing Database Connection ---'
    conn.close()
