class Livro:
    from time import sleep
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.valor = 0
        # print(f'Você acabou de abrir o livro: {self.titulo} que contem {self.paginas} paginas no total.\nVocê agora esta na pagina 1')
    def avancar(self, quant):       
        for _ in range(quant):
            self.sleep(0.5)
            print(f'Pág{self.valor+1} ->', end=' ', flush=True)
            self.valor += 1
        print(f'Voce avançou {self.valor} paginas e agora esta na pagina {self.valor}')
        if self.valor > quant:
            print('Voce atigiu o limite de pagina do livro')


l1 = Livro('Batalha do Apocalipse', 10)
l1.avancar(3)
l1.avancar(15)