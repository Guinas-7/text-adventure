import numpy as np
playerpossition = "r1"
charratio = 3
housedimentions = [25, 37*charratio]
maxLength = 80
display = np.zeros((housedimentions[0], housedimentions[1], 5), dtype=np.int64)
# display = [[[0 for col in range(housedimentions[0])]for row in range(housedimentions[1])] for x in range(5)]


houselines = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",""]

rooms = {"r1": [True, [[0*charratio, 8], [3*charratio, 16]],["","h1","",""]],
         "r2": [False, [[4*charratio, 12], [6*charratio, 14]],["h1","","",""]],
         "r3": [False, [[4*charratio, 9], [6*charratio, 11]],["","","h1",""]],
         "r4": [False, [[7*charratio, 10], [10*charratio, 13]],["h2","","r8","h1"]],
         "r5": [False, [[9*charratio, 5], [12*charratio, 9]],["","","h2",""]],
         "r6": [False, [[6*charratio, 3], [8*charratio, 8]],["r7","h2","",""]],
         "r7": [False, [[7*charratio, 1], [10*charratio, 3]],["","","r6",""]],
         "r8": [False, [[9*charratio, 13], [11*charratio, 17]],["r4","","r9",""]],
         "r9": [False, [[10*charratio, 17], [12*charratio, 19]],["r8","h4","r10",""]],
         "r10": [False, [[6*charratio, 19], [11*charratio, 24]],["r9","","","r11"]],
         "r11": [False, [[1*charratio, 17], [6*charratio, 20]],["","r10","h3",""]],
         "r12": [False, [[2*charratio, 22], [4*charratio, 24]],["h3","","",""]],
         "r13": [False, [[14*charratio, 17], [18*charratio, 21]],["h5","","","h4"]],
         "r14": [False, [[15*charratio, 14], [18*charratio, 16]],["","","","h5"]],
         "r15": [False, [[14*charratio, 8], [18*charratio, 13]],["h6","h7","h5",""]],
         "r16": [False, [[18*charratio, 6], [20*charratio, 10]],["r17","","",""]],
         "r17": [False, [[18*charratio, 3], [21*charratio, 6]],["","","r16","h6"]],
         "r18": [False, [[14*charratio, 2], [17*charratio, 7]],["","h6","",""]],
         "r19": [False, [[21*charratio, 9], [25*charratio, 13]],["","","","h7"]],
         "h1": [False, [[3*charratio, 11], [7*charratio, 12]],["r3","r4","r2","r1"]],
         "h2": [False, [[8*charratio, 7], [9*charratio, 10]],["","r5","r4","r6"]],
         "h3": [False, [[2*charratio, 20], [3*charratio, 22]],["r11","","r12",""]],
         "h4": [False, [[12*charratio, 18], [14*charratio, 19]],["","r13","","r9"]],
         "h5": [False, [[14*charratio, 13], [15*charratio, 17]],["r15","r14","r13",""]],
         "h6": [False, [[17*charratio, 5], [18*charratio, 8]],["","r17","r15","r18"]],
         "h7": [False, [[18*charratio, 11], [21*charratio, 12]],["","r19","","r15"]],
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


# update symbol table
def updateroom(room):
    global display
    # X and Y of top-left corner of room
    ix = rooms[room][1][0][0]
    iy = rooms[room][1][0][1]
    # defining top-left corner of room
    display[rooms[room][1][0][1], rooms[room][1][0][0], 1] = 1
    display[rooms[room][1][0][1], rooms[room][1][0][0], 2] = 1
    # defining top-right corner of room
    display[rooms[room][1][0][1], rooms[room][1][1][0], 1] = 1
    display[rooms[room][1][0][1], rooms[room][1][1][0], 3] = 1
    # defining bottom-left corner of room
    display[rooms[room][1][1][1], rooms[room][1][0][0], 0] = 1
    display[rooms[room][1][1][1], rooms[room][1][0][0], 2] = 1
    # defining bottom-right corner of room
    display[rooms[room][1][1][1], rooms[room][1][1][0], 0] = 1
    display[rooms[room][1][1][1], rooms[room][1][1][0], 3] = 1

    # defining top and bottom wall of room
    while ix + 1 < (rooms[room][1][1][0]):
        display[rooms[room][1][0][1], ix+1, 2] = 1
        display[rooms[room][1][0][1], ix+1, 3] = 1
        display[rooms[room][1][1][1], ix+1, 2] = 1
        display[rooms[room][1][1][1], ix+1, 3] = 1
        ix += 1

    # defining left and right wall of room
    while iy+1 < (rooms[room][1][1][1]):
        display[iy+1, rooms[room][1][0][0], 0] = 1
        display[iy+1, rooms[room][1][0][0], 1] = 1
        display[iy+1, rooms[room][1][1][0], 0] = 1
        display[iy+1, rooms[room][1][1][0], 1] = 1
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


def updateroomlines(room):
    i = rooms[room][1][0][1]
    while i <= rooms[room][1][1][1]:
        updatehouseline(i)
        i = i + 1
