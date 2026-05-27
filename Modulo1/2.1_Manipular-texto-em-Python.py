#AULA COMPLETA - STRINGS EM PYTHON

# - Criação de strings
# - Strings multilinha 
# - Índices e slices
# - Operações com strings
# - Inutabilidade 
# - Métodos úteis
# - Formatação de texto
# - Unicode e bytes

#-----------------------------------------------------
# 1) CRIAÇÃO DE STRINGS
#-----------------------------------------------------

# Strings são textos em python.
# Podem ser criadas usando aspas simples ou duplas

texto1 = "Python"
texto2 = 'Curso de Python'
texto3 = "Copa 'padrão fifa'"
texto4 = 'Copa "padrão fifa"'

print(texto1, texto2, texto3, texto4)

# Python permite misturar as aspas simples e duplas, dentro das strings sem precisar escapas caracteres

#-----------------------------------------------------
# 2) STRINGS MULTILINHA
#-----------------------------------------------------

# Usando três aspas (""" ou ''') para criar textos que ocupam várias linhas.

menu = """\
Uso: programa [OPÇÕES]
-h Exibe ajuda
-U Url do dataset
"""
print(menu)

# Esse formato é muito usado para:
# - Menus
# - Documentação
# - Textos longos

#-----------------------------------------------------
# 3) CONCATENAÇÃO AUTOMÁTICA
#-----------------------------------------------------

# Quando duas strings aparecem lado a lado, o Python junta automaticamente

texto = ("Copa" " 2026" " Neymar é show mesmo?" " Talvez")
print(texto)

#-----------------------------------------------------
# 4) STRINGS COMO SEQUÊNCIAS
#-----------------------------------------------------

#  Uma string funciona como uma sequência de caracteres, cada caractere possui um índice

st = "maracana"
print("Primeira Letra:", st[0])

# Só exibir a letra: m

print("ultima Letra:", st[-1])

print("Trecho 1:4:", st[1:4])

print("Do ínicio  até 3:", st[:3])

print("Do 2 até o fim:", st[2:])

print("Tamanho:", len(st))

#-----------------------------------------------------
# 5) OPERAÇÕES COM STRINGS
#-----------------------------------------------------
# Python permite várias operações com strings

print("m" in st)
# Significa que a letra "m" existe dentro da string

print("x" not in st)
# Significa que "X" não existe na string

print("m" * 67)
# Multiplicação repete a string

print("m" + "aracana")
# Operador + concatena strings

#-----------------------------------------------------
# 6) STRINGS SÃO IMUTÁVEIS
#-----------------------------------------------------
# Strings não podem ser alteradas diretamente!!!
# Isso significa que o conteúdo original não muda.
# O que acontece é a criação de uma nova string.

texto = "python 3"

# Método replace cria uma nova string
texto = texto.replace("3", "2")

print(texto)

#-----------------------------------------------------
# 7) MÉTODOS IMPORTANTES
#-----------------------------------------------------
# Strings possuem vários métodos úteis

cidade = "maracana"
# Coloca a primeira letra em maiúscula

print(cidade.capitalize())

# Conta quantas vezes "A" aparece

print(cidade.count("a"))

# Verificar se começa com "m"

print(cidade.startswith("m"))

#Verifica se termina com "z"
print(cidade.endswith("z"))

frase = "Copa de 2002"

# Divide a string em uma lista
print(frase.split(" "))


#-----------------------------------------------------
# 8) FORMATAÇÃO DE STRINGS
#-----------------------------------------------------
