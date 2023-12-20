from abc import ABC, abstractmethod
from datetime import datetime

class Conta(ABC):
    def __init__(self, nroConta, nome, saldo):
        self.__nroConta = nroConta
        self.__nome = nome
        self.__saldo = saldo
        self.__transacoes = []
    
    @property
    def nroConta(self):
        return self.__nroConta
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo
    
    @property
    def transacoes(self):
        return self.__transacoes
    
    def deposito(self, valor):
        if valor > 0:
            data = datetime.now()#add uma transação na lista de transações
            transacao = Transacao(data, valor, 'Depósito realizado')
            self.transacoes.append(transacao)#cada objeto da lista transações é um objeto da classe Transacao
            self.saldo += valor

    def retirada(self, valor):#sobrescrita de métodos
        if valor > 0 and valor <= self.saldo:
            data = datetime.now()
            transacao = Transacao(data, -valor, 'Retirada realizada')
            self.transacoes.append(transacao)
            self.saldo -= valor

    @abstractmethod
    def ImprimirExtrato(self):
        pass

class Transacao:
    def __init__(self, data, valor, descricao):
        self.__data = data
        self.__valor = valor
        self.__descricao = descricao

    @property
    def data(self):
        return self.__data
    
    @property
    def valor(self):
        return self.__valor
    
    @property
    def descricao(self):
        return self.__descricao
    
class contaComum(Conta):
    def __init__(self, nroConta, nome, saldo):
        super().__init__(nroConta, nome, saldo)
    
    def ImprimirExtrato(self):
        print(f'Nro Conta: {self.nroConta} - Nome: {self.nome}')
        for transacao in self.transacoes:
            print(f'Data: {transacao.data} - Valor: {transacao.valor} - Descrição: {transacao.descricao}')
        print(f'Saldo: {self.saldo}')

class contaLimite(Conta):
    def __init__(self, nroConta, nome, saldo, limite):
        super().__init__(nroConta, nome, saldo)
        self.__limite = limite

    @property
    def limite(self):
        return self.__limite
    
    def retirada(self, valor):
        if valor > 0 and valor <= (self.saldo + self.limite):
            data= datetime.now()
            transacao = Transacao(data, -valor, 'Retirada realizada')
            self.transacoes.append(transacao)
            self.saldo -= valor
    
    def ImprimirExtrato(self):
        print(f'Nro Conta: {self.nroConta} - Nome: {self.nome} - Limite: {self.limite}')
        for transacao in self.transacoes:
            print(f'Data: {transacao.data} - Valor: {transacao.valor} - Descrição: {transacao.descricao}')
        print(f'Saldo: {self.saldo}')

class contaPoupança(Conta):
    def __init__(self, nroConta, nome, saldo, diaAniversario):
        super().__init__(nroConta, nome, saldo)
        self.__diaAniversario = diaAniversario
    
    @property
    def diaAniversario(self):
        return self.__diaAniversario
    
    def ImprimirExtrato(self):
        print(f'Nro Conta: {self.nroConta} - Nome: {self.nome} - Dia do Aniversário: {self.diaAniversario}')
        for transacao in self.transacoes:
            print(f'Data: {transacao.data} - Valor: {transacao.valor} - Descrição: {transacao.descricao}')
        print(f'Saldo: {self.saldo}')

if __name__ == "__main__":
    comum = contaComum("1234", "José", 1500.0)
    limite = contaLimite("7854", "Maria", 1000.0, 500.0)
    poupanca = contaPoupança("5267", "João", 1800.0, 1)

    comum.deposito(200.0)
    comum.retirada(700.0)

    limite.deposito(100.0)
    limite.retirada(400.0)

    poupanca.deposito(200.0)
    poupanca.retirada(800.0)

    contas = [comum, limite, poupanca]

    for conta in contas:
        conta.ImprimirExtrato()
        print()

