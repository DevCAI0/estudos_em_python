# DECLARAÇÃO

# Variável que armazena o nome completo como uma string
nome_completo = "Gabriel Casemiro"

# Variável que armazena o nome completo com a possibilidade de quebrar a linha usando aspas triplas
nome_completo_com_aspas = """Gabriel 
Casemiro"""

# Variável que armazena o nome completo, mas quebra a linha explicitamente com uma barra invertida \
nome_completo_com_quebra = "Gabriel \
Casemiro"

# Variáveis separadas para o nome e o sobrenome
nome = "Caio"
sobrenome = "Pereira"

# FORMATAÇÃO

# Exibe o nome completo na primeira forma (simples, variável já formatada)
print("nome completo (1a forma):", nome_completo)

# Exibe o nome completo na segunda forma (concatenação de string usando o operador +)
print("nome completo (2a forma): " + nome_completo)

# Exibe o nome completo na terceira forma (concatenando duas strings "Caio" e "Ribeiro" diretamente)
print("nome completo (3a forma): " + "Caio " + "Ribeiro ")

# Exibe o nome completo na quarta forma (concatenação usando vírgula, a vírgula insere automaticamente um espaço entre as strings)
print("nome completo (4a forma): " + "Caio", "Ribeiro ")

# Exibe o nome completo com aspas triplas (mantém quebras de linha dentro do texto)
print("nome completo (5a forma): " + nome_completo_com_aspas)

# Exibe o nome completo com a quebra de linha forçada com barra invertida \
print("nome completo (6a forma): " + nome_completo_com_quebra)

# Exibe o nome completo com formatação do estilo C (usa %s para inserir variáveis no texto)
print("nome completo (7a forma): %s" % nome_completo_com_quebra)

# Exibe o nome e sobrenome usando formatação do estilo C, com múltiplas variáveis %s
print("nome completo (8a forma): %s %s" % (nome, sobrenome))

# Exibe o nome e sobrenome usando f-strings (fácil e moderno, insere variáveis diretamente no texto entre chaves {})
print(f"nome completo (9a forma): {nome} {sobrenome}")

# Exibe o nome e sobrenome usando o método format, insere variáveis dentro de {} na string
print("nome completo (10a forma): {} {}".format(nome, sobrenome))

# Usando formatação com índices para especificar as posições das variáveis (pode repetir variáveis)
print("nome completo (11a forma): {0} {1}".format(nome, sobrenome))
print("nome completo (12a forma): {1}, {0}".format(nome, sobrenome))  # Invertendo a ordem

# Usando formatação nomeada, passando os valores como pares chave-valor
print("nome completo (13a forma): {n} {s}".format(n=nome, s=sobrenome))

# Usando formatação com alinhamento e largura mínima de campo
print("nome completo (14a forma): {:<10} {:>10}".format(nome, sobrenome))  # Alinhando à esquerda e à direita

# Usando f-string com formatação de largura mínima e alinhamento
print(f"nome completo (15a forma): {nome:<10} {sobrenome:>10}")

# Usando f-string com a função de conversão (repr)
print(f"nome completo (16a forma): {nome!r} {sobrenome!r}")

# Usando o método de formatação format_map() com um dicionário
nome_dict = {"n": nome, "s": sobrenome}
print("nome completo (17a forma): {n} {s}".format_map(nome_dict))
