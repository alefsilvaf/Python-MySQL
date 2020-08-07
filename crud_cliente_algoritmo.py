import pymysql

host= "localhost"
user= "root"
password= "senha"
db= "crud_cliente"
port = 3306
con= pymysql.connect(host, user, password, db, port)

#Exibe
c= con.cursor()
c.execute("SELECT nome, cpf, email, telefone FROM usuarios")
res=c.fetchall()
print('Nomes: ')
for row in res:
	print(row)

"""#Insere
c.execute("INSERT INTO usuarios (nome, cpf, email, telefone) VALUES ('Álef Silva', '12345678910', 'alefsilva@outlook.com', '35 3555 1515')")

con.commit()
print('Usuarios e seus dados: ')
for row in res:
	print(row)
"""

#Delete
c.execute("DELETE FROM usuarios WHERE nome = 'Labaxurias Urias'")
con.commit()
print('Depois de deletar: ')
for row in res:
	print(row)



"""c.execute("UPDATE alunos SET nome = 'Joaquim' WHERE cpf = '12345678910'")
con.commit()
for row in res:
	print(row)
"""
c.close()
