# Estrutura básica de condicional if, elif, else
# O comando print("-" * 50) em Python é uma maneira de imprimir uma linha de traços repetidos. Aqui está o que está acontecendo:
# Neste exemplo, estamos verificando em qual faixa etária uma pessoa se encontra
idade = 25
if idade < 12:
    print("Criança")  # Executa se a idade for menor que 12
elif idade < 18:
    print("Adolescente")  # Executa se a idade for entre 12 e 17
elif idade < 65:
    print("Adulto")  # Executa se a idade for entre 18 e 64
else:
    print("Idoso")  # Executa se a idade for maior ou igual a 65
# O fluxo de execução segue do "if" até o "else", dependendo da condição.

print("-" * 50)

# Condicional if e else simples (par ou ímpar)
# Aqui estamos verificando se um número é par ou ímpar
numero = 7
if numero % 2 == 0:
    print("O número é par")  # Executa se o número for divisível por 2 (ou seja, par)
else:
    print("O número é ímpar")  # Executa se a condição anterior for falsa (ou seja, ímpar)

print("-" * 50)

# Condicional aninhada (voto)
# Verifica se a pessoa pode votar, dependendo da nacionalidade e da idade
idade = 17
nacionalidade = "Brasileiro"
if nacionalidade == "Brasileiro":
    if idade >= 16:
        print("Pode votar")  # Executa se for brasileiro e tiver 16 anos ou mais
    else:
        print("Não pode votar")  # Executa se for brasileiro, mas tiver menos de 16 anos
else:
    print("Não é brasileiro, então não pode votar")  # Executa se não for brasileiro

print("-" * 50)

# Condicional com operadores lógicos (and, or, not)
# Neste exemplo, verificamos se a pessoa pode dirigir (maior de idade e com habilitação)
idade = 20
tem_carteira = True
if idade >= 18 and tem_carteira:
    print("Pode dirigir")  # Executa se a idade for maior ou igual a 18 e a pessoa tiver carteira de motorista
else:
    print("Não pode dirigir")  # Executa se uma das condições não for verdadeira

print("-" * 50)

# Operadores de comparação e lógicos combinados
# Aqui verificamos se um número está entre 10 e 20 ou é menor que 5
numero = 12
if (numero > 10 and numero < 20) or numero < 5:
    print("O número está entre 10 e 20 ou é menor que 5")  # Executa se o número estiver entre 10 e 20 ou for menor que 5
else:
    print("O número não atende às condições")  # Executa se nenhuma das condições for verdadeira

print("-" * 50)

# Condicional em uma linha (expressão ternária)
# Usando expressão ternária para verificar se o número é par ou ímpar em uma linha
numero = 4
resultado = "par" if numero % 2 == 0 else "ímpar"
# Se a condição "numero % 2 == 0" for verdadeira, "par" será atribuído à variável resultado, caso contrário, "ímpar"
print(f"O número é {resultado}")

print("-" * 50)

# Uso de pass em condicional
# O pass é usado para deixar o bloco vazio sem gerar erros
numero = 5
if numero > 10:
    pass  # Não faz nada se o número for maior que 10
else:
    print("O número não é maior que 10")  # Executa se o número for menor ou igual a 10

print("-" * 50)

# Múltiplas comparações
# Verificamos se o número está entre 10 e 20 usando comparações encadeadas
numero = 15
if 10 < numero < 20:
    print("O número está entre 10 e 20")  # Executa se o número estiver no intervalo de 10 a 20
else:
    print("O número não está entre 10 e 20")  # Executa se o número não estiver no intervalo

print("-" * 50)

# Verificando se um item está em uma lista
# Usamos o operador in para verificar se um elemento está presente na lista
frutas = ["maçã", "banana", "laranja"]
fruta = "maçã"
if fruta in frutas:
    print(f"{fruta} está na lista de frutas")  # Executa se a fruta estiver na lista
else:
    print(f"{fruta} não está na lista de frutas")  # Executa se a fruta não estiver na lista

print("-" * 50)

# Exemplo completo com várias condições
# Neste exemplo, usamos várias condições e verificamos diferentes atributos (idade, habilitação, estado civil)
idade = 30
habilitacao = True
estado_civil = "casado"
if idade >= 18 and habilitacao:
    if estado_civil == "casado":
        print("Pode dirigir e é casado")  # Executa se a pessoa for maior de idade, tiver habilitação e for casada
    elif estado_civil == "solteiro":
        print("Pode dirigir e é solteiro")  # Executa se a pessoa for maior de idade, tiver habilitação e for solteira
    else:
        print("Pode dirigir, mas estado civil desconhecido")  # Executa se a pessoa for maior de idade e tiver habilitação
