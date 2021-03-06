from text import *
import variables
import random

playerattacks = ["swing", "fireball", "pass", "pass"]

potionlist = {"hp potion" :[1, 650],
             "dmg potion":[0, 1],
             "mag potion":[0, 1],
             "def potion":[0, 1]
             }

# enemies stats:[HP,DMG,SPD],attacks
enemies = {"spider1": [[20 , 10, 4 ], ["bite"          ,"web trow" ,"pass"        ]],
           "spider2": [[150, 25, 25], ["small spiders" ,"bite"     ,"pass"        ]],
           "blob1"  : [[35 , 13, 5 ], ["swallow"       ,"spit"     ,"pass"        ]],
           "blob2"  : [[250, 35, 15], ["spit"          ,"swallow"  ,"pass"        ]],
           "plant1" : [[65 , 17, 7 ], ["whip"          ,"squeeze"  ,"pass"        ]],
           "zombie1": [[90 , 20, 2 ], ["bite"          ,"scratch"  ,"pass"        ]],
           "dragon" : [[999, 50, 20], ["bite"          ,"fireball" ,"fire tornado"]]
           }
# name of attack and damagemultiplierr
enemyattacks = {"pass"            : [0],
                "bite"            : [2],
                "web trow"        : [1],
                "small spiders"   : [1.6],
                "swallow"         : [2],
                "spit"            : [1.4],
                "scratch"         : [1.3],
                "fireball"        : [2.5],
                "fire tornado"    : [3],
                "whip"            : [1.5],
                "squeeze"         : [2]
                }

# list of attacks - name of attack:[category,damage,wait time]
attacks = {"pass"     : ["dmg", 0  ,0],
           "swing"    : ["dmg", 1.3,1],
           "fireball" : ["mag", 1.6,1],
           "frenzy"   : ["dmg", 3  ,5]
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
    while True:
        displayenemystats(enemy)
        textlines[housedimentions[0] - 1] = "Do you want to start a fight with " + enemy + "?"
        printscreen(enemylines[enemy])
        playerinput = readinput()
        if playerinput in positiveanswer:
            saveplayerstats()
            clearquestion()
            if fightmain(enemy):
                if enemy == "dragon":
                    textlines[housedimentions[0] - 1] = "you killed the boss congratulations. write exit to finish game"
                    printscreen(enemylines[enemy])
                    readinput()
                reverseplayerstats()
                return variables.playerpossition
            else:
                reverseplayerstats()
                return variables.playerlastpossition
        elif playerinput in negativeanswer:
            clearquestion()
            return variables.playerlastpossition
        else:
            textlines[housedimentions[0] - 2] = playerinput + " is not a valid option."


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
                if enemies[enemy][0][0] > 0:
                    textlines[housedimentions[0] - 1] = "Press enter to continue."
                    printscreen(enemylines[enemy])
                    readinput()
                    enemyattack(enemy)
                else:
                    textlines[housedimentions[0] - 1] = "you killed " + enemy + ". Press enter to continue."
                    printscreen(enemylines[enemy])
                    readinput()
                updateplayerstats()
            else:
                return False


def enemyattack(enemy):
    attack = random.choice(enemies[enemy][1])
    variables.playerstats["hp"] = variables.playerstats["hp"] - (enemyattacks[attack][0] * enemies[enemy][0][1] - playerstats["def"])
    displaymessage("damage", attack, enemy, enemyattacks[attack][0] * enemies[enemy][0][1] - playerstats["def"])
    return


# updates lines with enemy stats
def displayenemystats(enemy):
    global enemymaxhp
    textlines[11] = "life: " + str(enemies[enemy][0][0]) + "    max: " + str(enemymaxhp)
    return


# ►◄▼
def displaymessage(category, attack, enemy, damage):
    textlines[12] = textlines[13]
    textlines[13] = textlines[14]
    if category == "attack":
        textlines[14] = "> You attacked " + enemy + " with " + attack + " and done " + str(damage) + " damage to it."
    elif category == "damage":
        textlines[14] = "< You were attacked by " + enemy + " with " + attack + " and received " + str(damage) + " damage."
    elif category == "failrun":
        textlines[14] = "You can not run, " + enemy + " is faster than you.   " + enemy + " speed:" + str(damage)+"."
    elif category == "potion":
        textlines[14] = "v You took a " + attack + " potion and got" + str(damage) + attack + " points."
    return


def fightoptionsmenu(enemy):
    global enemies
    textlines[15] = "MENU:"
    textlines[16] = "* Attack"
    textlines[17] = "* Item           * Run"

    while True:
        clearsecondaryfightmenu()
        textlines[housedimentions[0] - 1] = "What do you want to do?"
        printscreen(enemylines[enemy])
        playerinput = readinput()
        if playerinput == "attack":
            clearquestion()
            atackmenu(enemy)
            return True
        elif playerinput == "item":
            clearquestion()
            if itemmenu(enemy):
                return True
        elif playerinput == "run":
            clearquestion()
            i = runmenu(enemy)
            if not i:
                enemies[enemy][0][0] = enemymaxhp
                return i
            displaymessage("failrun", "", enemy, enemies[enemy][0][2])
        else:
            textlines[housedimentions[0] - 2] = playerinput + " is not on the menu"


def itemmenu(enemy):
    global potionlist
    textlines[19] = "Items:"
    textlines[20] = "* HP Potion   " + str(potionlist["hp potion"][0])  + "  * DMG Potion  " + str(potionlist["dmg potion"][0])
    textlines[21] = "* MAG Potion  " + str(potionlist["mag potion"][0]) + "  * DEF potion  " + str(potionlist["def potion"][0])
    while True:
        textlines[housedimentions[0] - 1] = "Which item do you want to use?"
        printscreen(enemylines[enemy])
        playerinput = readinput()
        if playerinput in("hp", "hp potion"):
            if potionlist["hp potion"][0] <= 0:
                textlines[housedimentions[0] - 2] = "You do not have enough HP potions."
            else:
                potionlist["hp potion"][0] = potionlist["hp potion"][0] - 1
                displaymessage("potion", "Health", "", potionlist["hp potion"][1])
                variables.playerstats["hp"] = variables.playerstats["hp"] + potionlist["hp potion"][1]
                if variables.playerstats["hp"] > variables.playerstats["maxhp"]:
                    variables.playerstats["hp"] = variables.playerstats["maxhp"]
            return True
        elif playerinput in("dmg", "dmg potion"):
            if potionlist["dmg potion"][0] <= 0:
                textlines[housedimentions[0] - 2] = "You do not have enough DMG potions."
            else:
                potionlist["dmg potion"][0] = potionlist["dmg potion"][0] - 1
                displaymessage("potion", "DMG", "", potionlist["dmg potion"][1])
                variables.playerstats["dmg"] = variables.playerstats["dmg"] + potionlist["dmg potion"][1]
            return True
        elif playerinput in("mag", "mag potion"):
            if potionlist["mag potion"][0] <= 0:
                textlines[housedimentions[0] - 2] = "You do not have enough MAG potions."
            else:
                potionlist["mag potion"][0] = potionlist["mag potion"][0] - 1
                displaymessage("potion", "MAG", "", potionlist["mag potion"][1])
                variables.playerstats["mag"] = variables.playerstats["mag"] + potionlist["mag potion"][1]
            return True
        elif playerinput in("def", "def potion"):
            if potionlist["def potion"][0] <= 0:
                textlines[housedimentions[0] - 2] = "You do not have enough DEF potions."
            else:
                potionlist["mag potion"][0] = potionlist["mag potion"][0] - 1
                displaymessage("potion", "DEF", "", potionlist["def potion"][1])
                variables.playerstats["def"] = variables.playerstats["def"] + potionlist["def potion"][1]
            return True
        elif playerinput in ("cancel", "back"):
            return False
        else:
            textlines[housedimentions[0] - 2] = playerinput + " is not an item you can use."


def atackmenu(enemy):
    textlines[19] = "Attack:"
    textlines[20] = "* " + playerattacks[0] + "".join([" " for x in range(1, 20-len(playerattacks[0]))]) + "* " + playerattacks[2]
    textlines[21] = "* " + playerattacks[1] + "".join([" " for x in range(1, 20-len(playerattacks[1]))]) + "* " + playerattacks[3]
    while True:
        textlines[housedimentions[0] - 1] = "Choose an attack."
        printscreen(enemylines[enemy])
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
            textlines[housedimentions[0] - 2] = "You do not have the " + playerinput + " attack."


def runmenu(enemy):
    if enemies[enemy][0][2] <= playerstats["spd"]:
        return False
    else:
        return True


# damage the enemy by multiplying the base damage of the player with the attack multiplier
def damageenemy(enemy, attack):
    enemies[enemy][0][0] = enemies[enemy][0][0] - (playerstats[attacks[attack][0]] * attacks[attack][1])
    displaymessage("attack", attack, enemy, playerstats[attacks[attack][0]] * attacks[attack][1])
    return
