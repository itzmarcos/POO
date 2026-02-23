class Adolecente:
    """
    Primeira class sendo testada no curso!
    """
    def __init__(self, nome = '', idade = 0):
        self.nome = nome
        self.idade = idade

    def maior(self):
        self.idade = self.idade + 1
    
    def __str__(self):
        return f'A {self.nome} tem {self.idade} anos'
    def __getstate__(self):
        return f'A {self.nome} tem {self.idade} anos'
    
aluno = Adolecente('jaki', 17)
print(aluno.__doc__)
print(aluno.__dict__)
print(aluno.__getstate__())