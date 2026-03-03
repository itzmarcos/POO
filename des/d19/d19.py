class Livro:
    from time import sleep
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.valor = 0
        print(f'\033[30mVocê acabou de abrir o livro: {self.titulo} que contem {self.paginas} paginas no total.\nVocê agora esta na\033[m\033[34m pagina 1\033[m')

    def avancar(self, quant):                   
        for _ in range(quant):
            if self.valor + 1 >= self.paginas:
                print('\n\033[31mVocê chegou ao final do livro!\033[m')
                break
            
            self.sleep(0.5)
            print(f'Pág{self.valor+2} ->', end=' ', flush=True)
            self.valor += 1
        
        print(f'\n\033[32mAgora você está na\033[m \033[34mpagina {self.valor+1}\033[m')
            
        
l1 = Livro('Batalha do Apocalipse', 20)
l1.avancar(5)
l1.avancar(4)
l1.avancar(100)