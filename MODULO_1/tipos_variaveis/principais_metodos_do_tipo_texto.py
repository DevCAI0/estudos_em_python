# DECLARAÇÃO

nome_completo = "Gabriel Casemiro"
nome = "Caio"
sobrenome = "Pereira"

# MÉTODOS DE STRINGS

# upper() - Converte todos os caracteres da string para maiúsculas
print("nome completo em maiúsculas:", nome_completo.upper())

# lower() - Converte todos os caracteres da string para minúsculas
print("nome completo em minúsculas:", nome_completo.lower())

# capitalize() - Converte o primeiro caractere da string para maiúscula e o restante para minúsculas
print("nome completo com o primeiro caractere maiúsculo:", nome_completo.capitalize())

# title() - Converte o primeiro caractere de cada palavra para maiúscula
print("nome completo em formato de título:", nome_completo.title())

# swapcase() - Inverte a capitalização: maiúsculas para minúsculas e vice-versa
print("nome completo com maiúsculas e minúsculas trocadas:", nome_completo.swapcase())

# strip() - Remove espaços em branco no início e no fim da string
nome_com_espacos = "   Caio Pereira   "
print("nome completo sem espaços extras:", nome_com_espacos.strip())

# lstrip() - Remove apenas os espaços à esquerda (início da string)
print("nome completo com espaços à esquerda removidos:", nome_com_espacos.lstrip())

# rstrip() - Remove apenas os espaços à direita (final da string)
print("nome completo com espaços à direita removidos:", nome_com_espacos.rstrip())

# replace() - Substitui parte de uma string por outra
print("nome completo com sobrenome alterado:", nome_completo.replace("Casemiro", "Pereira"))

# count() - Conta quantas vezes um caractere ou sequência de caracteres aparece na string
print("quantas vezes a letra 'a' aparece no nome completo:", nome_completo.count('a'))

# find() - Encontra a primeira ocorrência de um caractere ou sequência de caracteres e retorna sua posição
print("posição da primeira ocorrência de 'Casemiro':", nome_completo.find("Casemiro"))

# rfind() - Encontra a última ocorrência de um caractere ou sequência de caracteres e retorna sua posição
print("posição da última ocorrência da letra 'a':", nome_completo.rfind('a'))

# startswith() - Verifica se a string começa com um determinado caractere ou sequência de caracteres
print("nome completo começa com 'Gabriel'?:", nome_completo.startswith("Gabriel"))

# endswith() - Verifica se a string termina com um determinado caractere ou sequência de caracteres
print("nome completo termina com 'Casemiro'?:", nome_completo.endswith("Casemiro"))

# split() - Divide a string em uma lista de substrings com base em um delimitador (por padrão, espaço)
print("nome completo dividido em lista:", nome_completo.split())

# join() - Junta elementos de uma lista em uma única string, com um delimitador
nomes_separados = ["Caio", "Pereira"]
print("nome completo juntado novamente:", " ".join(nomes_separados))

# isdigit() - Verifica se todos os caracteres da string são dígitos
idade = "24"
print("idade é composta apenas por dígitos?", idade.isdigit())

# isalpha() - Verifica se todos os caracteres da string são letras
print("nome é composto apenas por letras?", nome.isalpha())

# isalnum() - Verifica se todos os caracteres da string são letras ou dígitos
identificador = "Caio123"
print("identificador é composto por letras e/ou dígitos?", identificador.isalnum())

# isspace() - Verifica se todos os caracteres da string são espaços em branco
somente_espacos = "   "
print("a string contém apenas espaços em branco?", somente_espacos.isspace())

# zfill() - Preenche a string com zeros à esquerda até atingir um tamanho específico
numero = "42"
print("número preenchido com zeros:", numero.zfill(5))

# center() - Centraliza a string em uma área de comprimento especificado, preenchendo com espaços ou outro caractere
print("nome completo centralizado com 30 caracteres:", nome_completo.center(30))

# ljust() - Alinha a string à esquerda em uma área de comprimento especificado
print("nome completo alinhado à esquerda com 30 caracteres:", nome_completo.ljust(30))

# rjust() - Alinha a string à direita em uma área de comprimento especificado
print("nome completo alinhado à direita com 30 caracteres:", nome_completo.rjust(30))
