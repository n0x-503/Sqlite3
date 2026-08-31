import sqlite3

conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor() #intermediario entre python e o banco de dados

cursor.execute("""CREATE TABLE IF NOT EXISTS contas_bancarias (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    titular TEXT NOT NULL,
                    saldo REAL NOT NULL,
                    cpf TEXT NOT NULL UNIQUE 
                )""")

#cursor.execute("""INSERT INTO contas_bancarias (titular, saldo, cpf) VALUES 
#                ('João Silva', 1000.00, '123.456.789-00'),
#                ('Maria Oliveira', 2500.50, '987.654.321-00'),
#                ('Carlos Souza', 500.75, '456.789.123-00')""") #insire valores na tabela contas_bancarias

cursor.execute("SELECT * FROM contas_bancarias WHERE saldo > 1000") #seleciona todos os registros da tabela contas_bancarias
contas = cursor.fetchall() #retorna todos os registros selecionados
cursor.execute("UPDATE contas_bancarias SET saldo = saldo + 500 WHERE titular = 'João Silva'") #atualiza o saldo do titular João Silva

for contas in contas:
    id, titular, saldo, cpf = contas
    print(f"ID: {id}, Titular: {titular}, Saldo: {saldo}, CPF: {cpf}") 

conexao.commit() #salva as alterações no banco de dados
