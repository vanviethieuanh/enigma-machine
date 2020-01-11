import terminaltables
import os
import roto
from colorclass import Color
from constant import Constant
import random

reflectorMap = list(range(0,25))
ter_size = os.get_terminal_size().columns

def LightUp(key):
    keymap = [["Q","W","E","R","T","Y","U","I","O","P"],["A","S","D","F","G","H","J","K","L"],["","Z","X","C","V","B","N","M"]]
    if key != None:
        for i in range(len(keymap)):
            for j in range(len(keymap[i])):
                if str.upper(key)==keymap[i][j]:
                    keymap[i][j] = Color('{autoyellow}'+keymap[i][j]+'{/autoyellow}')
    keyboard = terminaltables.SingleTable(keymap)
    keyboard.inner_heading_row_border = True
    keyboard.inner_row_border = True
    print(keyboard.table.center(ter_size))

def main():
    # --------------------------------------------------------------------------
    # init rotos
    # --------------------------------------------------------------------------
    rotoA = roto.Roto(path=Constant.defaultwiring['alpha'])
    rotoB = roto.Roto(path=Constant.defaultwiring['beta'])
    rotoC = roto.Roto(path=Constant.defaultwiring['gamma'])

    # --------------------------------------------------------------------------
    # show menu
    # --------------------------------------------------------------------------
    option = None
    while True:
        os.system('clear')

        options = [["1.Use".center(ter_size-4)],["2.Plug board"],["3.Custom roto wiring"],["x.Exit"]]

        panel = terminaltables.SingleTable(options,"Enigma")
        panel.inner_heading_row_border = False
        panel.inner_row_border = False
        panel.justify_columns = {0:'center'}

        print(panel.table)
        option = input("Your option >> ")

        if option == 'x':
            break

        # ----------------------------------------------------------------------
        # 1.Use
        # ----------------------------------------------------------------------
        if option == '1':
            os.system('clear')
            rotoA.printRoto()
            rotoB.printRoto()
            rotoC.printRoto()
            LightUp(None)
            working = True
            while working:
                # input & processing
                typed = input("Enter key: ")
                if typed == 'exit':
                    working = False
                    break
                keyinput = ord(str.upper(typed)) - 65

                output = rotoA.reverse(rotoB.reverse(rotoC.reverse(
                        25 - (rotoC.input(rotoB.input(rotoA.input(keyinput)))))))
                
                # reprint the keyboard and roto
                os.system('clear')
                rotoA.printRoto()
                rotoB.printRoto()
                rotoC.printRoto()
                LightUp(chr(output+65))

                # notched ring
                if rotoA.dotMarking == 25:
                    rotoB.rotate()
                if rotoB.dotMarking == 25:
                    rotoC.rotate()
                rotoA.rotate()

        # ----------------------------------------------------------------------
        # 2.Plug board
        # ----------------------------------------------------------------------
        if option == '2':
            os.system('clear')
            print('not done yet')

        # ----------------------------------------------------------------------
        # 3.Custom roto wiring
        # ----------------------------------------------------------------------
        if option == '3':
            os.system('clear')
            print(rotoA.showRoto())
            print(rotoB.showRoto())
            print(rotoC.showRoto())
            print()
            if input('Sure wanna change ? [y/n]') == 'y':
                rotoA.enterWiring()
                rotoB.enterWiring()
                rotoC.enterWiring()
            
            


if __name__ == "__main__":
    main()









