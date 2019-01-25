import numpy as np
charratio = 2
housedimentions = [22, 33*charratio]
maxLength = 80
display = np.zeros((housedimentions[0], housedimentions[1], 5), dtype=np.int64)
# display = [[[0 for col in range(housedimentions[0])]for row in range(housedimentions[1])] for x in range(5)]



houselines = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
textlines = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]

houseshape = {"room1": [True, [[0*charratio, 0], [5*charratio, 7]]],
              "room2": [True, [[0*charratio, 7], [10*charratio, 21]]],
              "room3": [True, [[5*charratio, 2], [10*charratio, 7]]],
              "room4": [True, [[28*charratio, 0], [32*charratio, 7]]],
              "room5": [True, [[25*charratio, 0], [28*charratio, 7]]],
              "room6": [True, [[10*charratio, 0], [25*charratio, 21]]],
              "room7": [True, [[25*charratio, 7], [30*charratio, 10]]],
              "room8": [True, [[25*charratio, 10], [32*charratio, 21]]],
              }


housesymbolcode = {" ": "[[0 0 0 0 0]]",
                   "╔": "[[0 1 1 0 0]]",
                   "╗": "[[0 1 0 1 0]]",
                   "╚": "[[1 0 1 0 0]]",
                   "╝": "[[1 0 0 1 0]]",
                   "║": "[[1 1 0 0 0]]",
                   "═": "[[0 0 1 1 0]]",
                   "╠": "[[1 1 1 0 0]]",
                   "╣": "[[1 1 0 1 0]]",
                   "╦": "[[0 1 1 1 0]]",
                   "╩": "[[1 0 1 1 0]]",
                   "╬": "[[1 1 1 1 0]]",
                   "│": "[[0 0 0 1 0]]",
                   "─": "[[0 0 1 0 0]]",

                   "A": "[[0 0 0 0 1]]",
                   "B": "[[0 0 0 1 1]]",
                   "C": "[[0 0 1 0 1]]",
                   "D": "[[0 0 1 1 1]]",
                   "E": "[[0 1 0 0 1]]",
                   "F": "[[0 1 0 1 1]]",
                   "G": "[[0 1 1 0 1]]",
                   "H": "[[0 1 1 1 1]]",
                   "I": "[[1 0 0 0 1]]",
                   "J": "[[1 0 0 1 1]]",
                   "K": "[[1 0 1 0 1]]",
                   "L": "[[1 0 1 1 1]]",
                   "M": "[[1 1 0 0 1]]",
                   "N": "[[1 1 0 1 1]]",
                   "O": "[[1 1 1 0 1]]",
                   "P": "[[1 1 1 1 1]]",
                   }


def clearScreen():
    print("\n" * 50)
    return


# update symbol table
def updateroom(room):
    global display
    # X and Y of top-left corner of room
    ix = houseshape[room][1][0][0]
    iy = houseshape[room][1][0][1]
    if houseshape[room][0]:
        # defining top-left corner of room
        display[houseshape[room][1][0][1], houseshape[room][1][0][0], 1] = 1
        display[houseshape[room][1][0][1], houseshape[room][1][0][0], 2] = 1
        # defining top-right corner of room
        display[houseshape[room][1][0][1], houseshape[room][1][1][0], 1] = 1
        display[houseshape[room][1][0][1], houseshape[room][1][1][0], 3] = 1
        # defining bottom-left corner of room
        display[houseshape[room][1][1][1], houseshape[room][1][0][0], 0] = 1
        display[houseshape[room][1][1][1], houseshape[room][1][0][0], 2] = 1
        # defining bottom-right corner of room
        display[houseshape[room][1][1][1], houseshape[room][1][1][0], 0] = 1
        display[houseshape[room][1][1][1], houseshape[room][1][1][0], 3] = 1

        # defining top and bottom wall of room
        while ix + 1 < (houseshape[room][1][1][0]):
            display[houseshape[room][1][0][1], ix+1, 2] = 1
            display[houseshape[room][1][0][1], ix+1, 3] = 1
            display[houseshape[room][1][1][1], ix+1, 2] = 1
            display[houseshape[room][1][1][1], ix+1, 3] = 1
            ix += 1

        # defining left and right wall of room
        while iy+1 < (houseshape[room][1][1][1]):
            display[iy+1, houseshape[room][1][0][0], 0] = 1
            display[iy+1, houseshape[room][1][0][0], 1] = 1
            display[iy+1, houseshape[room][1][1][0], 0] = 1
            display[iy+1, houseshape[room][1][1][0], 1] = 1
            iy += 1


# transform table into string
def updatehouseline(line):
    houselines[line] = ""
    i = 0
    while i < housedimentions[1]:
        houselines[line] = houselines[line].__add__(str(codetranslator(display[[line], [i]])))
        i += 1


# translate code into symbol
def codetranslator(activecode):
    for symbol, code in housesymbolcode.items():
        if str(code) == str(activecode):

            return symbol


def readInput():
    i = input().lower()
    if i == "exit":
        exit()
    else:
        return i


def printscreen():
    i = 0
    while i < housedimentions[0]:
        print(textlines[i].ljust(maxLength), houselines[i])
        i += 1


updateroom("room1")
updateroom("room2")
updateroom("room3")
updateroom("room4")
updateroom("room5")
updateroom("room6")
updateroom("room7")
updateroom("room8")



e = 0
while e < housedimentions[0]:
    updatehouseline(e)
    e += 1

while True:
    clearScreen()
    printscreen()
    readInput()
