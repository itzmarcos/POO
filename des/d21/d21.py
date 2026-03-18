#
class Caneta:
    cores = {
        'Azul': '\033[36m',
        'Vermelho': '\033[31m',
        'Verde': '\033[32m'
    }

    def __init__(self, cor):
        self.cor = cor
        self.usar_cor = True

    def escrever(self, frase):
        palavras = frase.split()
        for palavra in palavras:
            print(f"{Caneta.cores[self.cor]}{palavra}\033[m", end=' ')  

    def destampar(self):
        if self.escrever != Caneta.cores['Azul']:
            print('Ativado')
        else:
            print('Desativada')




    

c1 = Caneta('Azul')
c2 = Caneta('Vermelho')
c3 = Caneta('Verde')




c1.escrever('Olá')
c2.escrever('Mundo')
c3.escrever('Tudo bem?')



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