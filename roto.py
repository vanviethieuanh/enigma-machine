import random
import terminaltables

class Roto:

    def __init__(self):
        self.pathway = []

        rotoWiring = input("Please enter roto's Wiring: ")
        for c in rotoWiring:
            self.pathway.append(ord(c)-65)

    def rotate(self):
        self.pathway = self.pathway[1:] + self.pathway[:1]

    def input(self,index):
        return self.pathway[index]
    
    def reverse(self,number):
        return self.pathway.index(number)
    
    def printRoto(self):
        map = "|"
        for i in self.pathway:
            map += (chr(i+65)) + "|"
        map = map[0:-1]
        print(map)
        pass




































