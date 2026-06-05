print("--------------------------------------------------")
print("======= TREINAMENTO EM PYTHON ======")
print("\n\n")


#Numero inteiro em python

numero_int = 10
print("Valor:", numero_int)
print("Tipo:", type (numero_int))
print("--------------------------------------------------")


#Numero decimal em python "float"

numero_deci = 3.14
print("Valor:", numero_deci)
print("Tipo:", type(numero_deci))
print("--------------------------------------------------")


 #Numero complexo em python "j"

numero_comp = 2 +3j
print("Valor:", numero_comp)
print("Tipo:", type(numero_comp))
print("--------------------------------------------------")


#Acessando cada parte do numero
print("Parte real:", numero_comp.real)
print("--------------------------------------------------")


print("Parte imaginario:", numero_comp.imag)
print("--------------------------------------------------")


print("============== Conversões ================")

# float -> int

valor = int(3.9)
print("int(3.9):", valor)
print("Tipo:", type(valor))
print("--------------------------------------------------")

#strings -> int

valor1 = "10"
print(type(valor1))

valor2 = int("10")
print('int("10"):', valor2)
print("Tipo:", type (valor2))
print("--------------------------------------------------")

#int -> float

valor3 = float(10)
print("float(10):", valor3)
print("Tipo:", type (valor3))
print("--------------------------------------------------")



print("\n\n")
print("=============== Treinamento de Strings ===============")
print("\n\n")

#Criação de strings

texto1 = "Salve"
texto2 = 'Gamers'
texto3 = "Coxinha 'com catupiry'"
texto4 = 'Coxinha "com catupiry"'

print(texto1, texto2, texto3, texto4)
print("--------------------------------------------------")
#Menu

menu = """\
Compras: Loja [OPÇÕES]
-H Exibe ajuda para compras
-U Url do produto
-Y Quantidade
-C Confirmar compra do produto
"""
print(menu)

print("--------------------------------------------------")


texto = ("Coxinha" " Tempo" " Catupiry" " Pizza marguerita")
print(texto)


print("--------------------------------------------------")


st = "coxinha"
print("Palavra:",st)
print("Mostre a primeira letra:", st [0])

print("Mostre a última letra:", st [-1])

print("Trecho:", st [1:4])

print("Do início até 3:", st [:3])

print("Do 2 até o fim:", st [2:])

print("Tamanho", len(st))
print("--------------------------------------------------")

print("c" in st)

print("z" not in st)

print("c" * 67)

print("c" + "oxinha")
print("--------------------------------------------------")

texto1 = "python3"

texto1 = texto1.replace("3", "é vida")

print(texto1)

comida = "coxinha"

print(comida.capitalize())

print("\n\n")
print(comida.count("a"))

print("\n\n")
print(comida.startswith("co"))

print("\n\n")
print(comida.endswith("z"))

print("\n\n")
frase = "Cavalos são legais"

print(frase.split(" "))
print("\n\n")

print("========== Fim do treinamento ============")
print("05/06/2026")