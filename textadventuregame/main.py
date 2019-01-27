from interactions import *
global playerpossition
updateroom(playerpossition)
updateroomlines(playerpossition)
updateroomtext(playerpossition)
updateplayerstats()

while True:
    playerpossition = choseoption()
    updateroom(playerpossition)
    updateroomlines(playerpossition)
    updateroomtext(playerpossition)
    clearextra()
    clearoptions()


