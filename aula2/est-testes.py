class Estacionamento:
    def __init__(self, vagas_carro, vagas_moto):
        self.vagas_carro = vagas_carro
        self.vagas_moto = vagas_moto

    def estacionar_carro(self, carro):
        print("{} estacionado.".format(carro.placa))
    
    def estacionar_moto(self):
        print("Moto estacionada.")

    def __str__(self):
        return f'Há {self.vagas_carro} vagas de carro e {self.vagas_moto} vagas de moto no momento.'

class Vaga:
    def __init__(self, id_vaga, vaga_livre):
        self.id_vaga = id_vaga
        self.vaga_livre = vaga_livre

    def __str__(self):
        return f'Id da vaga: {self.id_vaga}, Livre: {self.vaga_livre}.'

class Carro:
    def __init__(self, placa, estacionado):
        self.placa = placa
        self.estacionado = estacionado
        teste.estacionar_carro(self)
    
    def __str__(self):
        return f'Placa do carro: {self.placa}, Estacionado: {self.estacionado}.'

teste = Estacionamento(5,5)
vaga1 = Vaga(1, False)
carro1 = Carro("KFC-0000", True)

print(f"O estacionamento {teste} tem {vaga1} restante. O veiculo {carro1} acabou de estacionar.")