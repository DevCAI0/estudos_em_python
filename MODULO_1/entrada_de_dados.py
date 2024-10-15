# Entrada de dados simples (nome e idade)
# A função input() captura a entrada do usuário como string, e estamos usando essa função para capturar o nome e a idade.

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))  # Convertendo a entrada para um número inteiro (int)

# Verificamos se a idade é válida, ou seja, se é maior ou igual a 0.
if idade < 0:
    print("Idade inválida.")
else:
    print(f"Olá, {nome}, você tem {idade} anos.")  # Usando f-string para inserir a variável dentro da string de forma fácil

print("-" * 50)

# Entrada de dois números e cálculo de soma
# Usamos input() para capturar dois números, separados por espaço. A função split() divide a string em duas partes.
# A função map() aplica a conversão para float em ambos os valores.

try:
    num1, num2 = map(float, input("Digite dois números separados por espaço: ").split())
    # Calculamos a soma dos dois números e mostramos o resultado
    print(f"A soma de {num1} e {num2} é {num1 + num2}.")
except ValueError:
    # Caso o usuário não insira números válidos, capturamos o erro e mostramos uma mensagem apropriada
    print("Você não digitou números válidos.")

print("-" * 50)

# Entrada de lista de frutas
# Solicitamos ao usuário que insira várias frutas separadas por vírgula. O método split(",") converte a string em uma lista.

frutas = input("Digite o nome das frutas separadas por vírgula: ").split(",")
# Mostramos a lista de frutas que o usuário digitou
print(f"Lista de frutas: {frutas}")

print("-" * 50)

# Entrada de confirmação (sim/não)
# Aqui, usamos input() para capturar uma confirmação do usuário (sim ou não). Usamos strip() para remover espaços
# e lower() para converter a resposta para minúsculas, facilitando a verificação.

resposta = input("Você deseja continuar? (sim/não): ").strip().lower()

# Verificamos se a resposta é "sim" e, caso contrário, assumimos que a resposta foi "não".
if resposta == "sim":
    print("Você escolheu continuar.")
else:
    print("Você escolheu sair.")

print("-" * 50)

# Verificação de múltiplos valores (idade e carteira de motorista)
# Aqui, vamos pedir novamente a idade e verificar se a pessoa tem carteira de motorista.

idade = int(input("Digite sua idade novamente: "))
habilitacao = input("Você tem carteira de motorista? (sim/não): ").strip().lower()

# Usamos uma condicional com operadores lógicos para verificar se a pessoa pode dirigir
if idade >= 18 and habilitacao == "sim":
    print("Você pode dirigir.")
else:
    print("Você não pode dirigir.")

print("-" * 50)

# Exemplo de verificação de um item em uma lista
# Vamos verificar se a fruta que o usuário digitou anteriormente está na lista.

fruta_para_verificar = input("Digite uma fruta para verificar se está na lista: ").strip()

# Usamos o operador in para verificar se a fruta está na lista de frutas digitadas anteriormente.
if fruta_para_verificar in frutas:
    print(f"{fruta_para_verificar} está na lista de frutas.")
else:
    print(f"{fruta_para_verificar} não está na lista de frutas.")

print("-" * 50)

# Usando try/except para verificar entradas numéricas inválidas
# Vamos capturar um número inteiro, garantindo que o usuário insira um valor correto.

try:
    numero_inteiro = int(input("Digite um número inteiro: "))
    print(f"Você digitou o número inteiro {numero_inteiro}.")
except ValueError:
    # Se o usuário não inserir um número inteiro, mostramos uma mensagem de erro.
    print("Erro: Você não digitou um número inteiro válido.")
