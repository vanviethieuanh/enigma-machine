import random
import terminaltables

class Roto:

    def __init__(self):
        self.pathway = list(range(0,26))
        random.shuffle(self.pathway)

        self.pointer = 0
        self.printRoto()

    def rotate(self):
        if self.pointer == 25:
            self.pointer = 0
            return
        self.pointer += 1

    def input(self,index):
        if index+self.pointer > 25:
            index = index + self.pointer - 25
        else:
            index = index + self.pointer
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



    




































