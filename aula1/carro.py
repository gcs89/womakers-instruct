# classe

class Carro:
    def __init__(self):
        self.ligado = False
        self.cor = "Branco"
        self.modelo = 2022
        self.velocidade = 0
        self.velocidade_min = 1
        self.velocidade_max = 200

    def liga(self):
        self.ligado = True
    
    def desliga(self):
        self.ligado = False
    
    def acelera(self):
        if not self.ligado:
            return
        if self.velocidade < self.velocidade_max:
            self.velocidade += 10

    def desacelera(self):
        if not self.ligado:
            return
        if self.velocidade > self.velocidade_min:
            self.velocidade -= 10
    
    def __str__(self) -> str:
        return f'Carro: Ligado? {self.ligado} - Cor: {self.cor} - Modelo: {self.modelo} - Velocidade: {self.velocidade} km/h'

# instancias

carro_novo = Carro()

carro_novo.liga()
print('carro_novo está ligado? {}'.format(carro_novo.ligado))

for _ in range(2):
    carro_novo.acelera()
print("carro_novo: {}" .format(carro_novo.velocidade))

for _ in range(2):
    carro_novo.desacelera()
print("carro_novo: {}" .format(carro_novo.velocidade))

print("carro_novo", carro_novo)