from text import *
from fighting import *

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
    textlines[12] = "move"
    textlines[13] = "explore"
    textlines[14] = "manage"
    textlines[15] = "extra"
    while True:
        textlines[housedimentions[0] - 1] = "what do you want to do?"
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



def exploremenu():
    return


def managemenu():
    return


def blankmenu():
    return


def directionchoice():
    global playerpossition
    textlines[16] = "you can move in these directions:"
    textlines[17] = "north"
    textlines[18] = "south"
    textlines[19] = "east"
    textlines[20] = "west"
    while True:
        textlines[housedimentions[0]-1] = "which direction do you want to move in?"
        printscreen()
        playerinput = readinput()
        if playerinput in north and rooms[playerpossition][2][0] != "":
            clearquestion()
            playerpossition = rooms[playerpossition][2][0]
            updateroom(playerpossition)
            return playerpossition
        elif playerinput in east and rooms[playerpossition][2][1] != "":
            clearquestion()
            playerpossition = rooms[playerpossition][2][1]
            updateroom(playerpossition)
            return playerpossition
        elif playerinput in south and rooms[playerpossition][2][2] != "":
            clearquestion()
            playerpossition = rooms[playerpossition][2][2]
            updateroom(playerpossition)
            return playerpossition
        elif playerinput in west and rooms[playerpossition][2][3] != "":
            clearquestion()
            playerpossition = rooms[playerpossition][2][3]
            updateroom(playerpossition)
            return playerpossition
        elif playerinput in back:
            clearquestion()
            return
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
