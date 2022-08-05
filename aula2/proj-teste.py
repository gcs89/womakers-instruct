# ao inves de fazer objetos diferentes, colocar so o veiculo com tipos diferentes e fazer a verificação a partir dele.

class Vaga:
    def __init__(self, id_vaga, tipo, livre):
        self.id_vaga = id_vaga
        self.tipo = tipo
        self.livre = livre

    def ocupar(self):

        self.livre = False

        print("A vaga {} foi ocupada.".format(self.id_vaga))

    def desocupar(self):
        # colocar if pra saber se está estacionado
        # liberar vaga com for. se a placa da vaga for == a placa do carro, reseta a placa e desocupa a vaga.
        print("A vaga {} foi desocupada.".format(self.id_vaga))

    # def __str__(self):
        #return f'A vaga de ID numero {self.id_vaga} é do tipo {self.tipo} e se encontra {self.livre} para um veiculo.'

class Veiculo:
    def __init__(self, placa, estacionado, tipo):
        self.placa = placa
        self.estacionado = estacionado
        self.tipo = tipo

    def estacionar(self, vaga: Vaga):

        vaga.ocupar()

        print("O {} está estacionando na vaga {}.".format(self.tipo, vaga.id_vaga))
    
    def sair_da_vaga(self, vaga: Vaga):

        vaga.livre = True
        print("O {} está saindo da vaga {}.".format(self.tipo, vaga.id_vaga))

    # def __str__(self):
        #return f'O {self.tipo} tem a placa {self.placa} e seu status de estacionamento é {self.estacionado}.'

class Carro(Veiculo):
    pass

class Moto(Veiculo):
    pass



class Estacionamento:
    def __init__(self, vagas_de_carro, vagas_de_moto, total_vagas_livres_carro, total_vagas_livres_moto, carros_para_vaga, motos_para_vaga):
        self.vagas_de_carro = vagas_de_carro
        self.vagas_de_moto = vagas_de_moto
        self.total_vagas_livres_carro = total_vagas_livres_carro
        self.total_vagas_livres_moto = total_vagas_livres_moto
        self.carros_para_vaga = carros_para_vaga
        self.motos_para_vaga = motos_para_vaga

    def estacionar_carro(self, carro: Carro, vaga: Vaga):



        if (self.carros_para_vaga > 0) and (self.carros_para_vaga < 6):
            print("Está livre para estacionar carro.")
        elif self.total_vagas_livres_carro == 1:
            print("Resta apenas uma vaga para carros")
        else:
            print("O estacionamento está cheio para carros.")

        #total_vagas_livres_carro = total_vagas_livres_carro - 1
        #print("O total de vagas livres para carro é {}\n".format(total_vagas_livres_carro))
            
    # somar vagas de carros e motos
    def estacionar_moto(self, total_vagas_livres_moto, total_vagas_livres_carro, motos_para_vaga, carros_para_vaga):
        if (motos_para_vaga <= 1) and (total_vagas_livres_moto >= 1) and (total_vagas_livres_moto <= 5):
            print("Está livre para estacionar moto.")
        elif (total_vagas_livres_moto == 0) and (motos_para_vaga > 1) and (total_vagas_livres_carro <= 5) and (carros_para_vaga == 0):
            print("A moto deverá estacionar em uma vaga de carro")
        else:
            print("Não há mais vagas livres para moto.")
        
        #total_vagas_livres_moto = (total_vagas_livres_moto + total_vagas_livres_carro) - 1
        #print("O total de vagas livres para moto é {}\n".format(total_vagas_livres_moto))
    def remover_moto(self, moto: Moto, vaga: Vaga):
        print("A moto de placa {} foi removida da vaga {}".format(moto.placa, vaga.id_vaga))

    def __str__(self):
         return f'O estacionamento tem {self.vagas_de_carro} vagas de carro e {self.vagas_de_moto} vagas de moto.\nNo momento, há {self.total_vagas_livres_carro} vagas livres de carro e {self.total_vagas_livres_moto} vagas livres de moto.\n'

vaga1 = Vaga("01", "carro", False)
vaga2 = Vaga("02", "carro", True)

carro1 = Carro("LLL-1111", True, "carro")
carro1.estacionar(vaga1)

moto1 = Moto("NAN-3333", True, "moto")
moto1.estacionar(vaga2)

estacionamento1 = Estacionamento(25, 25, 5, 0, 0, 2)
print(estacionamento1)


vaga3 = Vaga("03", "carro", True)
vaga4 = Vaga("04", "carro", True)
vaga5 = Vaga("05", "carro", True)
vaga6 = Vaga("06", "moto", False)
vaga7 = Vaga("07", "moto", True)
vaga8 = Vaga("08", "moto", True)
vaga9 = Vaga("09", "moto", True)
vaga10 = Vaga("10", "moto", True)

estacionamento1.estacionar_carro(4,1)
vaga1.ocupar()

estacionamento1.estacionar_moto(0,4,2,0)
vaga6.ocupar()
vaga7.desocupar()
estacionamento1.remover_moto(moto1, vaga6)
