#Exemplo de herança
print("\nExemplo de herança:")
class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome
    
    def andar(self):
        print(f"O animal {self.nome} andou")
        return
    def emetir_som(self):
        pass

class Cachorro(Animal):
    def emetir_som(self):
        return "Au, au"
    
class Gato(Animal):
    def emetir_som(self):
        return "Miau! ,miau!"
    
dog = Cachorro(nome="Rex")
cat = Gato(nome="Felix")

print("\nExemplo de polimorfismo")
animais = [dog, cat]

for Animal in animais:
    print(f"{Animal.nome} faz: {Animal.emetir_som()}")

print("\n Exemplo de encapsulamento:")
class ContaBancaria:
    def __init__(self, saldo) -> None:
        self.__saldo = saldo  # Atributo privado
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor  # Acessa o atributo privado corretamente
    
    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:  # Acessa o atributo privado corretamente
            self.__saldo -= valor
    
    def consultar_saldo(self):
        return self.__saldo  # Acessa o atributo privado corretamente

conta = ContaBancaria(saldo=1000)
print(f"Saldo da conta Bancaria: {conta.consultar_saldo()}")
conta.depositar(valor=500)
print(f"Saldo da conta Bancaria: {conta.consultar_saldo()}")
conta.depositar(valor=-500)
print(f"Saldo da conta Bancaria: {conta.consultar_saldo()}")
conta.sacar(valor=200)
print(f"Saldo da conta Bancaria: {conta.consultar_saldo()}")


print("\nExemplo de abstração:")
from abc import ABC,abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def ligar(self):
        pass
    @abstractmethod
    def desligar(self):
        pass
class Carro(Veiculo):
    def __init__(self) -> None:
        pass
    def ligar(self):
        return print("Carro ligado usando a chave")
    def desligar(self):
        return print("Carro desligado usando a chave")

carro_amarelo = Carro()
print(carro_amarelo.ligar())
print(carro_amarelo.desligar())