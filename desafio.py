import math

def automated_readability_index(sentence):
    # escreva aqui a sua implementacao
    sentence = input()
    letras = len(sentence.replace(" ", ""))
    palavras = len(sentence.split())
    frases = 1
        
    calculo1 = 4.71 * (letras/palavras)
    calculo2 = 0.5 * (palavras/frases)
    resultado = math.ceil(calculo1 + calculo2 - 21.43)
        
    if resultado > 14:
        return 14
    elif resultado <= 0:
        return 1
    else:
        return resultado
        
print(automated_readability_index(""))



