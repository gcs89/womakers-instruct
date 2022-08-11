from concurrent.futures import process

class Correntista:
    def __init__(self, titular1, titular2, telefone, renda, emprestimo):
        self.__titular1 = titular1
        self.__titular2 = titular2
        self.__telefone = telefone
        self.__renda = renda
        self.emprestimo = emprestimo

    @property
    def nome_titular1(self):
        return self.__titular1

    @property
    def nome_titular2(self):
        return self.__titular2

    @property
    def telefone(self):
        return self.__telefone
    
    @property
    def renda_mensal(self):
        return self.__renda

    @property
    def emprestimo_disponivel(self):
        return self.emprestimo
        
class Conta(Correntista):
    def __init__(self, titular1, titular2, telefone, renda, emprestimo, saldo):
        self.__titular1 = titular1
        self.__titular2 = titular2
        self.__telefone = telefone
        self.__renda = renda
        self.emprestimo = emprestimo
        self.__saldo = saldo

    @property
    def nome_titular1(self):
        return self.__titular1

    @property
    def nome_titular2(self):
        return self.__titular2

    @property
    def telefone(self):
        return self.__telefone
    
    @property
    def renda_mensal(self):
        return self.__renda

    @property
    def emprestimo_disponivel(self):
        return self.emprestimo

    def status_conta(self):
        print(f"Esta é a conta corrente de {self.__titular1} e {self.__titular2}. Seu saldo é de R$ {self.__saldo}")

    def deposito(self, deposito):
        self.__saldo = self.__saldo + deposito
        print(f"Você depositou R$ {deposito}. Seu saldo atual é de R$ {self.__saldo}.")

    def saque(self, saque):
        self.__saldo = self.__saldo - saque
        print(f"Você sacou R$ {saque}. Seu saldo atual é de R$ {self.__saldo}.")

    def pegar_emprestimo(self): 
        if (self.emprestimo == True):
            self.__saldo = self.__saldo + self.__renda
            print(f"Você solicitou um empréstimo de R$ {self.__renda} com sucesso. Seu saldo atual é R$ {self.__saldo}.")
        elif (self.emprestimo == False):
            print("Você não preenche os requisitos para solicitar um empréstimo.")

conta01 = Conta("Mario", "Alfredo", "000-000", 5000, False, 500)
conta01.status_conta()
conta01.deposito(500)
conta01.saque(300)
conta01.pegar_emprestimo()

conta02 = Conta("Jenifer", "Bento", "111-1111", 8000, True, 2500)
conta02.status_conta()
conta02.deposito(1000)
conta02.saque(500)
conta02.pegar_emprestimo()


