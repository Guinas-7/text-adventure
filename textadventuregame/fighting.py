from text import *
import variables

weapons = ["sword", "axe", "dagger", "wand", "staff"]
armor = ["leather", "copper", "iron"]
potion = ["hp", "str", "spd"]

playerattacks = ["swing", "fireball", "pass", "pass"]

# enemies stats:[HP,DMG,SPD],drop
enemies = {"spider1": [[20 , 5 , 15], ["attack1","attack2"]],
           "spider2": [[150, 25, 25], ["attack1","attack2"]],
           "blob1"  : [[35 , 7 , 5 ], ["attack1","attack2"]],
           "blob2"  : [[250, 35, 15], ["attack1","attack2"]],
           "plant1" : [[65 , 17, 7 ], ["attack1","attack2"]],
           "zombie1": [[90 , 20, 2 ], ["attack1","attack2"]],
           "dragon" : [[999, 50, 20], ["attack1","attack2"]]
           }
enemyattacks = {"pass"     : [0],
                "attack1"   : [2],
                "attack2"   : [1]
                }
# list of attacks - name of attack:[type,damage]
attacks = {"pass"     : ["dmg", 0],
           "swing"    : ["dmg", 2],
           "fireball" : ["mag", 1]
           }


enemymaxhp = 0

# fight or escape?
def startfight(enemy):
    global enemymaxhp
    enemymaxhp = enemies[enemy][0][0]
    variables.playerpossition
    while True:
        displayenemystats(enemy)
        textlines[housedimentions[0] - 1] = "Do you want to start a fight with " + str(enemy)
        printscreen()
        playerinput = readinput()
        if playerinput in positiveanswer:
            clearquestion()
            if fightmain(enemy):
                return variables.playerpossition
            else:
                return variables.startpossition
        elif playerinput in negativeanswer:
            clearquestion()
            return variables.playerlastpossition
        else:
            textlines[housedimentions[0] - 2] = playerinput + " is not a valid option"


# main fight cycle
def fightmain(enemy):
    while True:
        # battle won
        if enemies[enemy][0][0] <= 0:
            return True
        # battle lost
        elif playerstats["hp"] <= 0:
            return False
        else:
            fightoptionsmenu(enemy)
            displayenemystats(enemy)
            enemyattack(enemy)
            updateplayerstats()


def enemyattack(enemy):
    attack = "attack1"
    variables.playerstats["hp"] = variables.playerstats["hp"] - enemyattacks[attack][0] * enemies[enemy][0][1]
    displaymessage("damage", attack, enemy, enemyattacks[attack][0] * enemies[enemy][0][1])
    return


# updates lines with enemy stats
def displayenemystats(enemy):
    global enemymaxhp
    textlines[11] = "life: " + str(enemies[enemy][0][0]) + "max:" + str(enemymaxhp)
    return


# ►◄▼
def displaymessage(type, attack, enemy, damage):
    textlines[12] = textlines[13]
    if type == "attack":
        textlines[13] = "► You attacked " + enemy + " with " + attack + " and done " + str(damage) + " damage to it"
    elif type == "damage":
        textlines[13] = "◄ You were attacked by " + enemy + " with " + attack + " and received " + str(damage) + " damage"
    return


def fightoptionsmenu(enemy):
    global enemies
    textlines[15] = "MENU:"
    textlines[16] = "* Attack"
    textlines[17] = "* Item           * Run"

    while True:
        clearsecondaryfightmenu()
        textlines[housedimentions[0] - 1] = "What do you want to do?"
        printscreen()
        playerinput = readinput()
        if playerinput == "attack":
            clearquestion()
            atackmenu(enemy)
            return
        else:
            textlines[housedimentions[0] - 2] = playerinput + " is not a valid option"


def atackmenu(enemy):
    textlines[19] = "Attack:"
    textlines[20] = "* " + playerattacks[0] + "".join([" " for x in range(1, 20-len(playerattacks[0]))]) + "* " + playerattacks[2]
    textlines[21] = "* " + playerattacks[1] + "".join([" " for x in range(1, 20-len(playerattacks[1]))]) + "* " + playerattacks[3]
    while True:
        textlines[housedimentions[0] - 1] = "choose an attack"
        printscreen()
        playerinput = readinput()
        if playerinput == playerattacks[0]:
            clearquestion()
            damageenemy(enemy, playerattacks[0])
            return
        elif playerinput == playerattacks[1]:
            clearquestion()
            damageenemy(enemy, playerattacks[1])
            return
        elif playerinput == playerattacks[2]:
            clearquestion()
            damageenemy(enemy, playerattacks[2])
            return
        elif playerinput == playerattacks[3]:
            clearquestion()
            damageenemy(enemy, playerattacks[3])
            return
        else:
            textlines[housedimentions[0] - 2] = playerinput + " is not a valid option"

    return


# damage the enemy by multiplying the base damage of the player with the attack multiplier
def damageenemy(enemy, attack):
    enemies[enemy][0][0] = enemies[enemy][0][0] - playerstats[attacks[attack][0]] * attacks[attack][1]
    displaymessage("attack", attack, enemy, playerstats[attacks[attack][0]] * attacks[attack][1])
    return
