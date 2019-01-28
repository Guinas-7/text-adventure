from text import *
import variables

weapons = ["sword", "axe", "dagger", "wand", "staff"]
armor = ["leather", "copper", "iron"]
potion = ["hp", "str", "spd"]

playerattacks = ["swing", "fireball", "pass", "pass"]

itemslist = {"hp potion":[2,650],
             "dmg potion":[0,1],
             "mag potion":[0,1],
             "def potion":[0,1]
             }

# enemies stats:[HP,DMG,SPD],drop
enemies = {"spider1": [[20 , 5 , 4], ["attack1","attack2"]],
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
           "swing"    : ["dmg", 1.3],
           "fireball" : ["mag", 1]
           }


enemymaxhp = 0

originalplayerstats = {"dmg"  : 7,
                       "mag"  : 5,
                       "def"  : 5,
                       }


def saveplayerstats():
    originalplayerstats["dmg"] = variables.playerstats["dmg"]
    originalplayerstats["mag"] = variables.playerstats["mag"]
    originalplayerstats["def"] = variables.playerstats["def"]
    return


def reverseplayerstats():
    variables.playerstats["dmg"] = originalplayerstats["dmg"]
    variables.playerstats["mag"] = originalplayerstats["mag"]
    variables.playerstats["def"] = originalplayerstats["def"]
    return


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
            saveplayerstats()
            clearquestion()
            if fightmain(enemy):
                reverseplayerstats()
                return variables.playerpossition
            else:
                reverseplayerstats()
                return variables.playerlastpossition
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
            variables.playerstats["hp"] = variables.playerstats["maxhp"]
            variables.playerlastpossition = variables.startpossition
            return False
        else:
            if fightoptionsmenu(enemy):
                displayenemystats(enemy)
                enemyattack(enemy)
                updateplayerstats()
            else:
                return False


def enemyattack(enemy):
    attack = random.choice(enemies[enemy][1])
    variables.playerstats["hp"] = variables.playerstats["hp"] - enemyattacks[attack][0] * enemies[enemy][0][1]
    displaymessage("damage", attack, enemy, enemyattacks[attack][0] * enemies[enemy][0][1])
    return


# updates lines with enemy stats
def displayenemystats(enemy):
    global enemymaxhp
    textlines[11] = "life: " + str(enemies[enemy][0][0]) + "    max: " + str(enemymaxhp)
    return


# ►◄▼
def displaymessage(type, attack, enemy, damage):
    textlines[12] = textlines[13]
    textlines[13] = textlines[14]
    if type == "attack":
        textlines[14] = "► You attacked " + enemy + " with " + attack + " and done " + str(damage) + " damage to it"
    elif type == "damage":
        textlines[14] = "◄ You were attacked by " + enemy + " with " + attack + " and received " + str(damage) + " damage"
    elif type == "failrun":
        textlines[14] = "You can not run, " + enemy + " is faster than you.   " + enemy + " speed:" + str(damage)
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
            return True
        if playerinput == "item":
            clearquestion()
            itemmenu()
            return True
        if playerinput == "run":
            clearquestion()
            i = runmenu(enemy)
            if not i:
                return i
            displaymessage("failrun","",enemy,enemies[enemy][0][2])
        else:
            textlines[housedimentions[0] - 2] = playerinput + " is not a valid option"






def itemmenu():
    textlines[19] = "Items:"
    textlines[20] = "* HP Potion   " + str(itemslist["hp potion"][0])  + "  * DMG Potion  " + str(itemslist["dmg potion"][0])
    textlines[21] = "* MAG Potion  " + str(itemslist["mag potion"][0]) + "  * DEF potion  " + str(itemslist["def potion"][0])
    while True:
        textlines[housedimentions[0] - 1] = "which item do you want to use?"
        printscreen()
        playerinput = readinput()
        if playerinput in("hp", "hp potion"):
            if itemslist["hp potion"][0] <=0:
                textlines[housedimentions[0] - 2] = "you do not have enough HP potions "
            else:
                variables.playerstats["hp"] = variables.playerstats["hp"] + itemslist["hp potion"][1]
            return
        elif playerinput in("dmg", "dmg potion"):

            return
        elif playerinput in("mag", "mag potion"):

            return
        elif playerinput in("def", "def potion"):

            return
        else:
            textlines[housedimentions[0] - 2] = playerinput + " is not a valid option"
    return


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


def runmenu(enemy):
    if enemies[enemy][0][2] <= playerstats["spd"]:
        return False
    else:
        return True


# damage the enemy by multiplying the base damage of the player with the attack multiplier
def damageenemy(enemy, attack):
    enemies[enemy][0][0] = enemies[enemy][0][0] - playerstats[attacks[attack][0]] * attacks[attack][1]
    displaymessage("attack", attack, enemy, playerstats[attacks[attack][0]] * attacks[attack][1])
    return
