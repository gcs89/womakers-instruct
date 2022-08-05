from mailbox import NotEmptyError
from urllib.parse import _NetlocResultMixinBytes


class Pessoa:
    def __init__(self, nome, profissao, identidade):
        self._nome = nome
        self.profissao = profissao
        self.__identidade = identidade
    
    def __str__(self):
        return f'Nome: {self._nome}, Profissao: {self.profissao}, Identidade: {self.__identidade}'


pessoa1 = Pessoa('Ana', 'Programadora', '123456')
#print(pessoa1)

#Ao tentar alterar um atributo publico o valor eh alterado.
pessoa1.profissao = 'Medica'
# metodo privado nao consegue alterar/ver fora da classe.
pessoa1.__identidade = '234560'
#o protegido consegue alterar o valor com ressalvas. Ex: nome social.
pessoa1._nome = 'Marta'

print(pessoa1)