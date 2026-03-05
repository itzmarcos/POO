#
class Caneta:
    def __init__(self, cor):
        self.cor = cor

    def destampar(self):
        pass

    def escrever(self, cor):
        if self.cor == 'Azul' or 'Vermelho' or 'Verde':
            print(f'\033[36m{cor}\033[m \033[31m{cor}\033[m {cor}')

c1 = Caneta('Azul')
c2 = Caneta('Vermelho')
c3 = Caneta('Verde')

c1.escrever('Olá, tudo bem?')
c2.escrever('Olá, Gafanhoto!')
c3.escrever('Vamos exercitar!')


# if self.cor == 'Azul':
#         print(f'\033[36m{cor}\033[m')
# if self.cor == 'Vermelho':
#         print(f'\033[31m{cor}\033[m')
# if self.cor == 'Verde':
#         print(f'\033[32m{cor}\033[m')