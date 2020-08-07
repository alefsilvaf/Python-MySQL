arquivo = open ("ArquivoTeste.txt", "w")
arquivo.write("A Beyoncé tá no mesmo nível, talvez acima...")
arquivo.close()
arquivo = open ("ArquivoTeste.txt", "r")
print(arquivo.read())
arquivo.close()

