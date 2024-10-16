# Exemplo básico de exceções em Python

def dividir(val1, val2):
    """
    Função que divide dois números, com tratamento de exceções.
    """
    try:
        resultado = val1 / val2
    except ZeroDivisionError:  # Captura divisão por zero
        print("Erro: Não é possível dividir por zero.")
        return None
    except TypeError:  # Captura se os valores não forem números
        print("Erro: Ambos os valores devem ser números.")
        return None
    else:
        print(f"Divisão realizada com sucesso: {resultado}")
        return resultado
    finally:
        print("A operação de divisão foi concluída, com ou sem erro.")

# Testando a função dividir
dividir(10, 2)  # Exemplo válido
dividir(10, 0)  # Exemplo de divisão por zero
dividir(10, "a")  # Exemplo de erro de tipo

print("\n" + "-"*50 + "\n")

# Exemplo de exceção personalizada

class ValorNegativoError(Exception):
    """
    Exceção personalizada que será lançada quando um valor negativo for encontrado.
    """
    pass

def verificar_positivo(numero):
    """
    Função que verifica se um número é positivo. Lança uma exceção personalizada se o valor for negativo.
    """
    if numero < 0:
        raise ValorNegativoError(f"Erro: {numero} é um valor negativo!")
    else:
        print(f"O valor {numero} é positivo.")

# Testando a exceção personalizada
try:
    verificar_positivo(5)  # Número positivo, deve passar
    verificar_positivo(-3)  # Número negativo, deve lançar a exceção
except ValorNegativoError as e:
    print(e)

print("\n" + "-"*50 + "\n")

# Exemplo de múltiplas exceções

def pegar_elemento(lista, indice):
    """
    Função que tenta acessar um elemento de uma lista em um índice específico.
    Lida com exceções de índice fora do intervalo e tipo de dado incorreto.
    """
    try:
        elemento = lista[indice]
    except IndexError:  # Captura erro de índice fora do intervalo
        print(f"Erro: O índice {indice} está fora do intervalo.")
    except TypeError:  # Captura erro de tipo de dado incorreto
        print("Erro: O índice deve ser um número inteiro.")
    else:
        print(f"Elemento encontrado: {elemento}")

# Testando a função pegar_elemento
pegar_elemento([1, 2, 3], 1)  # Exemplo válido
pegar_elemento([1, 2, 3], 5)  # Índice fora do intervalo
pegar_elemento([1, 2, 3], "a")  # Índice inválido (não inteiro)

print("\n" + "-"*50 + "\n")

# Exemplo de 'finally' para limpar recursos

def abrir_arquivo(nome_arquivo):
    """
    Função que abre um arquivo para leitura e garante que ele será fechado, independentemente de erros.
    """
    try:
        arquivo = open(nome_arquivo, "r")
        print("Arquivo aberto com sucesso.")
        # Leitura do arquivo (não executado, apenas exemplo)
        conteudo = arquivo.read()
    except FileNotFoundError:  # Arquivo não encontrado
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    finally:
        try:
            arquivo.close()
            print("Arquivo fechado.")
        except NameError:  # Caso o arquivo não tenha sido aberto
            print("Nenhum arquivo foi aberto, então não há o que fechar.")

# Testando a função abrir_arquivo
abrir_arquivo("exemplo.txt")  # Arquivo inexistente
