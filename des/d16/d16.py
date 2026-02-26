class Funcionario:
    # Atributos de Classe
    empresa = 'Yout'
    def __init__(self, nome, setor, cargo):
        # Atributos de Instancia
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self):
        return f'Olá eu sou {self.nome} e sou {self.cargo} do setor de {self.setor} da empresa {Funcionario.empresa}'
    
Funcionario.empresa = 'VASpp'
    
c1 = Funcionario('Jaki', 'T1', 'Pleno')
print(c1.apresentacao())

c2 = Funcionario('Lucas', 'Administração', 'Diretor')
print(c2.apresentacao())

# print(c1)
# print(c2)
        