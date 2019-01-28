from map import *

# text to display
textlines = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
# predefined text for each room
roomtext = {"r1" : ["You found yourself in a dark and cold room, when your eyes start to get ", "used to the darkness you see something shiny, you approach, it is a", "sword, not the greatest and it is rusty, you look closer and you notice", "an engraving on the pommel of the sword where you can read:", "(It's dangerous to go alone, Take this.)", "", ""],
            "r2" : ["The smell of animals is very strong here, the room is full of hair all", "over the floor, you can see a big pile of hay and straw, a closet, at", "least what's left of it and a lot of tools spread out in a corner.", "", "", "", ""],
            "r3": ["this room is empty except for a old table with some potions on top.", "", "", "", "", "", ""],
            "r4" : ["This room is small and empty, the only thing here is a large spider's ", "web, which covers one corner of the room from ceiling to floor.", "You start to feel a tingling sensation in your leg.", "Hundreds of spiders try to reach you and climb your legs, you look up", "and a giant spider is hanging in the web ready to attack ...", "", ""],
            "r5" : ["Virtually empty and the floor has a few holes, three boxes lodged in the", "middle of the room near a heap of fabrics and a chain wrapped in the ", "wall.", "", "", "", ""],
            "r6" : ["The walls of this room seem to have something oozing, it's gooey and", "sticky. Suddenly this substance begins to climb walls and clump in a ", "big, disgusting sticky ball on the ceiling that falls to the floor with", "a huge bang and begins to crawl in your direction ...", "", "", ""],
            "r7" : ["Virtually empty and the floor has a few holes, three boxes lodged in the", "middle of the room near a heap of fabrics and a chain wrapped in the ", "wall.", "", "", "", ""],
            "r8": ["this room is empty except for a old table with some potions on top.", "", "", "", "", "", ""],
            "r9" : ["This room is completely empty.", "", "", "", "", "", ""],
            "r10": ["That smell of death! you cover your mouth in disgust, and what moments", "ago you thought was a pile of dirty clothes now jumps furiously in your", "direction and you can see a figure almost human, the smell worsens, the", "skin full of wounds and dirt and the mouth now open in an attempt of ", "roar, shows rotten and crooked teeth. He woke up…", "", ""],
            "r11": ["This room has old and rotten furniture, you can see an armchair with the", "lining already torn, two closets broken and what one day seems to have ", "been a table, not very big with 3 drawers.", "", "", "", ""],
            "r12": ["This room has many plants scattered everywhere. ", "You feel something touching you on the left shoulder, but you do not see", "anyone, when suddenly something pulls your foot, you fall on your back", "and hit your head, your vision is a little blurred but you can see the", "green increase around you. The plants have life ...", "", ""],
            "r13": ["The smell of animals is very strong here, the room is full of hair all", "over the floor, you can see a big pile of hay and straw, a closet, at", "least what's left of it and a lot of tools spread out in a corner.", "", "", "", ""],
            "r14": ["This room is small and empty, the only thing here is a large spider's ", "web, which covers one corner of the room from ceiling to floor.", "You start to feel a tingling sensation in your leg.", "Hundreds of spiders try to reach you and climb your legs, you look up", "and a giant spider is hanging in the web ready to attack ...", "", ""],
            "r15": ["This room looks like a throne room, big and empty, with only a big stone", "in the middle, and what seems like a shiny sword stuck on it.", "You should just take it!!!", "", "", "", ""],
            "r16": ["this room is empty except for an altar with a piece of paper on top.", "", "", "", "", "", ""],
            "r17": ["The walls of this room seem to have something oozing, it's gooey and", "sticky. Suddenly this substance begins to climb walls and clump in a ", "big, disgusting sticky ball on the ceiling that falls to the floor with", "a huge bang and begins to crawl in your direction ...", "", "", ""],
            "r18": ["this room is empty except for a old table with some potions on top.", "", "", "", "", "", ""],
            "r19": ["The sweat runs down your face, it's so hot here that you can see the", "heat waves all over the room through the smoke that emanates from the", "lava down below, when you lean to look and put your hands on the wall,", "burns and is so high that it gives you vertigo, to the bottom of the", "bridge a huge dragon, its scales shine in scarlet and carmine colors, he", "faces you with his giant and intimidating eyes and spits a huge ball ", "of fire that slides quickly on the bridge in your direction."],
            "h1" : ["just a corridor, empty and boring...", "", "", "", "", "", ""],
            "h2" : ["just a corridor, empty and boring...", "", "", "", "", "", ""],
            "h3" : ["just a corridor, empty and boring...", "", "", "", "", "", ""],
            "h4" : ["just a corridor, empty and boring...", "", "", "", "", "", ""],
            "h5" : ["just a corridor, empty and boring...", "", "", "", "", "", ""],
            "h6" : ["just a corridor, empty and boring...", "", "", "", "", "", ""],
            "h7" : ["just a corridor, empty and boring...", "", "", "", "", "", ""],
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
def printscreen(display):
    newscreen()
    i = 0
    while i < housedimentions[0]:
        print(textlines[i].ljust(maxLength), display[i])
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
