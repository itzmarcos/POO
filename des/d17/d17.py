class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f'Voce comprou um {self.nome}, pelo o valor de R${self.preco:,.2f}'

p1 = Produto('iPhone 15 Pro', 25000)
print(p1)