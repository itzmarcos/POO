class ContaBancaria:
    """
    Criei uma conta bancaria de saques e depositos.
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print (f'Conta {self.id} criada com sucesso!')
    

    def __str__(self):
        return f'A conta {self.id} de {self.titular} tem o saldo de R${self.saldo:,.2f} reais'
    

    def depositar(self, valor):
        self.saldo += valor
        print (f'Deposito de R${valor:,.2f} autorizado e o total foi atualizado para R${self.saldo:,.2f}')

    def sacar(self, valor):
        if valor > self.saldo:
            print (f'Saldo insuficiente para o valor de {valor:,.2f}')
        else:
            self.saldo -= valor
            print (f'Saque de R${valor:,.2f} realizado com sucesso, e o total atual é de R${self.saldo:,.2f}')

    
    
cliente = ContaBancaria(122, "Jaki", 9000)
cliente.depositar(500)
cliente.sacar(100000)
print(cliente)