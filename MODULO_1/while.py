# Exemplo 1: Loop básico com contagem simples
# Vamos usar um loop while para contar de 1 até 5

contador = 1  # Inicializamos o contador com 1
while contador <= 5:  # O loop vai continuar enquanto o contador for menor ou igual a 5
    print(f"Contagem: {contador}")
    contador += 1  # Incrementamos o contador em 1 a cada iteração
# Quando o contador chegar a 6, a condição (contador <= 5) será falsa, e o loop vai parar

print("-" * 50)

# Exemplo 2: Solicitando entrada do usuário até ele digitar um valor válido
# Vamos usar um loop while para garantir que o usuário insira um número válido

while True:  # Criamos um loop infinito, que só vai parar se o usuário digitar um número correto
    entrada = input("Digite um número inteiro: ")
    try:
        numero = int(entrada)  # Tentamos converter a entrada para inteiro
        print(f"Você digitou o número {numero}.")
        break  # Se a conversão for bem-sucedida, o loop é interrompido com o comando break
    except ValueError:
        # Se a conversão falhar, o except captura o erro e pede para o usuário tentar novamente
        print("Entrada inválida, tente novamente.")

print("-" * 50)

# Exemplo 3: Verificando senha com loop while
# Vamos criar um sistema de verificação de senha simples, onde o usuário tem 3 tentativas para acertar a senha

senha_correta = "1234"
tentativas = 0
max_tentativas = 3

while tentativas < max_tentativas:
    senha = input("Digite a sua senha: ")
    if senha == senha_correta:
        print("Senha correta! Acesso permitido.")
        break  # Interrompemos o loop se a senha estiver correta
    else:
        tentativas += 1  # Contamos o número de tentativas erradas
        print(f"Senha incorreta. Você tem {max_tentativas - tentativas} tentativas restantes.")
else:
    # O else do while só executa se o loop terminar sem o break, ou seja, se as tentativas se esgotarem
    print("Número máximo de tentativas atingido. Acesso bloqueado.")

print("-" * 50)

# Exemplo 4: Usando continue para ignorar certas iterações
# Vamos usar o continue para ignorar os números ímpares e mostrar apenas os números pares até 10

numero = 0
while numero < 10:
    numero += 1
    if numero % 2 != 0:
        continue  # Se o número for ímpar, o continue ignora o restante do loop e passa para a próxima iteração
    print(f"Número par: {numero}")

print("-" * 50)

# Exemplo 5: Loop infinito com condição de parada (usando break)
# Vamos criar um loop infinito que só para quando o usuário digitar "sair"

while True:
    comando = input("Digite um comando ('sair' para encerrar): ").lower()
    if comando == "sair":
        print("Encerrando o programa.")
        break  # O loop para quando o usuário digita "sair"
    else:
        print(f"Você digitou: {comando}")

print("-" * 50)

# Exemplo 6: Contador decrescente (usando while para contagem regressiva)
# Vamos contar de 10 até 1 usando um loop while

contador = 10
while contador > 0:  # O loop vai rodar enquanto o contador for maior que 0
    print(f"Contagem regressiva: {contador}")
    contador -= 1  # Decrementamos o contador a cada iteração
print("Contagem finalizada!")

print("-" * 50)

# Exemplo 7: Soma de números usando loop while
# O usuário pode continuar digitando números, e o programa soma esses números até ele digitar 0

soma = 0
while True:
    numero = int(input("Digite um número para somar (ou 0 para sair): "))
    if numero == 0:
        break  # O loop para se o número for 0
    soma += numero  # Adiciona o número à soma total
print(f"A soma total é {soma}")
