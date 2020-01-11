import terminaltables
import os
import roto
from colorclass import Color
import random

reflectorMap = range(0,25)

def LightUp(key):
    keymap = [["Q","W","E","R","T","Y","U","I","O","P"],["A","S","D","F","G","H","J","K","L"],["","Z","X","C","V","B","N","M"]]
    if key != None:
        for i in range(len(keymap)):
            for j in range(len(keymap[i])):
                if str.upper(key)==keymap[i][j]:
                    keymap[i][j] = Color('{autoyellow}'+keymap[i][j]+'{/autoyellow}')
    keyboard = terminaltables.SingleTable(keymap, 'Enigma')
    keyboard.inner_heading_row_border = True
    keyboard.inner_row_border = True
    print(keyboard.table)

rotoA = roto.Roto()
rotoB = roto.Roto()
rotoC = roto.Roto()

while True:
    keyinput = ord(str.upper(input("Enter key: "))) - 65
    output = rotoA.reverse(rotoB.reverse(rotoC.reverse(25 - (rotoC.input(rotoB.input(rotoA.input(keyinput)))))))
    os.system('clear')

    rotoA.printRoto()
    rotoB.printRoto()
    rotoC.printRoto()

    LightUp(chr(output+65))
    if rotoA.dotMarking == 25:
        rotoB.rotate()
    if rotoB.dotMarking == 25:
        rotoC.rotate()
    rotoA.rotate()







