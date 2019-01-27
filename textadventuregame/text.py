from map import *


textlines = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
roomtext = {"r1" : ["teste", "ola", "khac", "fsbgdhbdfb", "dfgbdhfhfgbsfvdsfbvdsfb", "dsbvd", "sdvbdvbsfvsdfvsdv"],
            "r2" : ["nope", "", "", "", "", "", ""],
            "r3" : ["", "", "", "", "", "", ""],
            "r4" : ["", "oioioioioioioioi", "", "", "", "", ""],
            "r5" : ["", "", "", "", "", "", ""],
            "r6" : ["", "", "", "", "", "", ""],
            "r7" : ["", "", "", "", "", "", ""],
            "r8" : ["", "", "", "", "", "", ""],
            "r9" : ["", "", "", "", "", "", ""],
            "r10": ["", "", "", "", "", "", ""],
            "r11": ["", "", "", "", "", "", ""],
            "r12": ["", "", "", "", "", "", ""],
            "r13": ["", "", "", "", "", "", ""],
            "r14": ["", "", "", "", "", "", ""],
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


def readinput():
    i = input().lower()
    if i == "exit":
        exit()
    else:
        return i


def newscreen():
    print("\n" * spacebetweenscreens)
    return


def clearscreen():
    clearline(4)
    clearline(5)
    clearline(6)
    clearline(7)
    clearline(8)
    clearline(9)
    clearline(10)


def clearline(linenumber):
    textlines[linenumber] = ""


def clearquestion():
    clearline(housedimentions[0] - 1)
    clearline(housedimentions[0] - 2)


def clearoptions():
    clearline(11)
    clearline(12)
    clearline(13)
    clearline(14)
    clearline(15)


def clearextra():
    clearline(16)
    clearline(17)
    clearline(18)
    clearline(19)
    clearline(20)


def printscreen():
    newscreen()
    i = 0
    while i < housedimentions[0]:
        print(textlines[i].ljust(maxLength), houselines[i])
        i += 1


def updateroomtext(room):
    i = 0
    while i < spacefordescription:
        textlines[i+4] = roomtext[room][i]
        i = i+1


def updateplayerstats():
    textlines[0] = str(playerstats["hp"])
    textlines[2] = "Str: " + str(playerstats["str"]) + "  Spd: " + str(playerstats["spd"])
