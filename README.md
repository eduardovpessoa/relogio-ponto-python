# Relógio de Ponto - OraSystems

### Sejam Bem Vindos! (Pull Requests são aceitas! ;D)

## Introdução

Este sistema foi desenvolvido com Python e possui a finalidade de funcionar em um Raspberry Pi (se assemelhando a um relógio de ponto). O sistema identifica o código de barras por meio do leitor e insere no banco de dados a "Data" e a "Hora" do "Funcionário" que acabou de passar o seu crachá/código.

## Requisitos

- Você precisará de:
1) Um Raspberry Pi (qualquer modelo).
2) Um leitor de código de barras.
3) Um banco de dados com a estrutura do arquivo "script.sql" (estamos utilizando o Oracle, mas pode-se utilizar qualquer outro).

## Configuração

1) Instale o leitor de código de barras no Raspberry Pi e crie a estrutura do banco de dados.
2) Cadastre os funcionários e seus respectivos códigos na base de dados. 
3) Copie esse projeto p/ o Raspberry e rode a aplicação com o seguinte comando:
- python relogio.py

### Pronto!! Basta realizar a leitura ;)


## Agradecimentos

- https://github.com/alanecher
- https://github.com/duduvp
- https://github.com/viniciussanchez
- http://www.orasystems.com.br

## OraSystems - Consultoria e Tecnologia
<a href='http://www.orasystems.com.br'><img src='https://i.ytimg.com/i/qCLTYgDE9Wh0bbPmgG_qZA/mq1.jpg?v=53461fc0'/></a>
