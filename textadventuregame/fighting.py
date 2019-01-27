from text import *
import variables

weapons = ["sword", "axe", "dagger", "wand", "staff"]
armor = ["leather", "copper", "iron"]
potion = ["hp", "str", "spd"]

# enemies stats:[HP,DMG,SPD],drop
enemies = {"spider1": [[20 , 5 , 15], "armor"],
           "spider2": [[150, 25, 25], ""],
           "blob1"  : [[35 , 7 , 5 ], ""],
           "blob2"  : [[250, 35, 15], ""],
           "plant1" : [[65 , 17, 7 ], ""],
           "zombie1": [[90 , 20, 2 ], ""],
           "dragon" : [[999, 50, 20], ""]
           }

# list of attacks - name of attack:[type,damage]
atacks = {"swing sword": ["dmg", 2],
          "fireball"   : ["mag", 1]
          }


enemiemaxhp = 0

# fight or escape?
def startfight(enemie):
    global enemiemaxhp
    enemiemaxhp = enemies[enemie][0][0]
    variables.playerpossition
    while True:
        displayenemiestats(enemie)
        textlines[housedimentions[0] - 1] = "Do you want to start a fight with " + str(enemie)
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
    while True:
        if enemies[enemie][0][0] <= 0:
            return True
        elif playerstats["hp"] <= 0:
            return False
        else:
            fightoptionsmenu(enemie)
            displayenemiestats(enemie)


def displayenemiestats(enemie):
    global enemiemaxhp
    textlines[11] = "life: " + str(enemies[enemie][0][0]) + "max:" + str(enemiemaxhp)
    return


def displaymessage():

    return


def fightoptionsmenu(enemie):
    global enemies
    textlines[14] = "MENU:"
    textlines[15] = "* Attack"
    textlines[16] = "* Item"
    textlines[17] = ""
    textlines[18] = "* Run"
    while True:
        clearsecondaryfightmenu()
        textlines[housedimentions[0] - 1] = "What do you want to do?"
        printscreen()
        playerinput = readinput()
        if playerinput == "attack":
            clearquestion()
            atackmenu(enemie)
            return
        else:
            textlines[housedimentions[0] - 2] = playerinput + " is not a valid option"


def atackmenu(enemie):
    textlines[19] = "Attack:"
    textlines[20] = "* Swing Sword"
    textlines[21] = "* Fireball"
    while True:
        textlines[housedimentions[0] - 1] = "choose an attack"
        printscreen()
        playerinput = readinput()
        if playerinput == "swing sword":
            clearquestion()
            damageenemie(enemie,"swing sword")
            return
        elif playerinput == "fireball":
            clearquestion()
            damageenemie(enemie,"fireball")
            return
        else:
            textlines[housedimentions[0] - 2] = playerinput + " is not a valid option"

    return

def damageenemie(enemie, attack):
    enemies[enemie][0][0] = enemies[enemie][0][0] - playerstats[atacks[attack][0]]*atacks[attack][1]
    return