# ==============================================================================
# ROTO
# ==============================================================================

import random
import terminaltables
from constant import Constant
from colorclass import Color

class Roto:

    def __init__(self,path):
        self.pathway = []
        self.wired(path)
        self.dotMarking = 0 # in the enigma machine, people marking dot for "A" contact

    def enterWiring(self):
        rotoWiring = input("Please enter roto's Wiring: ")
        for c in rotoWiring:
            self.pathway.append(ord(c)-65)
    
    def wired(self, path):
        for c in path:
            self.pathway.append(ord(c)-65)

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
        print(map.center(Constant.keyboard_width))
        pass

    def showRoto(self):
        result = "Wiring map: |"
        for i in self.pathway:
            result += chr(i+65)+"|"
        return result



































