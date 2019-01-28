from interactions import *
import variables
variables.playerpossition = variables.startpossition

global textlines
updateplayerstats()

# main cycle
while True:
    #textlines[1] = "player pos " + variables.playerpossition + "     last pos " + variables.playerlastpossition
    updateroom(variables.playerpossition)
    updateroomlines(variables.playerpossition)
    updateroomtext(variables.playerpossition)
    variables.playerpossition = choseoption()
    clearextra()
    clearoptions()


