import pymysql

host= "localhost"
user= "Alef"
password= "123456"
db= "escola_curso"
port = 3306
con= pymysql.connect(host, user, password, db, port)

#Exibe
c= con.cursor()
c.execute("SELECT nome, cidade FROM alunos")
res=c.fetchall()
print('Alunos e seus dados: ')
for row in res:
	print(row)

"""#Insere
c.execute("INSERT INTO alunos (nome, nascimento, endereco, cidade, estado, cpf) VALUES ('Labaxurias Urias', '4040-01-01', 'Dinhabawns', 'Diabatown', 'SP', 66666666666)")
con.commit()
print('Alunos e seus dados: ')
for row in res:
	print(row)
"""

"""#Delete
c.execute("DELETE FROM alunos WHERE idalunos > '13'")
con.commit()
print('Depois de deletar: ')
for row in res:
	print(row)
"""


"""c.execute("UPDATE alunos SET nome = 'Joaquim' WHERE cpf = '12345678910'")
con.commit()
for row in res:
	print(row)
"""
c.close()

