from text import *
from puzzle import *


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
    clearscreen()
    printscreen()
    directionchoice()
    readinput()
