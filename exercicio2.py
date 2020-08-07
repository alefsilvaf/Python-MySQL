# -*- coding: utf-8 -*-
"""	Lista de exercicios PRATICOS 2
	Escreva um programa que compare se duas sequências digitadas pelo usuário são iguais.   
	Escreva um programa que abra um arquivo digitado pelo usuário e imprima seu conteúdo na tela.   
	Escreva um programa que receba uma sequência digitada pelo usuário e a salve num arquivo no formato fasta.   
	Escreva um programa que exiba um menu e pergunte o que o usuário deseja fazer. Se o usuário digitar 1, o programa 
	deve chamar uma função que lê um arquivo de texto. Se o usuário apertar 2, o programa deve imprimir o conteúdo do 
	arquivo lido anteriormente. Se o usuário apertar três o programa deve ser fechado.
	Escreva um programa que leia um arquivo multi-fasta e armazene em um dicionário: cabeçalho da sequência como a chave e a 
	sequência como valor. """

#EXERCICIO1
"""
seq1 = "abracadabra"
seq2 = "abracadabra"
seq3 = "gambiarra"

print('Cara, bora comparar esses bagulhos ae!')

if seq1 == seq2:
	print ('São iguais (s1 e s2)')
else:
	print('São diferentes, mano!')
if seq2 == seq3:
	print('São iguais (s1 e s3)')
else:
	print('São diferentes, mano!')"""

#EXERCICIO2
"""
arquivo = (input('Digite o nome do arquivo que deseja abrir: ') + ".txt")
try:
	lendo=open(arquivo, "r")
	print(lendo.read())
except:
	print("Arquivo não existe")"""

#EXERCICIO3
"""
seq = input('Digite a sequência: ')
arquivo = open("fasta.fasta","w")
arquivo.write(">sequencia\n")
arquivo.write(seq)
arquivo.close()"""

#EXERCICIO4
"""
def openingarquivo():
	arquivo = open ("ArquivoTeste.txt", "r")
	print("oi")
	return(arquivo)

def imprime_arquivo(arquivo):
	print (arquivo.read())
	print("Quero mais")

escolha=0

while escolha != 3:
	print ("Menu:\nDigite [1] para ler um arquivo.\nDigite [2] para imprimir o que foi lido no arquivo.\nDigite [3] para fechar o programa.\n")
	escolha = int(input("Digite sua escolha: "))
	if escolha == 1:
		arquivo=openingarquivo()

	elif escolha == 2:
		imprime_arquivo(arquivo)
		arquivo.close()"""

#EXERCICIO5
"""
arquivo=open("fasta.fasta")
linhas = arquivo.readlines()
dicionario={}

for linha in linhas:
	if linha[0] == ">":
		aux = linha.strip()
		dicionario[aux]=" "
	else:dicionario[aux]=dicionario[aux]+linha.strip()

print(dicionario)"""
