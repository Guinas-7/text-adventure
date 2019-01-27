from text import *
import variables



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


# fight or escape?
def startfight(enemie):
    variables.playerpossition
    while True:
        displayenemiestats(enemie)
        textlines[housedimentions[0] - 1] = "Do you want to start a fight with " + str(enemie) + variables.playerpossition + variables.playerlastpossition
        printscreen()
        playerinput = readinput()
        if playerinput in positiveanswer:
            clearquestion()
            if fightmain(enemie):
                return variables.playerpossition
            else:
                return variables.startpossition
        elif playerinput in negativeanswer:
            clearquestion()
            return variables.playerlastpossition
        else:
            textlines[housedimentions[0] - 2] = playerinput + " is not a valid option"


# main fight cicle
def fightmain(enemie):
    global enemies
    while True:
        textlines[housedimentions[0] - 1] = "type the name of the enemie"
        printscreen()
        playerinput = readinput()
        if playerinput == enemie:
            enemies[enemie][0][0] = 0
            return True
        else:
            return False


def displayenemiestats(enemie):
    textlines[11] = "life: " + str(enemies[enemie][0][0])
    return


def displaymessage():

    return


def fightoptionsmenu():

    return

