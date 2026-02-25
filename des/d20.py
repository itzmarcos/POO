class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick

    def favoritos(self, jogo):
        lista = []
        lista.append(jogo)

    def ficha(self):
        print(f'Jogador {self.nick}')
        print(f'Nome real: {self.nome}')
        
j1 = Gamer('Antonia Luana', 'Peach')
j1.favoritos('LOL')
j1.favoritos('Tibia')
j1.ficha()