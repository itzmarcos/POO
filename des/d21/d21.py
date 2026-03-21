#
class Caneta:
    def __init__(self, cor):
        self.cor = cor
        self.cores = []
        
    def destampar(self):
        self.cores = {
            'Azul': '\033[36m',
            'Vermelho': '\033[31m',
            'Verde': '\033[32m'
        }
        try:
            if self.cor == 'Azul':
              return '\033[36m'
            if self.cor == 'Vermelho':
              return '\033[31m'
            if self.cor == 'Verde':
              return '\033[32m'
        except:
           print('Caneta azul tampanda')
        
    def escrever(self, frase):
        palavras = frase.split()
        for palavra in palavras:
            print(f"{palavra}\033[m", end=' ')

c1 = Caneta('Azul')
c2 = Caneta('Vermelho')
c3 = Caneta('Verde')

c1.destampar()

c1.escrever('A')
c2.escrever('B')
c3.escrever('C')



# class Caneta:
#     cores = {
#         'Azul': '\033[36m',
#         'Vermelho': '\033[31m',
#         'Verde': '\033[32m'
#     }

#     def __init__(self, cor):
#         self.cor = cor

#     def escrever(self, frase):
#         palavras = frase.split()
#         for palavra in palavras:
#             print(f"{Caneta.cores[self.cor]}{palavra}\033[m", end=' ')  

#     def destampar(self):
#         pass


    

# c1 = Caneta('Azul')
# c2 = Caneta('Vermelho')
# c3 = Caneta('Verde')

# c1.escrever('Olá')
# c2.escrever('Mundo')
# c3.escrever('Tudo bem?')