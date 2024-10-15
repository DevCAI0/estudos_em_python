# meu_modulo.py

def saudacao(nome):
    """
    Retorna uma saudação personalizada para o nome dado.
    """
    return f"Olá, {nome}! Bem-vindo ao mundo dos módulos em Python!"

def soma(a, b):
    """
    Retorna a soma de dois números.
    """
    return a + b

def multiplicar(a, b):
    """
    Retorna o produto de dois números.
    """
    return a * b

def subtrair(a, b):
    """
    Retorna a subtração de dois números.
    """
    return a - b

PI = 3.14159265359  # Constante Pi que pode ser usada em cálculos matemáticos

# Função que calcula a área de um círculo
def area_circulo(raio):
    """
    Calcula a área de um círculo dado o raio.
    """
    return PI * (raio ** 2)

# Função que exibe uma mensagem simples
def mensagem():
    """
    Exibe uma mensagem de exemplo.
    """
    print("Essa mensagem vem do meu_modulo!")
