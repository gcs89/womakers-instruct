class Pessoa:
    def __init__(self,nome):
        self._nome = nome
        self._tipo = 'Pessoa'
    
    def falar_oi(self):
        print('Oiiii! Meu nome eh {}.'.format(self._nome))

    def falar_tipo(self):
        print('Meu tipo eh {}'.format(self._tipo))

pessoa1 = Pessoa('Maria')
pessoa1.falar_oi()
pessoa1.falar_tipo()

# A classe Estudante é derivada da classe Pessoa
# Relação: todo estudante é uma pessoa
class Estudante(Pessoa):
    def __init__(self, nome, curso):
        super().__init__(nome) #chama o construtor da classe base
        self._curso = curso

    def falar_curso(self):
        print(f'Eu, {self._nome}, estudo o curso de {self._curso}.') #a propriedade self._nome é herdada da classe base (super)
    
    def falar_tipo(self):
        self._tipo = 'Estudante'
        return super().falar_tipo()

estudante = Estudante('Yasmin', 'Introducao ao Python')
estudante.falar_oi() #o metodo falar_oi eh herdado da classe base (super)
estudante.falar_tipo() # herdado da classe base e sobreescrito na classe derivada
estudante.falar_curso() #