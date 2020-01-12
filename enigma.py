import terminaltables
import os
import roto
from colorclass import Color
from constant import Constant
import random

reflectorMap = list(range(0,25))
ter_size = os.get_terminal_size().columns
Plugboard = []

def PrintPlugBoard(Plugboard):
    if len(Plugboard) == 0:
        print("Plugboard hasn't been plugged")

    for i in range(len(Plugboard)):
        print(chr(Plugboard[i][0]+65),end=' ')
    print()

    for _ in range(len(Plugboard)):
        print('|', end=' ')
    print()

    for i in range(len(Plugboard)):
        print(chr(Plugboard[i][1]+65),end=' ')
    print()
    pass

def MessengerBox(message,title):
    messbox = terminaltables.SingleTable(message,title)
    messbox.inner_heading_row_border = False
    messbox.inner_row_border = False
    messbox.justify_columns = {0:'center'}
    print(messbox.table)

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

def OpenPlugBoard(Plugboard):
    while True:
        os.system('clear')
        MessengerBox([["1.Plug"],["2.Unplug"],["x.exit"]],"Plug board") 
        option = input("Your options >> ")

        if option == '1':
            while True:
                os.system('clear')
                PrintPlugBoard(Plugboard)
                MessengerBox([["Press a pair of keys to plug together,\nfor example press \"PD\" to plug \"P\" & \"D\" together.\nTo exit, type \"exit\" key then hit \"Enter\""]],
                                                "Guide")
                command = input(">> ")
                if command == 'exit':
                    break
                
                if len(command) != 2:
                    continue
                else:
                    command = str.upper(command)
                    key1 = ord(command[0]) - 65
                    key2 = ord(command[1]) - 65
                    
                    allow = True
                    for pair in Plugboard:
                        if key1 == pair[0] or key1 == pair[1]:
                            print ("the key ",command[0]," has been plugged, please enter another key")
                            input()
                            allow = False
                            break
                        
                        if key2 == pair[0] or key2 == pair[1]:
                            print ("the key ",command[1]," has been plugged, please enter another key")
                            input()
                            allow = False
                            break
                    if not allow:
                        continue

                    Plugboard.append([key1,key2])
                

        if option == '2':
            while True:
                os.system('clear')
                PrintPlugBoard(Plugboard)
                MessengerBox([["Press any key to unplug those key with their partner.\nTo unplug all, type \"all\" then hit \"Enter\".\nTo exit, type \"exit\" then hit \"Enter\""]],
                                "Guide")
                command = input(">> ")
                if command == 'exit':
                    break
                if command == 'all':
                    Plugboard = []
                else:
                    key = ord(str.upper(command[0])) - 65
                    length = len(Plugboard)
                    for i in range(length):
                        if Plugboard[i][0] == key or Plugboard[i][1] == key:
                            Plugboard = Plugboard[:i]+Plugboard[i+1:]
                            break

        if option == 'x':
            break

def CustomRotoWiring(rotoA, rotoB, rotoC):
    os.system('clear')
    print(rotoA.showRoto())
    print(rotoB.showRoto())
    print(rotoC.showRoto())
    print()
    if input('Sure wanna change ? [y/n]') == 'y':
        rotoA.enterWiring()
        rotoB.enterWiring()
        rotoC.enterWiring()

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

        options = [["1.Use".center(ter_size-4)],["2.Plug board"],["3.Ring settings"],["4.Custom roto wiring"],["x.Exit"]]
        MessengerBox(options,"Enigma")
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
            PrintPlugBoard(Plugboard)

            while True:
                # input & processing
                typed = input("Enter key: ")
                if typed == 'exit':
                    break

                keyinput = ord(str.upper(typed)) - 65

                for pair in Plugboard:
                    if keyinput == pair[0]:
                        keyinput = pair[1]
                        break
                    if keyinput == pair[1]:
                        keyinput = pair[0]
                        break

                output = rotoA.reverse(rotoB.reverse(rotoC.reverse(
                        25 - (rotoC.input(rotoB.input(rotoA.input(keyinput)))))))
                
                for pair in Plugboard:
                    if output == pair[0]:
                        output = pair[1]
                        break
                    if output == pair[1]:
                        output = pair[0]
                        break
                
                # reprint the rotos, keyboard, plugboard
                os.system('clear')
                rotoA.printRoto()
                rotoB.printRoto()
                rotoC.printRoto()
                LightUp(chr(output+65))
                PrintPlugBoard(Plugboard)

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
            OpenPlugBoard(Plugboard)

        # ----------------------------------------------------------------------
        # 3. Ring settings
        # ----------------------------------------------------------------------
        if option == '3':
            os.system('clear')

            MessengerBox([["Enter a number for ring settings"]],"Guide")

            rotoA.rotateTo(int(input(">>")))
            rotoA.printRoto()
            rotoB.rotateTo(int(input(">>")))
            rotoB.printRoto()
            rotoC.rotateTo(int(input(">>")))
            rotoC.printRoto()

            input()



        # ----------------------------------------------------------------------
        # 4.Custom roto wiring
        # ----------------------------------------------------------------------
        if option == '4':
            CustomRotoWiring(rotoA,rotoB,rotoC)
            
            


if __name__ == "__main__":
    main()









