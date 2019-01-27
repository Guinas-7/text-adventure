
from fighting import *

inventory = []


roomoptions = ["move", "explore", "manage", "extra"]


def choseoption():
    # activates the fighting menu if there is an enemie in that room(room info table) and if that enemie is not dead
    if rooms[playerpossition][0][0] != "" and enemies[rooms[playerpossition][0][0]][0][0] != 0:
        return startfight(rooms[playerpossition][0][0])
    textlines[11] = "you can do all of these:"
    textlines[12] = " * " + rooms[playerpossition][3][0]
    textlines[13] = " * " + rooms[playerpossition][3][1]
    textlines[14] = " * " + rooms[playerpossition][3][2]
    textlines[15] = " * " + rooms[playerpossition][3][3]
    while True:
        textlines[housedimentions[0] - 1] = "what do you want to do? " + playerpossition + playerlastpossition
        printscreen()
        playerinput = readinput()
        if playerinput == roomoptions[0]:
            return directionchoice()
        elif playerinput == roomoptions[1]:
            exploremenu()
            return
        elif playerinput == roomoptions[2]:
            managemenu()
            return
        elif playerinput == roomoptions[3]:
            blankmenu()
            return
        else:
            textlines[housedimentions[0] - 2] = playerinput + " is not a valid option"


def directionchoice():
    global playerpossition
    textlines[16] = "you can move in these directions:"
    if rooms[playerpossition][2][0] != "":
        textlines[17] = "north"
    else:
        textlines[17] = ""
    if rooms[playerpossition][2][2] != "":
        textlines[18] = "south"
    else:
        textlines[18] = ""
    if rooms[playerpossition][2][1] != "":
        textlines[19] = "east"
    else:
        textlines[19] = ""
    if rooms[playerpossition][2][3] != "":
        textlines[20] = "west"
    else:
        textlines[20] = ""

    while True:
        textlines[housedimentions[0]-1] = "which direction do you want to move in?"
        printscreen()
        playerinput = readinput()
        if playerinput in north and rooms[playerpossition][2][0] != "":
            updateplayerlastpossition(playerpossition)
            clearquestion()
            playerpossition = rooms[playerpossition][2][0]
            updateroom(playerpossition)
            return playerpossition
        elif playerinput in east and rooms[playerpossition][2][1] != "":
            updateplayerlastpossition(playerpossition)
            clearquestion()
            playerpossition = rooms[playerpossition][2][1]
            updateroom(playerpossition)
            return playerpossition
        elif playerinput in south and rooms[playerpossition][2][2] != "":
            updateplayerlastpossition(playerpossition)
            clearquestion()
            playerpossition = rooms[playerpossition][2][2]
            updateroom(playerpossition)
            return playerpossition
        elif playerinput in west and rooms[playerpossition][2][3] != "":
            updateplayerlastpossition(playerpossition)
            clearquestion()
            playerpossition = rooms[playerpossition][2][3]
            updateroom(playerpossition)
            return playerpossition
        elif playerinput in back:
            clearquestion()
            return
        else:
            textlines[housedimentions[0]-2] = playerinput + " is not a valid option"


def updateplayerlastpossition(possition):
    global playerlastpossition
    playerlastpossition = possition


def exploremenu():
    return


def managemenu():
    return


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
