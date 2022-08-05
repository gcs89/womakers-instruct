import math
#string literal formatada ou f-strings

ano = 2022
evento = "FIG"
#print(f"Hoje vai ter {evento} {ano}")

#print(f"O valor de pi é aproximadamente {math.pi:.3f}!")

animal = "gatos"
#print (f"Minha casa está cheia de {animal}!!")
#print (f"Minha casa está cheia de {animal!r}!!")

table = {"Maria": 1111112, "João": 2222223, "Marilia": 3333334}

#for nome, telefone in table.items():
    #print(f"{nome:10} -> {telefone:10d}")

# metodo format()

#print('We are the {} who say "{}!"'.format('knights', 'Ni'))
print("Nós somos os {} que dizem {}!".format("Cavaleiros", "NI"))
print("Queria {} uma {}...".format("jantar", "lasanha de lentilha"))

# elementos posicionados com format()
#print('{0} and {1}'.format('spam', 'eggs'))
#print('{1} and {0}'.format('spam', 'eggs'))
print("{0} e {1}".format("torrada", "tofu"))
print("{1} e {0}".format("torrada", "tofu"))

# argumentos nomeados com format())
print("Esse {comida} é muito {adjetivo}!".format(comida="bolo de chocolate", adjetivo="gostoso"))

print("Hoje eu vou comer {0}, {1} e {outro}!".format("bolo", "salada", outro="chá de camomila"))

print('The value of pi is approximately %0.3f.' % math.pi)
