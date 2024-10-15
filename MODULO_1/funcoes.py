# # Definindo uma lista de tarefas global para ser acessada pelas funções
# tarefas = []

# # Função para adicionar uma nova tarefa
# def adicionar_tarefa():
#     tarefa = input("Digite o nome da tarefa a ser adicionada: ")
#     tarefas.append({"nome": tarefa, "completa": False})
#     print(f"Tarefa '{tarefa}' adicionada com sucesso!")

# # Função para ver todas as tarefas
# def ver_tarefas():
#     if not tarefas:
#         print("Não há tarefas na lista.")
#         return
    
#     print("\nLista de tarefas:")
#     for index, tarefa in enumerate(tarefas):
#         status = "✔️" if tarefa["completa"] else "❌"
#         print(f"{index + 1}. {tarefa['nome']} - {status}")

# # Função para atualizar uma tarefa existente
# def atualizar_tarefa():
#     ver_tarefas()  # Mostra as tarefas atuais
#     try:
#         indice = int(input("Digite o número da tarefa que deseja atualizar: ")) - 1
#         nova_tarefa = input("Digite o novo nome da tarefa: ")
#         tarefas[indice]["nome"] = nova_tarefa
#         print("Tarefa atualizada com sucesso!")
#     except (ValueError, IndexError):
#         print("Entrada inválida ou tarefa não encontrada.")

# # Função para marcar uma tarefa como completa
# def completar_tarefa():
#     ver_tarefas()  # Mostra as tarefas atuais
#     try:
#         indice = int(input("Digite o número da tarefa que deseja marcar como completa: ")) - 1
#         tarefas[indice]["completa"] = True
#         print("Tarefa marcada como completa!")
#     except (ValueError, IndexError):
#         print("Entrada inválida ou tarefa não encontrada.")

# # Função para deletar todas as tarefas que foram completadas
# def deletar_completadas():
#     global tarefas
#     tarefas = [tarefa for tarefa in tarefas if not tarefa["completa"]]
#     print("Todas as tarefas completadas foram deletadas.")

# # Função principal do menu
# def mostrar_menu():
#     print("\nMenu de Gerenciamento de Lista de Tarefas:")
#     print("1. Adicionar tarefa")
#     print("2. Ver tarefas")
#     print("3. Atualizar tarefa")
#     print("4. Completar tarefa")
#     print("5. Deletar tarefas completadas")
#     print("6. Sair")

# # Função para executar o menu
# def gerenciar_tarefas():
#     while True:
#         mostrar_menu()  # Mostra o menu para o usuário
#         escolha = input("Digite um número do Menu: ")

#         # Verifica a escolha do usuário e chama a função correspondente
#         if escolha == "1":
#             adicionar_tarefa()
#         elif escolha == "2":
#             ver_tarefas()
#         elif escolha == "3":
#             atualizar_tarefa()
#         elif escolha == "4":
#             completar_tarefa()
#         elif escolha == "5":
#             deletar_completadas()
#         elif escolha == "6":
#             print("Programa finalizado.")
#             break  # Sai do loop e encerra o programa
#         else:
#             print("Opção inválida. Tente novamente.")

#         print("-" * 50)  # Separador visual para o próximo ciclo

# # Inicia o programa chamando a função principal
# gerenciar_tarefas()

# Exemplo 1: Função simples sem parâmetros e sem retorno
# Esta função apenas imprime uma saudação

def saudacao(nome):
    print(f"Olá! Bem-vindo ao nosso programa, {nome}")

# Chamamos a função para que ela execute sua tarefa
saudacao("CAIO")

print("-" * 50)

# Exemplo 2: Função com parâmetros
# Esta função recebe dois números como entrada e imprime a soma deles

def somar(num1, num2):
    soma = num1 + num2
    print(f"A soma de {num1} e {num2} é {soma}.")

# Chamamos a função passando dois valores como argumentos
somar(5, 10)

print("-" * 50)

# Exemplo 3: Função com retorno de valor
# Esta função recebe dois números e retorna a multiplicação deles

def multiplicar(a, b):
    return a * b

# Armazenamos o valor retornado pela função em uma variável e imprimimos
resultado = multiplicar(4, 5)
print(f"O resultado da multiplicação é {resultado}.")

print("-" * 50)

# Exemplo 4: Função com valor padrão para parâmetros
# Esta função retorna a área de um retângulo, e se o usuário não fornecer valores, usamos valores padrão

def calcular_area_retangulo(largura=1, altura=1):
    return largura * altura

# Chamando a função com argumentos personalizados
print(f"A área do retângulo é {calcular_area_retangulo(5, 10)}.")

# Chamando a função sem fornecer argumentos, que usará os valores padrão
print(f"A área do retângulo (padrão) é {calcular_area_retangulo()}.")

print("-" * 50)

# Exemplo 5: Função com múltiplos retornos
# Esta função retorna o quadrado e o cubo de um número

def calcular_potencias(numero):
    quadrado = numero ** 2
    cubo = numero ** 3
    return quadrado, cubo

# Recebemos os múltiplos valores retornados pela função
q, c = calcular_potencias(3)
print(f"O quadrado de 3 é {q} e o cubo é {c}.")

print("-" * 50)

# Exemplo 6: Função com número variável de parâmetros (*args)
# Esta função recebe qualquer quantidade de números e retorna a soma

def somar_todos(*numeros):
    return sum(numeros)

# Chamando a função com diferentes números de argumentos
print(f"A soma de 1, 2, 3 é {somar_todos(1, 2, 3)}.")
print(f"A soma de 4, 5, 6, 7, 8 é {somar_todos(4, 5, 6, 7, 8)}.")

print("-" * 50)

# Exemplo 7: Função com parâmetros nomeados (**kwargs)
# Esta função recebe parâmetros nomeados e imprime o nome e valor de cada um

def imprimir_informacoes(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

# Chamando a função passando argumentos nomeados
imprimir_informacoes(nome="Caio", idade=24, profissao="Desenvolvedor")

print("-" * 50)

# Exemplo 8: Função recursiva
# Esta função usa recursão para calcular o fatorial de um número

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

# Chamamos a função recursiva para calcular o fatorial de 5
print(f"O fatorial de 5 é {fatorial(5)}.")

print("-" * 50)

# Exemplo 9: Função como argumento para outra função (funções de primeira classe)
# Esta função recebe outra função como argumento e aplica essa função a um número

def aplicar_funcao(funcao, valor):
    return funcao(valor)

# Definimos uma função que eleva um número ao quadrado
def quadrado(x):
    return x ** 2

# Passamos a função quadrado como argumento para aplicar_funcao
print(f"O quadrado de 6 é {aplicar_funcao(quadrado, 6)}.")

print("-" * 50)

# Exemplo 10: Função lambda (função anônima)
# Criamos uma função lambda para somar dois números

soma_lambda = lambda x, y: x + y
print(f"A soma de 7 e 8 usando uma função lambda é {soma_lambda(7, 8)}.")

print("-" * 50)

# Exemplo 11: Função com docstring
# Adicionamos uma docstring para documentar a função

def calcular_media(nota1, nota2):
    """
    Esta função recebe duas notas e retorna a média entre elas.
    :param nota1: primeira nota (float)
    :param nota2: segunda nota (float)
    :return: média das notas (float)
    """
    return (nota1 + nota2) / 2

# Usando a função help() para exibir a documentação da função
help(calcular_media)

print("-" * 50)

# Exemplo 12: Função interna (função dentro de outra função)
# Uma função interna só pode ser usada dentro da função que a contém

def funcao_externa():
    print("Esta é a função externa.")

    def funcao_interna():
        print("Esta é a função interna.")

    # Chamando a função interna dentro da função externa
    funcao_interna()

# Chamamos a função externa, que chama a função interna
funcao_externa()

print("-" * 50)

# Exemplo 13: Função com tratamento de erros (try/except)
# Esta função tenta dividir dois números e lida com a divisão por zero

def dividir(numerador, denominador):
    try:
        resultado = numerador / denominador
    except ZeroDivisionError:
        return "Erro: Divisão por zero não é permitida."
    else:
        return resultado

# Chamamos a função e tratamos possíveis erros
print(f"A divisão de 10 por 2 é {dividir(10, 2)}.")
print(f"A tentativa de dividir 10 por 0 resultou em: {dividir(10, 0)}.")
