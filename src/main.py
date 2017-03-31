import connection


# Metodo Inicial - Loop de Leitura do Codigo de Barras
def start():
    while True:
        codigo = input('Insira o Codigo de Barras do Funcionario: ')
        if registra_ponto(codigo):
            print 'Ponto cadastrado com sucesso!'
        else:
            print 'Problemas ao cadastrar o ponto!'


# Metodo que Registra o Ponto de Acordo com o Codigo
def registra_ponto(codigo):
    conn = connection.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT F.COD_FUNCIONARIO FROM FUNCIONARIO F WHERE F.COD_BARRAS = %s" % codigo)
    resultado = cursor.fetchone()
    if resultado is None:
        connection.close(conn)
        return False
    if cursor.rowcount > 0:
        codigo_funcionario = resultado[0]
        cursor.execute("INSERT INTO REGISTRO_PONTO (COD_FUNCIONARIO) VALUES (%s)" % codigo_funcionario)
        connection.close(conn)
        return True
    connection.close(conn)
    return False


# Main - Inicia a Aplicacao Chamando o Metodo Start
if __name__ == '__main__':
    start()
