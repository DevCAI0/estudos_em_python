# DECLARAÇÃO DE TUPLAS

# Tupla vazia
tupla_vazia = ()
print("Tupla vazia:", tupla_vazia)

# Tupla com um único elemento (é necessário a vírgula após o elemento)
tupla_unica = (5,)
print("Tupla com um único elemento:", tupla_unica)

# Tupla de inteiros
tupla_inteiros = (1, 2, 3, 4, 5)
print("Tupla de inteiros:", tupla_inteiros)

# Tupla de strings
tupla_strings = ("Caio", "Gabriel", "Ana")
print("Tupla de strings:", tupla_strings)

# Tupla mista (diferentes tipos de dados)
tupla_mista = (1, "Caio", 3.14, True)
print("Tupla mista:", tupla_mista)

# ACESSANDO ELEMENTOS DE UMA TUPLA

# Acessando pelo índice (o índice começa em 0)
print("Primeiro elemento da tupla de inteiros:", tupla_inteiros[0])

# Acessando o último elemento com índice negativo
print("Último elemento da tupla de strings:", tupla_strings[-1])

# FATIAMENTO DE TUPLAS (SLICING)
# Obtendo uma parte da tupla (do índice 1 ao 3, excluindo o 3)
print("Fatiamento da tupla de inteiros [1:3]:", tupla_inteiros[1:3])

# Acessando todos os elementos a partir de um índice
print("A partir do índice 2:", tupla_inteiros[2:])

# Acessando todos os elementos até um índice
print("Até o índice 3:", tupla_inteiros[:3])

# Acessando toda a tupla com um intervalo específico
print("Elementos com passo 2:", tupla_inteiros[::2])

# TUPLAS SÃO IMUTÁVEIS

# Tentar modificar um elemento de uma tupla gera erro
# Exemplo de erro:
# tupla_inteiros[0] = 10  # Isso gera TypeError

# CONCATENAÇÃO E REPETIÇÃO DE TUPLAS

# Concatenando duas tuplas
tupla_concatenada = tupla_strings + tupla_inteiros
print("Tupla concatenada:", tupla_concatenada)

# Multiplicação de tuplas (repetição de itens)
tupla_repetida = tupla_strings * 2
print("Tupla repetida:", tupla_repetida)

# DESEMPACOTAMENTO DE TUPLAS

# Desempacotando os valores de uma tupla em variáveis
nome, sobrenome, idade = ("Caio", "Pereira", 24)
print("Nome:", nome)
print("Sobrenome:", sobrenome)
print("Idade:", idade)

# Se a quantidade de variáveis for menor que os itens, usamos *
nome, *detalhes = ("Caio", "Pereira", 24, "Brasil")
print("Nome:", nome)
print("Outros detalhes:", detalhes)

# MÉTODOS PARA TUPLAS

# count() - Conta o número de ocorrências de um valor na tupla
contagem = tupla_inteiros.count(2)
print("Número de ocorrências do número 2:", contagem)

# index() - Retorna o índice da primeira ocorrência de um valor
indice = tupla_strings.index("Gabriel")
print("Índice da primeira ocorrência de 'Gabriel':", indice)

# PERTINÊNCIA (MEMBRESIA)

# Verificar se um elemento está presente na tupla (in)
print("Caio está na tupla de strings?", "Caio" in tupla_strings)

# Verificar se um elemento **não** está presente na tupla (not in)
print("Maria não está na tupla de strings?", "Maria" not in tupla_strings)

# FUNÇÕES ÚTEIS COM TUPLAS

# len() - Retorna o número de elementos da tupla
print("Número de elementos na tupla de inteiros:", len(tupla_inteiros))

# min() - Retorna o menor valor da tupla
print("Menor valor na tupla de inteiros:", min(tupla_inteiros))

# max() - Retorna o maior valor da tupla
print("Maior valor na tupla de inteiros:", max(tupla_inteiros))

# sum() - Retorna a soma de todos os valores da tupla (válido apenas para tuplas numéricas)
print("Soma dos valores da tupla de inteiros:", sum(tupla_inteiros))

# CONVERTENDO ENTRE LISTA E TUPLA

# Converter uma tupla em lista (para modificar os valores)
lista_convertida = list(tupla_inteiros)
print("Tupla convertida para lista:", lista_convertida)

# Modificando a lista
lista_convertida[0] = 10
print("Lista modificada:", lista_convertida)

# Convertendo de volta para tupla
tupla_modificada = tuple(lista_convertida)
print("Lista convertida de volta para tupla:", tupla_modificada)

# ITERAÇÃO SOBRE TUPLAS

# Usando um loop for para percorrer os elementos de uma tupla
for item in tupla_strings:
    print("Nome:", item)

# TUPLA ANINHADA (TUPLA DENTRO DE TUPLA)

tupla_aninhada = ((1, 2, 3), ("a", "b", "c"))
print("Tupla aninhada:", tupla_aninhada)

# Acessando elementos de uma tupla aninhada
print("Primeiro elemento da segunda tupla aninhada:", tupla_aninhada[1][0])
