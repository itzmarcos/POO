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
            print(f'Pág{self.valor+2} ->', end=' ', flush=True)
            self.valor += 1
        print(f'\033[32mVoce avançou {quant} paginas e agora esta na\033[m \033[34mpagina {self.valor+1}\033[m')  
            
        
l1 = Livro('Batalha do Apocalipse', 20)
l1.avancar(5)
l1.avancar(10)
l1.avancar(6)