inventory = []
positiveanswer = ["yes", "sure"]
negativeanswer = ["no", "nope"]
north = ["north", "up", "top"]
south = ["south", "down", "bottom"]
east = ["east", "right"]
west = ["west", "left"]
back = ["back", "previous", "cancel"]


def readinput():
    i = input().lower()
    if i == "exit":
        exit()
    else:
        return i


def directionchoice():
    while True:
        print("wich direction do you want to move in")
        playerinput = readinput()
        if playerinput in north:
            return 1
        elif playerinput in east:
            return 2
        elif playerinput in south:
            return 3
        elif playerinput in west:
            return 4
        elif playerinput in back:
            return 0
        else:
            print("That is not a valid option")


def startfight():
    while True:
        playerinput = readinput()
        if playerinput in positiveanswer:
            return True
        elif playerinput in negativeanswer:
            return False
        else:
            print("That is not a valid option")

def keepitem()