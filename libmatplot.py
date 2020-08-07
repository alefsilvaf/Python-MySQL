import matplotlib.pyplot as plt 

x = [1, 3, 5, 7, 9]
y = [2, 3, 7, 1, 0]
z = [200, 25, 400, 3300, 100]
 
titulo = "Scatterplot: gráfico de dispersão"
eixox = "Eixo X"
eixoy = "Eixo Y"
 
# Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)
 
plt.plot(x, y, color="#000000", linestyle="--")
plt.scatter(x, y, label="Meus pontos", color="k", marker=".", s=z)
plt.legend()
plt.show()
plt.savefig("figura.png")

"""x = [1,2,5,4,5]
y = [2,3,7,1,0]

a = [5,4,3,2,1]
b = [1,2,3,4,5]

titulo= "Gráfico de barras"
eixox= "Eixo X"
eixoy= "Eixo Y"

plt.title("Gráfico:")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.plot(x,y, label = "Grafic 1")
plt.plot(a,b, label = "Grafic 2")
plt.legend()
#plt.plot(x,y)
plt.show()"""
