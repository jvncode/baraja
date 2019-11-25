import random


_palos = ["o", "c", "e", "b"]
_cartas = ["A", "2", "3", "4", "5", "6", "7","S", "C", "R"]

def baraja():

    result=[]
    for palo in _palos:
        for carta  in _cartas:
            result.append(carta + palo)

    return result

def mezclar(b):
    for i in range(len(b)):
        al_azar = random.randint(0, len(b)-1)

        aux = b[i]  
        b[i] = b[al_azar]
        b[al_azar] = aux
    return b


    
    

