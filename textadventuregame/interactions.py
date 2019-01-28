from fighting import *
from random import randint
import variables
import map
import fighting


itemlist = {"wood sword"      :["dmg",2],
             "staff"          :["mag",4],
             "shoe"           :["spd",10],
             "chestplate"     :["def",5],
             "iron sword"     :["dmg",8],
             "shield"         :["def",7],
             "master sword"   :["dmg",15],
             "ability scroll" :["exp",1],
             "potion"         :["exp",1]
             }


# main menu
def choseoption():
    textlines[1] = "player possition:   " + variables.playerpossition
    # activates the fighting menu if there is an enemie in that room(room info table) and if that enemie is not dead
    if rooms[variables.playerpossition][0][0] != "" and enemies[rooms[variables.playerpossition][0][0]][0][0] > 0:
        return startfight(rooms[variables.playerpossition][0][0])
    textlines[11] = "you can do these:"
    textlines[12] = " * " + rooms[variables.playerpossition][3][0]
    textlines[13] = " * " + rooms[variables.playerpossition][3][1]
    textlines[14] = " * " + rooms[variables.playerpossition][3][2]
    while True:
        textlines[housedimentions[0] - 1] = "what do you want to do?"
        printscreen(houselines)
        playerinput = readinput()
        if playerinput == rooms[variables.playerpossition][3][0] and playerinput != "":
            return directionchoice()
        elif playerinput == rooms[variables.playerpossition][3][1] and playerinput != "":
            lootmenu()
            clearquestion()
            return variables.playerpossition
        elif playerinput == rooms[variables.playerpossition][3][2] and playerinput != "":
            cheatsmenu()
            clearquestion()
            return variables.playerpossition

        else:
            textlines[housedimentions[0] - 2] = playerinput + " is not a valid option."


# move secondary menu
def directionchoice():
    # only shows the available directions saved in the room layout table
    textlines[16] = "you can move in these directions:"
    if rooms[variables.playerpossition][2][0] != "":
        textlines[17] = " * north"
    else:
        textlines[17] = ""
    if rooms[variables.playerpossition][2][2] != "":
        textlines[18] = " * south"
    else:
        textlines[18] = ""
    if rooms[variables.playerpossition][2][1] != "":
        textlines[19] = " * east"
    else:
        textlines[19] = ""
    if rooms[variables.playerpossition][2][3] != "":
        textlines[20] = " * west"
    else:
        textlines[20] = ""

    while True:
        textlines[housedimentions[0]-1] = "which direction do you want to move in?"
        printscreen(houselines)
        playerinput = readinput()
        if playerinput in north and rooms[variables.playerpossition][2][0] != "":
            updateplayerlastpossition(variables.playerpossition)
            clearquestion()
            variables.playerpossition = rooms[variables.playerpossition][2][0]
            updateroom(variables.playerpossition)
            return variables.playerpossition
        elif playerinput in east and rooms[variables.playerpossition][2][1] != "":
            updateplayerlastpossition(variables.playerpossition)
            clearquestion()
            variables.playerpossition = rooms[variables.playerpossition][2][1]
            updateroom(variables.playerpossition)
            return variables.playerpossition
        elif playerinput in south and rooms[variables.playerpossition][2][2] != "":
            updateplayerlastpossition(variables.playerpossition)
            clearquestion()
            variables.playerpossition = rooms[variables.playerpossition][2][2]
            updateroom(variables.playerpossition)
            return variables.playerpossition
        elif playerinput in west and rooms[variables.playerpossition][2][3] != "":
            updateplayerlastpossition(variables.playerpossition)
            clearquestion()
            variables.playerpossition = rooms[variables.playerpossition][2][3]
            updateroom(variables.playerpossition)
            return variables.playerpossition
        elif playerinput in back:
            clearquestion()
            return
        else:
            textlines[housedimentions[0]-2] = playerinput + " is not a valid option."


# saves the last position of the player
def updateplayerlastpossition(possition):
    variables.playerlastpossition = possition
    return


# loot secondary menu
def lootmenu():
    item = rooms[variables.playerpossition][4][0]
    map.rooms[variables.playerpossition][3][1] = ""
    if item == "ability scroll":
        addability("frenzy")
    elif item == "potion":
        addpotion()
    else:
        additem(item)
    return


def addpotion():
    fighting.potionlist["hp potion"][0] = fighting.potionlist["hp potion"][0] + randint(0, 3)
    fighting.potionlist["dmg potion"][0] = fighting.potionlist["dmg potion"][0] + randint(0, 1)
    fighting.potionlist["mag potion"][0] = fighting.potionlist["mag potion"][0] + randint(0, 1)
    fighting.potionlist["def potion"][0] = fighting.potionlist["def potion"][0] + randint(0, 1)
    textlines[housedimentions[0] - 1] = "You fond some potion that can be used in battle."
    printscreen(houselines)
    readinput()
    return


def additem(item):
    variables.playerstats[itemlist[item][0]] = variables.playerstats[itemlist[item][0]] + itemlist[item][1]
    updateplayerstats()
    textlines[housedimentions[0] - 1] = "You fond a " + item + ", your " + itemlist[item][0] + " increased by " + str(itemlist[item][1]) + ". Press enter to continue."
    printscreen(houselines)
    readinput()
    return


def addability(ability):
    playerattacks[2] = ability
    textlines[housedimentions[0] - 1] = "You fond an ability scroll, now you can use " + ability + " in combat. Press enter to continue."
    printscreen(houselines)
    readinput()
    return


# cheats
def cheatsmenu():
    textlines[housedimentions[0] - 1] = "Do you want to all 10 points to all your stats??"
    printscreen(houselines)
    playerinput = readinput()
    if playerinput in positiveanswer:
        variables.playerstats["dmg"] = variables.playerstats["dmg"] + 10
        variables.playerstats["mag"] = variables.playerstats["mag"] + 10
        variables.playerstats["def"] = variables.playerstats["def"] + 10
        variables.playerstats["spd"] = variables.playerstats["spd"] + 10
        updateplayerstats()
    elif playerinput in negativeanswer:
        textlines[housedimentions[0] - 1] = "Good decision. Press enter to continue."
        printscreen(houselines)
        readinput()
    else:
        textlines[housedimentions[0] - 2] = playerinput + " is not an option."
    return

