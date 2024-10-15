# DECLARAÇÃO DE BOOLEANOS

# Variáveis booleanas podem armazenar apenas dois valores: True ou False
is_true = True
is_false = False

# OPERADORES LÓGICOS

# AND - Retorna True se ambas as condições forem verdadeiras
print("True AND True:", True and True)   # True
print("True AND False:", True and False)  # False

# OR - Retorna True se pelo menos uma das condições for verdadeira
print("True OR False:", True or False)   # True
print("False OR False:", False or False)  # False

# NOT - Inverte o valor booleano
print("NOT True:", not True)   # False
print("NOT False:", not False)  # True

# OPERADORES DE COMPARAÇÃO

# Igualdade (==) - Verifica se dois valores são iguais
print("5 == 5:", 5 == 5)  # True
print("5 == 3:", 5 == 3)  # False

# Diferença (!=) - Verifica se dois valores são diferentes
print("5 != 3:", 5 != 3)  # True
print("5 != 5:", 5 != 5)  # False

# Maior que (>)
print("5 > 3:", 5 > 3)  # True
print("3 > 5:", 3 > 5)  # False

# Menor que (<)
print("3 < 5:", 3 < 5)  # True
print("5 < 3:", 5 < 3)  # False

# Maior ou igual (>=)
print("5 >= 5:", 5 >= 5)  # True
print("5 >= 3:", 5 >= 3)  # True

# Menor ou igual (<=)
print("3 <= 5:", 3 <= 5)  # True
print("5 <= 3:", 5 <= 3)  # False

# OPERADORES DE IDENTIDADE

# is - Verifica se duas variáveis referenciam o mesmo objeto
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print("a is b:", a is b)  # True (mesmo objeto na memória)
print("a is c:", a is c)  # False (objetos diferentes, mas com o mesmo valor)

# is not - Verifica se duas variáveis não referenciam o mesmo objeto
print("a is not c:", a is not c)  # True

# OPERADORES DE PERTINÊNCIA (MEMBRESIA)

# in - Verifica se um elemento está presente em uma sequência (como uma lista ou string)
print("'Caio' in ['Caio', 'Gabriel', 'Pedro']:", 'Caio' in ['Caio', 'Gabriel', 'Pedro'])  # True
print("'Maria' in ['Caio', 'Gabriel', 'Pedro']:", 'Maria' in ['Caio', 'Gabriel', 'Pedro'])  # False

# not in - Verifica se um elemento **não** está presente em uma sequência
print("'Maria' not in ['Caio', 'Gabriel', 'Pedro']:", 'Maria' not in ['Caio', 'Gabriel', 'Pedro'])  # True

# OUTROS EXEMPLOS DE OPERAÇÕES BOOLEANAS

# Usando valores que podem ser convertidos para booleanos (0 é False, qualquer outro número é True)
print("bool(0):", bool(0))  # False
print("bool(1):", bool(1))  # True

# Strings vazias são False, qualquer outra string é True
print("bool(''):", bool(''))  # False
print("bool('Caio'):", bool('Caio'))  # True

# Listas vazias são False, listas com elementos são True
