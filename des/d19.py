class Livro:
    from time import sleep
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        print(f'Você acabou de abrir o livro: {self.titulo} que contem {self.paginas} paginas no total.\nVocê agora esta na pagina 1')
    def avancar(self, valor):
        inicio = 1
        inicio += valor
        for c in range(1, valor+1):
            self.sleep(0.5)
            print(f'Pág{c} ->', end=' ', flush=True)
        print(f'Voce avançou {valor} paginas e agora esta na pagina {c}')
    

l1 = Livro('Batalha do Apocalipse', 20)
l1.avancar(2)
l1.avancar(10)