# DECLARAÇÃO DE DICIONÁRIOS

# Dicionário vazio
dicionario_vazio = {}
print("Dicionário vazio:", dicionario_vazio)

# Dicionário com pares chave-valor
dicionario_pessoas = {
    "nome": "Caio",
    "sobrenome": "Pereira",
    "idade": 24,
    "profissao": "Desenvolvedor"
}
print("Dicionário de uma pessoa:", dicionario_pessoas)

# Dicionário misto com diferentes tipos de valores
dicionario_misto = {
    "nome": "Gabriel",
    "idade": 30,
    "habilidades": ["Python", "JavaScript", "SQL"],
    "casado": False
}
print("Dicionário misto:", dicionario_misto)

# ACESSANDO VALORES EM UM DICIONÁRIO

# Acessando o valor associado a uma chave específica
print("Nome:", dicionario_pessoas["nome"])
print("Idade:", dicionario_pessoas["idade"])

# Usando o método get() para acessar valores (retorna None se a chave não existir)
print("Profissão:", dicionario_pessoas.get("profissao"))
print("Telefone (não existente):", dicionario_pessoas.get("telefone", "Chave não encontrada"))

# MODIFICANDO UM DICIONÁRIO

# Adicionando um novo par chave-valor
dicionario_pessoas["cidade"] = "São Paulo"
print("Dicionário após adicionar cidade:", dicionario_pessoas)

# Modificando o valor de uma chave existente
dicionario_pessoas["idade"] = 25
print("Dicionário após modificar a idade:", dicionario_pessoas)

# REMOVENDO ELEMENTOS DE UM DICIONÁRIO

# pop() - Remove um par chave-valor específico e retorna o valor removido
idade_removida = dicionario_pessoas.pop("idade")
print("Idade removida:", idade_removida)
print("Dicionário após remover idade:", dicionario_pessoas)

# popitem() - Remove e retorna o último par chave-valor adicionado
ultimo_item = dicionario_pessoas.popitem()
print("Último item removido:", ultimo_item)
print("Dicionário após popitem:", dicionario_pessoas)

# del - Remove uma chave específica
del dicionario_pessoas["profissao"]
print("Dicionário após remover profissão:", dicionario_pessoas)

# clear() - Remove todos os itens do dicionário
dicionario_pessoas.clear()
print("Dicionário após clear:", dicionario_pessoas)

# MÉTODOS ÚTEIS PARA DICIONÁRIOS

# keys() - Retorna todas as chaves do dicionário
print("Chaves do dicionário_misto:", dicionario_misto.keys())

# values() - Retorna todos os valores do dicionário
print("Valores do dicionário_misto:", dicionario_misto.values())

# items() - Retorna todos os pares chave-valor como tuplas
print("Pares chave-valor do dicionário_misto:", dicionario_misto.items())

# VERIFICAR SE UMA CHAVE EXISTE

# in - Verifica se uma chave existe no dicionário
print("A chave 'nome' está no dicionário_misto?", "nome" in dicionario_misto)
print("A chave 'telefone' está no dicionário_misto?", "telefone" in dicionario_misto)

# COPIANDO DICIONÁRIOS

# copy() - Cria uma cópia superficial do dicionário
dicionario_copia = dicionario_misto.copy()
print("Cópia do dicionário:", dicionario_copia)

# ATUALIZANDO UM DICIONÁRIO

# update() - Atualiza o dicionário com os pares chave-valor de outro dicionário ou de uma lista de tuplas
dicionario_novo = {"endereco": "Rua ABC", "telefone": "1234-5678"}
dicionario_copia.update(dicionario_novo)
print("Dicionário após update:", dicionario_copia)

# ITERANDO SOBRE UM DICIONÁRIO

# Iterando sobre as chaves
for chave in dicionario_misto:
    print("Chave:", chave)

# Iterando sobre os valores
for valor in dicionario_misto.values():
    print("Valor:", valor)

# Iterando sobre os pares chave-valor
for chave, valor in dicionario_misto.items():
    print(f"Chave: {chave}, Valor: {valor}")

# DICIONÁRIO ANINHADO (DICIONÁRIOS DENTRO DE DICIONÁRIOS)

dicionario_aninhado = {
    "pessoa1": {"nome": "Caio", "idade": 24},
    "pessoa2": {"nome": "Gabriel", "idade": 30},
    "pessoa3": {"nome": "Ana", "idade": 28}
}
print("Dicionário aninhado:", dicionario_aninhado)

# Acessando dados em um dicionário aninhado
print("Nome da pessoa 2:", dicionario_aninhado["pessoa2"]["nome"])
