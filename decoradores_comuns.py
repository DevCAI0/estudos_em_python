# Exemplo completo decoradores_comuns.py

# Exemplo 1: Decorador simples que adiciona mensagens antes e depois de executar a função

def decorador_simples(funcao):
    """
    Este é um decorador simples que adiciona uma mensagem antes e depois
    de chamar a função original.
    """
    def wrapper(*args, **kwargs):
        print("Executando antes da função...")
        resultado = funcao(*args, **kwargs)
        print("Executando após a função...")
        return resultado
    return wrapper

# Exemplo 2: @staticmethod e @classmethod em ação

class Pessoa:
    populacao = 0  # Atributo da classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        Pessoa.populacao += 1  # Incrementa a população a cada nova instância

    @classmethod
    def obter_populacao(cls):
        """
        Este é um método de classe que acessa diretamente os atributos da classe (cls).
        """
        return f"População atual: {cls.populacao}"

    @staticmethod
    def e_maior_idade(idade):
        """
        Este é um método estático que não interage com a classe ou com instâncias,
        ele apenas realiza uma operação que está relacionada à classe.
        """
        return idade >= 18

# Testando o @classmethod e @staticmethod
print(Pessoa.obter_populacao())  # População inicial
p1 = Pessoa("Caio", 24)
p2 = Pessoa("Ana", 17)
print(Pessoa.obter_populacao())  # População após adicionar pessoas

# Verificando se alguém é maior de idade usando o método estático
print(f"Ana é maior de idade? {Pessoa.e_maior_idade(17)}")
print(f"Caio é maior de idade? {Pessoa.e_maior_idade(24)}")

print("-" * 50)

# Exemplo 3: Decorador para medir o tempo de execução de uma função

import time

def medir_tempo(funcao):
    """
    Este decorador mede o tempo de execução da função decorada.
    """
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcao(*args, **kwargs)
        fim = time.time()
        print(f"Tempo de execução: {fim - inicio:.4f} segundos.")
        return resultado
    return wrapper

# Aplicando o decorador medir_tempo
@medir_tempo
def tarefa_demorada():
    """
    Função que simula uma tarefa que demora 2 segundos.
    """
    print("Iniciando uma tarefa demorada...")
    time.sleep(2)
    print("Tarefa concluída.")

# Chamando a função decorada
tarefa_demorada()

print("-" * 50)

# Exemplo 4: Decorador para verificar permissões de usuário

def verificar_permissoes(funcao):
    """
    Este decorador verifica se o usuário tem permissões antes de executar a função.
    """
    def wrapper(*args, **kwargs):
        usuario = kwargs.get('usuario')
        if usuario and usuario.get('admin'):
            print("Permissão concedida.")
            return funcao(*args, **kwargs)
        else:
            print("Permissão negada. Você não tem acesso.")
            return None
    return wrapper

# Função decorada que exige permissões de administrador
@verificar_permissoes
def deletar_usuario(usuario):
    print(f"Usuário {usuario['nome']} deletado com sucesso!")

# Testando o decorador de permissões
deletar_usuario(usuario={"nome": "Caio", "admin": True})  # Usuário admin
deletar_usuario(usuario={"nome": "Ana", "admin": False})  # Usuário sem permissões

print("-" * 50)

# Exemplo 5: Decorador para registrar a chamada de uma função

def logar_chamada(funcao):
    """
    Decorador que registra a chamada de uma função, incluindo argumentos e retorno.
    """
    def wrapper(*args, **kwargs):
        print(f"Chamando a função {funcao.__name__} com os argumentos: {args}, {kwargs}")
        resultado = funcao(*args, **kwargs)
        print(f"Função {funcao.__name__} retornou: {resultado}")
        return resultado
    return wrapper

# Função decorada para registrar chamadas
@logar_chamada
def somar(a, b):
    return a + b

# Chamando a função decorada
resultado_soma = somar(10, 20)

print("-" * 50)

# Exemplo 6: Decorador com argumentos (parâmetros para o decorador)

def repetir_vezes(n):
    """
    Decorador que repete a execução da função decorada 'n' vezes.
    """
    def decorador(funcao):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                funcao(*args, **kwargs)
        return wrapper
    return decorador

# Aplicando o decorador com argumento (n = 3)
@repetir_vezes(3)
def diga_oi():
    print("Oi!")

# Chamando a função decorada
diga_oi()

print("-" * 50)

# Exemplo 7: Decoradores aninhados

@logar_chamada
@medir_tempo
def multiplicar(a, b):
    time.sleep(1)  # Simulando operação lenta
    return a * b

# Chamando a função com dois decoradores
resultado_multiplicacao = multiplicar(4, 5)

print("-" * 50)

# Exemplo 8: Decorador que substitui o retorno de uma função

def substituir_retorno(funcao):
    """
    Este decorador modifica o retorno da função original para sempre retornar "Substituído!".
    """
    def wrapper(*args, **kwargs):
        funcao(*args, **kwargs)
        return "Substituído!"
    return wrapper

# Função decorada que terá seu retorno substituído
@substituir_retorno
def exibir_mensagem():
    print("Esta é a mensagem original.")

# Chamando a função decorada
resultado_mensagem = exibir_mensagem()
print(f"Resultado da função: {resultado_mensagem}")
