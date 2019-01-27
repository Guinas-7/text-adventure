from text import *

weapons = ["sword", "axe", "dagger", "wand", "staff"]
armor = ["leather", "copper", "iron"]
potion = ["hp", "str", "spd"]

# enemies stats:[HP,DMG,SPD],drop
enemies = {"spider1":[[20 , 5 , 15],"armor"],
           "spider2":[[150, 25, 25],""],
           "blob1"  :[[35 , 7 , 5 ],""],
           "blob2"  :[[250, 35, 15],""],
           "plant1" :[[65 , 17, 7 ],""],
           "zombie1":[[90 , 20, 2 ],""],
           "dragon" :[[999, 50, 20],""],
           }


def startfight(enemie):
    while True:
        textlines[housedimentions[0] - 1] = "Do you want to start a fight with " + str(enemie) + playerpossition + playerlastpossition
        printscreen()
        playerinput = readinput()
        if playerinput in positiveanswer:
            clearquestion()
            fightmain(enemie)
            return playerpossition
        elif playerinput in negativeanswer:
            clearquestion()
            return playerlastpossition
        else:
            textlines[housedimentions[0] - 2] = playerinput + " is not a valid option"


def fightmain(enemie):
    global enemies
    while True:
        textlines[housedimentions[0] - 1] = "type the name of the enemie"
        printscreen()
        playerinput = readinput()
        if playerinput == enemie:
            enemies[rooms[playerpossition][0][0]][0][0] = 0
            return
        else:
            textlines[housedimentions[0] - 2] = playerinput + " is not a valid option"
