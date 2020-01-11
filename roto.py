import random
import terminaltables
from colorclass import Color

class Roto:

    def __init__(self):
        self.pathway = []

        rotoWiring = input("Please enter roto's Wiring: ")
        for c in rotoWiring:
            self.pathway.append(ord(c)-65)

        self.dotMarking = 0 # in the enigma machine, people marking dot for "A" contact

    def rotate(self):
        self.pathway = self.pathway[1:] + self.pathway[:1]
        self.dotMarking += 1
        if self.dotMarking == 26:
            self.dotMarking = 0

    def input(self,index):
        return self.pathway[index]
    
    def reverse(self,number):
        return self.pathway.index(number)
    
    def printRoto(self):
        map = Color("{autoblack}"+"|" + str(chr(self.pathway[-1]+65)) + "{/autoblack}")
        map += "|" + (chr(self.pathway[0]+65)) + "|"
        map += Color("{autoblack}" + str(chr(self.pathway[1]+65))+ "|" + "{/autoblack}")
        print(map)
        pass




































