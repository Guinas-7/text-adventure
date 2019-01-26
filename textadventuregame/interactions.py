from text import *
from fighting import *
playerpossition = "r1"
inventory = []

positiveanswer = ["yes", "sure"]
negativeanswer = ["no", "nope"]
north = ["north", "up", "top"]
south = ["south", "down", "bottom"]
east = ["east", "right"]
west = ["west", "left"]
back = ["back", "previous", "cancel"]

roomoptions = ["move", "explore", "manage", "extra"]





def readinput():
    i = input().lower()
    if i == "exit":
        exit()
    else:
        return i


def choseoption():
    textlines[11] = "you can do all of these:"
    while True:
        textlines[housedimentions[0] - 1] = "what do you want to do?"
        printscreen()
        playerinput = readinput()
        if playerinput == roomoptions[0]:
            movemenu()
            return
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


def movemenu():
    return


def exploremenu():
    return


def managemenu():
    return


def blankmenu():
    return


def directionchoice():
    global playerpossition
    if playerpossition[0] == "h":
        tipo = halls
    elif playerpossition[0] == "r":
        tipo = rooms
    else:
        return

    while True:
        textlines[housedimentions[0]-1] = "which direction do you want to move in?"
        printscreen()
        playerinput = readinput()
        if playerinput in north and tipo[playerpossition][2][0] != "":
            clearquestion()
            playerpossition = tipo[playerpossition][2][0]
            updateroom(playerpossition)
            return 1
        elif playerinput in east and tipo[playerpossition][2][1] != "":
            clearquestion()
            playerpossition = tipo[playerpossition][2][1]
            updateroom(playerpossition)
            return 2
        elif playerinput in south and tipo[playerpossition][2][2] != "":
            clearquestion()
            playerpossition = tipo[playerpossition][2][2]
            updateroom(playerpossition)
            return 3
        elif playerinput in west and tipo[playerpossition][2][3] != "":
            clearquestion()
            playerpossition = tipo[playerpossition][2][3]
            updateroom(playerpossition)
            return 4
        elif playerinput in back:
            clearquestion()
            return 0
        else:
            textlines[housedimentions[0]-2] = playerinput + " is not a valid option"


def startfight():
    while True:
        textlines[housedimentions[0] - 1] = "Do you want to start a fight with "
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


