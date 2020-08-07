#Programa pra identificar a maioridade do usuario através da entrada
""" Faça um programa que receba a idade do usuário e diga se ele é maior ou menor de idade.   

    Faça um programa que receba duas notas digitadas pelo usuário. Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado.   

    Escreva um programa que resolva uma equação de segundo grau.   

    Escreva um programa que ordene uma lista numérica com três elementos.   

    Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal. """

#EXERCICIO1
idade_do_user=int(input('1- Digite sua idade: '))
if idade_do_user >= 18:
	print("Legal, pode entrar!")
else:
	print("Barrado na balada, baby!")

#EXERCICIO2
nota1=float(input('2- Digite a nota1:'))
nota2=float(input('2- Digite a nota2:'))
nota3=(nota1+nota2)/2
if nota3 >= 6:
	print("AEEEEE! Aprovado!")
else:
	print('Vish... se lascou!')

#EXERCICIO3
a=2
b=7
c=5
delta=(b**2)-(4*a*c)
print("Delta=",delta)

#EXERCICIO4
lista=[1,3,1,2,7,1,]
aux=0
print('Lista antes de ordenar=',lista)
for i in range(len(lista)):
    for j in range(i + 1, len(lista)):

        if lista[i] > lista[j]:
           lista[i], lista[j] = lista[j], lista[i]
print(lista)

#EXERCICIO5
n1=input('Digite um numero:')
n2=input('Digite outro numero:')
opc=input("Digite um sinal para realizar a operação matemática: ")
if opc == "+": 
   result=float(int (n1) + int(n2))
elif opc == "-":
   result=float(int(n1)-int(n2))
elif opc == "*":
   result=float(int(n1)*int(n2))
elif opc == "/" and n2 == 0:
   print("Não é possivel realizar a divisão por zero")
   sys.exit(1)
elif opc == "/":
	result=float(int(n1)/int(n2))
print (result)



