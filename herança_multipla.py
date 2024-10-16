class Animal :
    def __init__(self, nome) -> None:
        self.nome = nome
    def emetir_som(self):
        pass

class Mamifero(Animal):
    def amamentar(self):
        return f"{self.nome} esta amamentando"
class Ave(Animal):
    def voar(self):
        return f"{self.nome} esta voando"
    
class Morcego(Mamifero,Ave):
    def emetir_som(self):
        return   "Morcegos emitem sons ultrassônicos"
    

morcego = Morcego(nome="Batman")
# Acessando metodos sa classebase Animal
print("Nome do morcego:", morcego.nome)
print("Som do morcego", morcego.emetir_som())

#acessando classes dos metodos Mamifero e ave

print("Morcego amamentando:" , morcego.amamentar())
print("Morcego voando:",morcego.voar())