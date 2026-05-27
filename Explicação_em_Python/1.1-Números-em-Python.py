#AULA COMPLETA: NUMEROS EM PYTHON

"""  ""
1 - Tipos númericos
2 - conversão de tipos
3 - Hierarquia
4 - Operação matemática
5 - coerção de tipos
6 - vericação de tipos
7 - entrada de dados
"""  ""
############################
# PASSO 01 - TIPOS NÚMERICOS
############################
#int -> números inteiros
#float -> números com casas decimais
#complex -> números complexos (usado em matemática/ engenharia)

print("======= TIPOS NÚMERICOS ======")

#EXEMPLO 01 - NUMERO INTEIRO

#ciramos uma variável chamada "numero_inteiro"
numero_inteiro = 10

#mostramos o valor
print ("Valor:", numero_inteiro)

#Type() mostra qual é o tipo da variável
print("Tipo:",type(numero_inteiro) )

print("--------------------------------------")

# EXEMPLO 02 - NUMERO DECIMAL

#Float é um número com ponto decimal
numero_decimal = 3.14

print ("Valor:", numero_decimal)
print ("Tipo:", type(numero_decimal))

print("---------------------------------")

#EXEMPLO 03 - NÚMEROS COMPLEXOS

#Um número complexo possui duas partes:
#Parte real (numero normal)
#Parte Imaginaria (multiplicada por j)

#Estrutura Geral:
# número = a + bj

# a = parte real
# b = parte Imaginaria
# j = unidadde Imaginaria 

numero_complexo = 2 + 3j

print("Valor:", numero_complexo)
print("Tipo:", type(numero_complexo))

print("---------------------------------")

#EXEMPLO 03 - ACESSANDO CADA PARTE DO NÚMERO

# .real retornar a parte real
print ("Parte real:", numero_complexo.real)

# .imag retorna a parte imaginaria
print ("Parte Imaginaria:", numero_complexo.imag)

# Apenas para separar visualmente a saída no terminal
print("\n\n")

#===============================
## PASSO 02 - CONVERSÃO TIPOS
#==============================

## Exemplo Clássico:
## Dados vindos do usuário são texto (string), muitas vezes é necessário converter eles.

print("====== Conversões =======")

# float -> int

valor = int(3.9)

print("int(3.9):", valor)
print("Tipo:", type(valor))

# string -> int 
valor1 = "10"
print (type(valor1))

valor2 = int("10")
print ('int("10"):', valor2)
print ("tipo:", type(valor2))

# int --> Float
valor3 = float(10)
print("float(10):", valor3)
print("Tipo:", type(valor3))

