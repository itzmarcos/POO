class Churrasco:
    """
    CONSIDERE:
    Consumo padrão: 400g por pessoa
    preço: R$82,40/kg
    """
    def __init__(self, titulo, quant):
        self.titulo = titulo
        self.quant = quant
        self.consumo = 0.4
        self.preco = 82.40

    def analisador(self):
        valor = self.consumo * self.quant
        total_valor = valor * self.preco
        divisao = total_valor / self.quant
        return f'Analisando o {self.titulo} com {self.quant} convidados.\nCada participante comerá 0.4kg e cada kg custa R${self.preco}\nO custo total será de R${total_valor:,.2f}, Cada pessoa pagará R${divisao} para participar.'
        


c1 = Churrasco('Churras dos Amigos', 15)
print(c1.analisador())