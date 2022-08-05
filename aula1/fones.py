class Fone:
    def __init__(self):
        self.ligado = False
        self.toca_musica = False
        self.volume = 20
        self.volume_min = 0
        self.volume_max = 100

    def ligar(self):
         self.ligado = True

    def desligar(self):
        self.ligado = False

    def play(self):
        if not self.ligado:
            return
        if self.toca_musica == False:
            self.toca_musica = True
    def pause(self):
        if not self.ligado:
            return
        if self.toca_musica == True:
            self.toca_musica = False

    def diminuir_volume(self):
        if not self.ligado:
            return
        if self.volume > self.volume_min:
            self.volume -= 10
    
    def aumentar_volume(self):
        if not self.ligado:
            return
        if self.volume < self.volume_max:
            self.volume += 10

fone_celular = Fone()
fone_celular.ligar()

print("O fone_celular está ligado? {}".format(fone_celular.ligado))

for _ in range(1):
    fone_celular.aumentar_volume()
print("O volume do fone_celular está em: {}".format(fone_celular.volume))

print("fone_celular", fone_celular)