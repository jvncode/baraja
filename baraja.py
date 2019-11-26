import random

class Baraja():
    naipes = []
    __palos = ["o", "c", "e", "b"]
    __cartas = ["A", "2", "3", "4", "5", "6", "7","S", "C", "R"]

    def __init__(self):
        self.naipes = []
        for palo in self.__palos:
            for carta  in self.__cartas:
                self.naipes.append(carta + palo)

    def elige_carta(self, i, longitud):
        return random.randint(0, len(self.naipes)-1)

    def mezclar(self):
        for i in range(len(self.naipes)):
            al_azar = self.elige_carta, len(self.naipes)

            aux = self.naipes[i]  
            self.naipes[i] = self.naipes[al_azar]
            self.naipes[al_azar] = aux

    def repartir(self, mano, jugadores):
        pass
    