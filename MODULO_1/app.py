# Importando o módulo correto
import meu_modulo

# Usando a função saudacao() do módulo
nome = input("Digite seu nome: ")
print(meu_modulo.saudacao(nome))

# Usando a função soma() do módulo
print(f"A soma de 10 e 5 é: {meu_modulo.soma(10, 5)}")

# Usando a função multiplicar() do módulo
print(f"Multiplicação de 3 e 4 é: {meu_modulo.multiplicar(3, 4)}")

# Usando a função subtrair() do módulo
print(f"Subtração de 15 e 7 é: {meu_modulo.subtrair(15, 7)}")

# Usando a constante PI e a função area_circulo()
raio = float(input("Digite o raio de um círculo: "))
print(f"A área do círculo com raio {raio} é: {meu_modulo.area_circulo(raio)}")

# Usando a função mensagem() do módulo
meu_modulo.mensagem()
