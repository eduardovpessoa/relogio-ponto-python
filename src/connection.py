# Importa os módulos necessário
import cx_Oracle
import datetime

# Dados de Acesso ao Banco
host = ''
user = ''
passwd = ''
port = ''
service = ''

# Variável de Conexão
conn = None
cursor = None


def __init__(self):
    self.conn = cx_Oracle.connect(user + '/' + passwd + '@' + host + ':' + port + '/' + service)
    self.cursor = self.conn.cursor()


def registra_ponto(self, codigo_barras):
    self.cursor.execute("SELECT ID_FUNCIONARIO FROM FUNCIONARIO WHERE CODIGO_BARRAS = codigo_barras")
    resultado = self.cursor.fetchone()
    if len(resultado) > 0:
        self.cursor.execute("INSERT INTO REGISTRO (ID_FUNCIONARIO, DATA_HORA) VALUES (resultado, sysdate)")
        self.conn.commit()
        return True
    return False


def __del__(self):
    self.conn.close()
