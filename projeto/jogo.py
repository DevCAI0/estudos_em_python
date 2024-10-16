# Persongem: classe mãe
# heroi: controlado pelo usuário
# Inimigo: adversário do usuário

class Personagem: 
    def __init__(self, nome, vida, nivel) -> None:
        self._nome = nome
        self.vida = vida
        self._nivel = nivel

    # Métodos getter que retornam os valores dos atributos
    def get_nome(self):
        return self._nome
    
    def get_vida(self):
        return self.vida
    
    def get_nivel(self):
        return self._nivel

    def exibir_detalhes(self):
        return f"Nome: {self.get_nome()} \nVida: {self.get_vida()} \nNível: {self.get_nivel()}"

class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade) -> None:
        super().__init__(nome, vida, nivel)
        self._habilidade = habilidade

    def get_habilidade(self):
        return self._habilidade

    # Sobrescrevemos o método exibir_detalhes para incluir a habilidade do herói
    def exibir_detalhes(self):
        detalhes_base = super().exibir_detalhes()  # Detalhes herdados da classe Personagem
        return f"{detalhes_base}\nHabilidade: {self.get_habilidade()}"

class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo) -> None:
        super().__init__(nome, vida, nivel)
        self._tipo = tipo

    def get_tipo(self):
        return self._tipo

    # Sobrescrevemos o método exibir_detalhes para incluir o tipo do inimigo
    def exibir_detalhes(self):
        detalhes_base = super().exibir_detalhes()  # Detalhes herdados da classe Personagem
        return f"{detalhes_base}\nTipo: {self.get_tipo()} (Quadrinhos)"  # Adicionando tipo como "Quadrinhos"



class Jogo:
    """Classe orquestradora do jogo"""

    def __init__(self) -> None:
        # Inicializando o herói e o inimigo
        self.heroi = Heroi(nome="Hulk", vida=1000, nivel=100, habilidade="Hulk Esmaga")
        self.inimigo = Inimigo(nome="Thanos", vida=8000, nivel=100, tipo="Deus da destruição")

    def iniciar_batalha(self):
        """Gerencia a batalha em turnos entre herói e inimigo"""
        print("Iniciando Batalha!")
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            # Exibindo os detalhes do herói
            print("Detalhes do Herói:")
            print(self.heroi.exibir_detalhes())

            print("-" * 50)

            # Exibindo os detalhes do inimigo
            print("Detalhes do Inimigo:")
            print(self.inimigo.exibir_detalhes())

            input("Pressione Enter para atacar...")

            # Escolha do tipo de ataque
            escolha = input("Escolha 1 - Ataque normal, 2 - Ataque Especial: ")

            # Ataque normal
            if escolha == "1":
                print(f"{self.heroi.get_nome()} ataca {self.inimigo.get_nome()} com ataque normal!")
                dano = 100  # Exemplo de dano normal
                self.inimigo.vida -= dano
                print(f"{self.inimigo.get_nome()} perde {dano} pontos de vida!")
            
            # Ataque especial
            elif escolha == "2":
                print(f"{self.heroi.get_nome()} usa {self.heroi.get_habilidade()}!")
                dano = 300  # Exemplo de dano especial
                self.inimigo.vida -= dano
                print(f"{self.inimigo.get_nome()} perde {dano} pontos de vida!")

            else:
                print("Escolha inválida! Você perdeu a vez.")

            # Inimigo contra-ataca se ainda estiver vivo
            if self.inimigo.get_vida() > 0:
                print(f"{self.inimigo.get_nome()} contra-ataca!")
                dano_inimigo = 200  # Exemplo de dano do inimigo
                self.heroi.vida -= dano_inimigo
                print(f"{self.heroi.get_nome()} perde {dano_inimigo} pontos de vida!")

            print("=" * 50)

        # Verificando o resultado final da batalha
        if self.heroi.get_vida() > 0:
            print(f"{self.heroi.get_nome()} venceu a batalha!")
        else:
            print(f"{self.inimigo.get_nome()} venceu a batalha!")

# Iniciar o jogo
jogo = Jogo()
jogo.iniciar_batalha()




















