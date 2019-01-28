from map import *

# text to display
textlines = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
# predefined text for each room
roomtext = {"r1" : ["", "", "", "", "", "", ""],
            "r2" : ["nope", "", "", "", "", "", ""],
            "r3" : ["", "", "", "", "", "", ""],
            "r4" : ["This room is small and empty, the only thing here is a large", "spider's web, which covers one corner of the room from ceiling to floor.", "You start to feel a tingling in the leg, hundreds of spiders try to", "reach you and climb your legs, look up,", "a giant spider is hanging in the web ready to attack ...", "", ""],
            "r5" : ["", "", "", "", "", "", ""],
            "r6" : ["", "", "", "", "", "", ""],
            "r7" : ["", "", "", "", "", "", ""],
            "r8" : ["", "", "", "", "", "", ""],
            "r9" : ["", "", "", "", "", "", ""],
            "r10": ["", "", "", "", "", "", ""],
            "r11": ["", "", "", "", "", "", ""],
            "r12": ["", "", "", "", "", "", ""],
            "r13": ["", "", "", "", "", "", ""],
            "r14": ["This room is small and empty, the only thing here is a large", "spider's web, which covers one corner of the room from ceiling to floor.", "You start to feel a tingling in the leg, hundreds of spiders try to", "reach you and climb your legs, look up,", "a giant spider is hanging in the web ready to attack ...", "", ""],
            "r15": ["", "", "", "", "", "", ""],
            "r16": ["", "", "", "", "", "", ""],
            "r17": ["", "", "", "", "", "", ""],
            "r18": ["", "", "", "", "", "", ""],
            "r19": ["", "", "", "", "", "", ""],
            "h1" : ["nope", "", "", "", "", "", ""],
            "h2" : ["", "", "", "", "", "", ""],
            "h3" : ["", "", "", "", "", "", ""],
            "h4" : ["", "", "", "", "", "", ""],
            "h5" : ["", "", "", "", "", "", ""],
            "h6" : ["", "", "", "", "", "", ""],
            "h7" : ["", "", "", "", "", "", ""],
            }


# gives the option to exit the game at any time
def readinput():
    i = input().lower()
    if i == "exit":
        exit()
    else:
        return i


# gives a new screen by pushing all text up
def newscreen():
    print("\n" * spacebetweenscreens)
    return


# clear description of room
def clearscreen():
    clearline(4)
    clearline(5)
    clearline(6)
    clearline(7)
    clearline(8)
    clearline(9)
    clearline(10)


# clear an individual line
def clearline(linenumber):
    textlines[linenumber] = ""


# clear bottom 2 lines (the question, and the wrong input message)
def clearquestion():
    clearline(housedimentions[0] - 1)
    clearline(housedimentions[0] - 2)


# clear the main menu
def clearoptions():
    clearline(11)
    clearline(12)
    clearline(13)
    clearline(14)
    clearline(15)


# clear the secondary menu
def clearextra():
    clearline(16)
    clearline(17)
    clearline(18)
    clearline(19)
    clearline(20)
    clearline(21)


# clear the secondary figth menu
def clearsecondaryfightmenu():
    clearline(19)
    clearline(20)
    clearline(21)


# print the entire screen
def printscreen():
    newscreen()
    i = 0
    while i < housedimentions[0]:
        print(textlines[i].ljust(maxLength), houselines[i])
        i += 1


# update description of room
def updateroomtext(room):
    i = 0
    while i < spacefordescription:
        textlines[i+4] = roomtext[room][i]
        i = i+1


def updateplayerstats():
    textlines[0] = str(playerstats["hp"])
    textlines[2] = "Dmg: " + str(playerstats["dmg"]) + "  Mag: " + str(playerstats["mag"]) + "  Def: " + str(playerstats["def"]) + "  Spd: " + str(playerstats["spd"])
