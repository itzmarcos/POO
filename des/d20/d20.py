class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.jogo = []
        
    def favoritos(self, jogo):     
        self.jogo.append(jogo)

    def ficha(self):
        print('-' * 25)
        print(f'Jogador: {self.nick}')
        print(f'Nome Real: {self.nome}')
        print('-' * 25)
        for item in sorted(self.jogo):
            print(item)
        print('-' * 25)

j1 = Gamer('Luana Cavalaro', 'Qtc')
j1.favoritos('League of Legends')
j1.favoritos('Tibia')
j1.favoritos('World of Warcraft')
j1.favoritos('Perfect World')
j1.ficha()