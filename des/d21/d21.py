
class Caneta:
    def __init__(self, cor = 'azul'):
        escolha = ''
        match cor.lower().strip():
            case 'azul':
                escolha = "\033[36m"
            case "vermelho" | "vermelha":
                escolha = "\033[31m"
            case "verde":
                escolha = "\033[32m"
            case _:
                escolha = "\033[30m"
        self.cor = escolha
        self.tampada = True
    def escrever(self, msg):
        if self.tampada:
            print('A Caneta esta tampada!')
        else:
            print(f"{self.cor}{msg}\033[m", end=' ')

    def pular_linha(self, qtd = 0):
        print(f'\n' * qtd, end='')

    def tampar(self):
        self.tampada = True

    def destampar(self):
        self.tampada = False

c1 = Caneta('azul')
c2 = Caneta('vermelha')
c3 = Caneta('verde')

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever('Hello')
c1.pular_linha(2)
c2.escrever('World')
c3.escrever('thanks')