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
        self.pathway.clear()
        rotoWiring = input("Please enter roto's Wiring: ")
        for c in rotoWiring:
            self.pathway.append(ord(c)-65)
    
    def wired(self, path):
        for c in path:
            self.pathway.append(ord(c)-65)

    def rotate(self):
        self.dotMarking += 1
        if self.dotMarking == 26:
            self.dotMarking = 0

    def rotateTo(self, number):
        self.dotMarking = (number - 1)%25
        if self.dotMarking == 26:       
            self.dotMarking = 0


    def input(self,index):
        if not self.dotMarking == 0:
            rotated = self.pathway[self.dotMarking:] + self.pathway[:self.dotMarking]
            return rotated[index]
        else:
            return self.pathway[index]
    
    def reverse(self,number):
        if not self.dotMarking == 0:
            rotated = self.pathway[self.dotMarking:] + self.pathway[:self.dotMarking]
            return rotated.index(number)
        else:
            return self.pathway.index(number)
    
    def printRoto(self):
        map = Color("{autoblack}"+"|" + str.zfill(str(1 if self.dotMarking == 25 else self.dotMarking + 2),2) + "{/autoblack}")
        map += "|" + str.zfill(str(self.dotMarking+1),2) + "|"
        map += Color("{autoblack}" + str.zfill(str(26 if self.dotMarking == 0 else self.dotMarking),2)+ "|" + "{/autoblack}")
        print(map.center(Constant.keyboard_width))
        pass

    def showRoto(self):
        result = "Wiring map: |"
        for i in self.pathway:
            result += chr(i+65)+"|"
        return result



































