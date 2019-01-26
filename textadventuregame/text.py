from map import *

textlines = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]


def clearscreen():
    print("\n" * 50)
    return




def printscreen():
    i = 0
    while i < housedimentions[0]:
        print(textlines[i].ljust(maxLength), houselines[i])
        i += 1
