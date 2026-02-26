class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        print('-' * 30)
        print(f'{self.nome}'.center(30))
        print(f'R${self.preco:,.2f}'.center(30))
        print('-' * 30)

p1 = Produto('iPhone 15 Pro', 5000)
p1.etiqueta()

p2 = Produto('Notebook Gamer', 11000)
p2.etiqueta()