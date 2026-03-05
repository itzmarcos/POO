class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.jogo = []
        
    def favoritos(self, jogo):     
        self.jogo.append(jogo)

    def ficha(self):
        print('-' * 25)
        print(f'Jogador: \033[33m{self.nick}\033[m')
        print(f'Nome Real: \033[32m{self.nome}\033[m')
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

j2 = Gamer('Leon Kennedy', 'L requeim')
j2.favoritos('Dota 2')
j2.favoritos('CS:GO')
j2.favoritos('Call of Duty')
j2.favoritos('PUBG')
j2.ficha()