# INTEIROS

# Declaração de uma variável inteira (número sem casas decimais)
numero_inteiro = 3
# Exibe o valor da variável inteira
print("Inteiro =", numero_inteiro)

# REAL COM PONTO FLUTUANTE

# Declaração de uma variável de número real (float), que inclui casas decimais
numero_real = 3.14
# Exibe o valor da variável real (com ponto flutuante)
print("Real com ponto flutuante =", numero_real)

# type()

# Usa a função type() para mostrar o tipo da variável 'numero_inteiro' (que será <class 'int'>)
print("Tipo da variável inteiro =", type(numero_inteiro))

# Usa a função type() para mostrar o tipo da variável 'numero_real' (que será <class 'float'>)
print("Tipo da variável real =", type(numero_real))

# SOMA +

# Realiza a soma de dois números inteiros (1 + 9) e armazena na variável 'soma'
soma = 1 + 9
# Exibe o resultado da soma
print('A soma de 1 + 9 é igual a', soma)

# SUBTRAÇÃO -

# Realiza a subtração de dois números inteiros (9 - 1) e armazena na variável 'subritação' (correção: subtração)
subritação = 9 - 1
# Exibe o resultado da subtração
print('A subtração de 9 - 1 é igual a', subritação)

# DIVISÃO /

# Realiza a divisão de dois números (9 / 9), o resultado é um número float
divisao = 9 / 9
# Exibe o resultado da divisão
print('A divisão de 9 / 9 é igual a', divisao)

# Exibe o tipo da variável 'divisao' (que será <class 'float'> porque a divisão resulta em um número decimal)
print("Tipo da variável divisao =", type(divisao))

# Converte a variável 'divisao' para inteiro (o número é truncado, ou seja, as casas decimais são removidas)
print("Tipo da variável divisao em inteiro =", int(divisao))

# MULTIPLICAÇÃO *

# Realiza a multiplicação de dois números inteiros (5 * 9)
multiplicação = 5 * 9
# Exibe o resultado da multiplicação
print('A multiplicação de 5 * 9 é igual a', multiplicação)

# Converte o resultado da multiplicação para float e exibe o valor (mesmo resultado, mas agora com ponto flutuante)
print("Tipo da variável multiplicação em float =", float(multiplicação))

# MÓDULO %

# Realiza a operação de módulo (resto da divisão de 5 por 2) e armazena o resultado na variável 'modulo'
modulo = 5 % 2
# Exibe o resultado da operação de módulo (que será 1, porque 5 dividido por 2 tem resto 1)
print('O módulo de 5 % 2 é igual a', modulo)
