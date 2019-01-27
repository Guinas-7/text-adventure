from interactions import *
global playerpossition
updateroom(playerpossition)
updateroomlines(playerpossition)
updateroomtext(playerpossition)

while True:
    print(playerpossition)
    playerpossition = choseoption()
    updateroom(playerpossition)
    updateroomlines(playerpossition)
    updateroomtext(playerpossition)
    clearextra()


