# POO

# Classe example 

class Pessoa: 
    def __init__(self, nome,idade) -> None:
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos"
# Objetos

Pessoa1 = Pessoa("joao", 30)
mensagem = Pessoa1.saudacao()

print("Nome",Pessoa1.nome)
print("Idade",Pessoa1.idade)
print(mensagem)
