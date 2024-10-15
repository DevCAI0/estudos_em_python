# DECLARAÇÃO DE LISTAS

# Criando uma lista de inteiros
lista_inteiros = [1, 2, 3, 4, 5]
print("Lista de inteiros:", lista_inteiros)

# Criando uma lista de strings
lista_strings = ["Caio", "Gabriel", "Ana"]
print("Lista de strings:", lista_strings)

# Criando uma lista mista (com diferentes tipos de dados)
lista_mista = [1, "Caio", 3.14, True]
print("Lista mista:", lista_mista)

# LISTA VAZIA
lista_vazia = []
print("Lista vazia:", lista_vazia)

# ACESSANDO ELEMENTOS DA LISTA

# Acessando pelo índice (o índice começa em 0)
print("Primeiro elemento da lista de inteiros:", lista_inteiros[0])
print("Segundo elemento da lista de strings:", lista_strings[1])

# Acessando o último elemento com índice negativo
print("Último elemento da lista de inteiros:", lista_inteiros[-1])

# FATIAMENTO DE LISTAS (SLICING)
# Obtendo uma parte da lista (do índice 1 ao 3, excluindo o 3)
print("Fatiamento da lista de inteiros [1:3]:", lista_inteiros[1:3])

# Acessando todos os elementos a partir de um índice
print("A partir do índice 2:", lista_inteiros[2:])

# Acessando todos os elementos até um índice
print("Até o índice 3:", lista_inteiros[:3])

# Acessando toda a lista com um intervalo específico
print("Elementos com passo 2:", lista_inteiros[::2])

# MODIFICANDO LISTAS

# Substituir um valor em um índice específico
lista_inteiros[0] = 10
print("Lista de inteiros após alteração:", lista_inteiros)

# Adicionando elementos à lista

# append() - Adiciona um item ao final da lista
lista_inteiros.append(6)
print("Lista de inteiros após append:", lista_inteiros)

# insert() - Adiciona um item em um índice específico
lista_inteiros.insert(1, 15)
print("Lista de inteiros após insert:", lista_inteiros)

# extend() - Adiciona múltiplos itens de outra lista ao final
lista_inteiros.extend([7, 8, 9])
print("Lista de inteiros após extend:", lista_inteiros)

# REMOVENDO ELEMENTOS DA LISTA

# pop() - Remove e retorna o último item ou o item em um índice específico
ultimo = lista_inteiros.pop()
print("Último elemento removido:", ultimo)
print("Lista após pop:", lista_inteiros)

# pop() em um índice específico
removido = lista_inteiros.pop(2)
print("Elemento removido no índice 2:", removido)
print("Lista após remoção pelo índice:", lista_inteiros)

# remove() - Remove a primeira ocorrência de um valor
lista_inteiros.remove(15)
print("Lista após remove (remove o número 15):", lista_inteiros)

# clear() - Remove todos os itens da lista
lista_inteiros.clear()
print("Lista de inteiros após clear:", lista_inteiros)

# MANIPULAÇÃO DE LISTAS

# Contar o número de ocorrências de um valor
lista_numeros = [1, 2, 3, 2, 4, 2, 5]
contagem = lista_numeros.count(2)
print("Número de ocorrências de 2:", contagem)

# index() - Retorna o índice da primeira ocorrência de um valor
indice = lista_numeros.index(4)
print("Índice da primeira ocorrência de 4:", indice)

# sort() - Ordena a lista em ordem crescente
lista_numeros.sort()
print("Lista de números ordenada:", lista_numeros)

# reverse() - Inverte a ordem dos itens na lista
lista_numeros.reverse()
print("Lista de números em ordem reversa:", lista_numeros)

# copiar uma lista (evitar referência)
lista_copia = lista_numeros.copy()
print("Cópia da lista de números:", lista_copia)

# CONCATENAÇÃO DE LISTAS

# Concatenando duas listas
lista_concatenada = lista_strings + lista_numeros
print("Lista concatenada:", lista_concatenada)

# Multiplicação de listas (repetição de itens)
lista_multiplicada = lista_strings * 2
print("Lista multiplicada:", lista_multiplicada)

# ITERANDO SOBRE LISTAS

# Usando um loop for para iterar sobre os elementos da lista
for nome in lista_strings:
    print("Nome:", nome)

# Verificar se um item está na lista (pertinência)
print("Caio está na lista?", "Caio" in lista_strings)
print("Maria está na lista?", "Maria" in lista_strings)

# FUNÇÕES ÚTEIS PARA LISTAS

# len() - Retorna o número de elementos na lista
print("Número de elementos na lista de strings:", len(lista_strings))

# min() - Retorna o menor valor em uma lista numérica
print("Menor valor na lista de números:", min(lista_numeros))

# max() - Retorna o maior valor em uma lista numérica
print("Maior valor na lista de números:", max(lista_numeros))

# sum() - Retorna a soma de todos os valores em uma lista numérica
print("Soma dos valores na lista de números:", sum(lista_numeros))

# zip() - Combina duas listas em pares (útil em iterações)
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
lista_zip = list(zip(lista1, lista2))
print("Listas combinadas com zip:", lista_zip)

# MAP, FILTER E LAMBDA COM LISTAS

# map() - Aplica uma função a todos os elementos de uma lista
lista_quadrados = list(map(lambda x: x**2, lista1))
print("Lista de quadrados:", lista_quadrados)

# filter() - Filtra os elementos de uma lista com base em uma condição
lista_filtrada = list(filter(lambda x: x > 1, lista1))
print("Lista filtrada (elementos > 1):", lista_filtrada)
