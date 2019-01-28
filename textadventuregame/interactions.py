from fighting import *
import variables
import map


roomoptions = ["move", "loot", "manage", "extra"]

itemlist = {"wood sword"      :["dmg",2],
             "staff"          :["mag",4],
             "shoe"           :["spd",10],
             "chestplate"     :["def",5],
             "iron sword"     :["dmg",8],
             "shield"         :["def",7],
             "master sword"   :["dmg",15],
             "ability scroll" :["exp",1],
             }


# main menu
def choseoption():
    # activates the fighting menu if there is an enemie in that room(room info table) and if that enemie is not dead
    if rooms[variables.playerpossition][0][0] != "" and enemies[rooms[variables.playerpossition][0][0]][0][0] > 0:

        return startfight(rooms[variables.playerpossition][0][0])
    textlines[11] = "you can do all of these:"
    textlines[12] = " * " + rooms[variables.playerpossition][3][0]
    textlines[13] = " * " + rooms[variables.playerpossition][3][1]
    textlines[14] = " * " + rooms[variables.playerpossition][3][2]
    textlines[15] = " * " + rooms[variables.playerpossition][3][3]
    while True:
        textlines[housedimentions[0] - 1] = "what do you want to do?"
        printscreen()
        playerinput = readinput()
        if playerinput == roomoptions[0]:
            return directionchoice()
        elif playerinput == roomoptions[1]:
            lootmenu()
            return variables.playerpossition
        elif playerinput == roomoptions[2]:
            managemenu()
            return variables.playerpossition
        elif playerinput == roomoptions[3]:
            blankmenu()
            return variables.playerpossition
        else:
            textlines[housedimentions[0] - 2] = playerinput + " is not a valid option"


# move secondary menu
def directionchoice():
    # only shows the available directions saved in the room layout table
    textlines[16] = "you can move in these directions:"
    if rooms[variables.playerpossition][2][0] != "":
        textlines[17] = "north"
    else:
        textlines[17] = ""
    if rooms[variables.playerpossition][2][2] != "":
        textlines[18] = "south"
    else:
        textlines[18] = ""
    if rooms[variables.playerpossition][2][1] != "":
        textlines[19] = "east"
    else:
        textlines[19] = ""
    if rooms[variables.playerpossition][2][3] != "":
        textlines[20] = "west"
    else:
        textlines[20] = ""

    while True:
        textlines[housedimentions[0]-1] = "which direction do you want to move in?"
        printscreen()
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
            textlines[housedimentions[0]-2] = playerinput + " is not a valid option"


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
    else:
        additem(item)
    print(item)

    return


def additem(item):
    variables.playerstats[itemlist[item][0]] = variables.playerstats[itemlist[item][0]] + itemlist[item][1]
    updateplayerstats()
    textlines[housedimentions[0] - 1] = "You fond a " + item +", your " + itemlist[item][0] + " increased by " + str(itemlist[item][1]) + ". Press enter to continue"
    printscreen()
    readinput()


def addability(ability):
    playerattacks[2] = ability
    textlines[housedimentions[0] - 1] = "You fond an ability scroll, now you can use " + ability + " in combat. Press enter to continue"
    printscreen()
    readinput()
    return
# management secondary menu
def managemenu():
    return


# extra secondary menu
def blankmenu():
    return


def keepitem(item):
    while True:
        textlines[housedimentions[0] - 1] = "Do you want to keep the " + item
        printscreen()
        playerinput = readinput()
        if playerinput in positiveanswer:
            clearquestion()
            return True
        elif playerinput in negativeanswer:
            clearquestion()
            return False
        else:
            textlines[housedimentions[0] - 2] = playerinput + " is not a valid option"
