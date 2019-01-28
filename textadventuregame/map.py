from variables import *
import numpy as np

# display uses a 3d matrix to store five values into each coordinate of the map which after is translated to a symbol
display = np.zeros((housedimentions[0], housedimentions[1], 5), dtype=np.int64)

houselines = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]

enemylines = {"spider1":[''' ''', ''' ''', ''' ''', ''' ''', '''           ____                      ,''', '''          /---.'.__             ____//''', '''               '--.\           /.---' ''', '''          _______  \\         //''', '''        /.------.\  \|      .'/  ______''', '''       //  ___  \ \ ||/|\  //  _/_----.\__''', '''      |/  /.-.\  \ \:|< >|// _/.'..\   '--' ''', '''         //   \'. | \'.|.'/ /_/ /  \\''', '''        //     \ \_\/" ' ~\-'.-'    \\''', '''       //       '-._| :H: |'-.__     \\''', '''      //           (/'==='\)'-._\     ||''', '''      ||                        \\    \|''', '''      ||                         \\    ' ''', '''      |/                          \\''', '''                                   ||''', '''                                   ||''', '''                                   \\''', ''' ''', ''' ''', ''' ''', ''' '''],
              "spider2":[''' ''', ''' ''', ''' ''', ''' ''', '''           ____                      ,''', '''          /---.'.__             ____//''', '''               '--.\           /.---' ''', '''          _______  \\         //''', '''        /.------.\  \|      .'/  ______''', '''       //  ___  \ \ ||/|\  //  _/_----.\__''', '''      |/  /.-.\  \ \:|< >|// _/.'..\   '--' ''', '''         //   \'. | \'.|.'/ /_/ /  \\''', '''        //     \ \_\/" ' ~\-'.-'    \\''', '''       //       '-._| :H: |'-.__     \\''', '''      //           (/'==='\)'-._\     ||''', '''      ||                        \\    \|''', '''      ||                         \\    ' ''', '''      |/                          \\''', '''                                   ||''', '''                                   ||''', '''                                   \\''', ''' ''', ''' ''', ''' ''', ''' '''],
              "blob1"  :[''' ''', ''' ''', ''' ''', ''' ''', ''' ''', '''     /^\    /^\ ''', '''    {  O}  {  O}''', '''     \ /    \ /''', '''     //     //       _------_''', '''    //     //     ./~        ~-_''', '''   / ~----~/     /              \ ''', ''' /         :___./                ~-''', '''|  \________)                     |''', '''|        /                        |''', '''|                                 |''', '''|                               ./''', ''' \                               \.''', ''' .|                                ~-_''', '''/_____________________________________~~''', ''' ''', ''' ''', ''' ''', ''' ''', ''' ''', ''' '''],
              "blob2"  :[''' ''', ''' ''', ''' ''', ''' ''', ''' ''', '''     /^\    /^\ ''', '''    {  O}  {  O}''', '''     \ /    \ /''', '''     //     //       _------_''', '''    //     //     ./~        ~-_''', '''   / ~----~/     /              \ ''', ''' /         :___./                ~-''', '''|  \________)                     |''', '''|        /                        |''', '''|                                 |''', '''|                               ./''', ''' \                               \.''', ''' .|                                ~-_''', '''/_____________________________________~~''', ''' ''', ''' ''', ''' ''', ''' ''', ''' ''', ''' '''],
              "zombie1":[''' ''', ''' ''', '''                        _,--~~~,''', '''                       .'        `.''', '''                       |           ;''', '''                       |           :''', '''                      /_,-==/     .' ''', '''                    /'`\*  ;      : ''', '''                  :'    `-        :  ''', '''                  `~*,'     .     : ''', '''                     :__.,._  `;  :  ''', '''                     `\'    )  '  `,  ''', '''                         \-/  '     )   ''', '''                         :'          \ _''', '''                          `~---,-~    `,)''', '''          ___                   \     /~`\ ''', '''    \---__ `;~~~-------------~~~(| _-'    `,''', '''  ---, ' \`-._____     _______.---'         \ ''', ''' \--- `~~-`,      ~~~~~~                     `,''', '''\----      )                                   \ ''', '''\----.  __ /                                    `-''', ''' \----'` -~____  ''', '''               ~~~~~--------,.___    ''', '''                                 ```\_''', ''' '''],
              "plant1" :[''' ''', ''' ''', ''' ''', ''' ''', '''    .-'`"'-.      _.---. ''', '''  .'        \   .'      '. ''', ''' /           \ /          \ ''', '''|      __     Y    __      | ''', '''|   .'`   '-./  .-'  `'.   | ''', ''' \ /        ',,'        \ /-. ''', '''  \|      .-"()"-.      |/--.`\ ''', '''   |    /`  /||\  `\    |    \ \ ''', '''    \   |          |   /      ; ; ''', '''     '--`\        /`--'       | | ''', '''          '-.__.-'            ; ; ''', '''          __                  / / ''', '''   .-'`'-`  '.  .-.   _     /`/` ''', '''  (_  .--..._ `-'  \_| \  /`/` ''', '''   '.__.     `---._    |/`/` ''', '''        `)    _..  '-./`/` ''', '''        (__.-'  _)  /`/` ''', '''                `--`/` ''', '''                   ` ''', ''' ''', ''' '''],
              "dragon" :[''' ''', ''' ''', ''' ''', ''' ''', '''               ___====-_  _-====___ ''', '''           _--^^^#####//      \\#####^^^--_ ''', '''        _-^##########// (    ) \\##########^-_ ''', '''       -############//  |\^^/|  \\############- ''', '''     _/############//   (@::@)   \\############\_ ''', '''    /#############((     \\//     ))#############\ ''', '''   -###############\\    (oo)    //###############- ''', '''  -#################\\  / VV \  //#################- ''', ''' -###################\\/      \//###################- ''', '''_#/|##########/\######(   /\   )######/\##########|\#_ ''', '''|/ |#/\#/\#/\/  \#/\##\  |  |  /##/\#/  \/\#/\#/\#| \| ''', '''`  |/  V  V  `   V  \#\| |  | |/#/  V   '  V  V  \|  ' ''', '''   `   `  `      `   / | |  | | \   '      '  '   ' ''', '''                    (  | |  | |  ) ''', '''                   __\ | |  | | /__ ''', '''                  (vvv(VVV)(VVV)vvv) ''', ''' ''', ''' ''', ''' ''', ''' ''', ''' '''],
              }

# Rooms Information
# Layout - [enemies],[coordinates of 2 corners],[connections to other rooms],[available options],[items]
rooms = {"r1":  [[""]       , [[0  * charratio, 8 ], [3  * charratio, 16]], [""   , "h1" , ""   , ""   ], ["move", "loot", "cheats", "extra"], ["wood sword"]    ],
         "r2":  [[""]       , [[4  * charratio, 12], [6  * charratio, 14]], ["h1" , ""   , ""   , ""   ], ["move", "loot", "cheats", "extra"], ["staff"]         ],
         "r3":  [[""]       , [[4  * charratio, 9 ], [6  * charratio, 11]], [""   , ""   , "h1" , ""   ], ["move", "loot", "cheats", "extra"], ["potion"]        ],
         "r4":  [["spider1"], [[7  * charratio, 10], [10 * charratio, 13]], ["h2" , ""   , "r8" , "h1" ], ["move", ""    , "cheats", "extra"], [""]              ],
         "r5":  [[""]       , [[9  * charratio, 5 ], [12 * charratio, 9 ]], [""   , ""   , ""   , "h2" ], ["move", "loot", "cheats", "extra"], ["shoe"]          ],
         "r6":  [["blob1"]  , [[6  * charratio, 3 ], [8  * charratio, 8 ]], ["r7" , "h2" , ""   , ""   ], ["move", ""    , "cheats", "extra"], [""]              ],
         "r7":  [[""]       , [[7  * charratio, 1 ], [10 * charratio, 3 ]], [""   , ""   , "r6" , ""   ], ["move", "loot", "cheats", "extra"], ["chestplate"]    ],
         "r8":  [[""]       , [[9  * charratio, 13], [11 * charratio, 17]], ["r4" , ""   , "r9" , ""   ], ["move", "loot", "cheats", "extra"], ["potion"]        ],
         "r9":  [[""]       , [[10 * charratio, 17], [12 * charratio, 19]], ["r8" , "h4" , "r10", ""   ], ["move", ""    , "cheats", "extra"], [""]              ],
         "r10": [["zombie1"], [[6  * charratio, 19], [11 * charratio, 24]], ["r9" , ""   , ""   , "r11"], ["move", ""    , "cheats", "extra"], [""]              ],
         "r11": [[""]       , [[1  * charratio, 17], [6  * charratio, 20]], [""   , "r10", "h3" , ""   ], ["move", "loot", "cheats", "extra"], ["iron sword"]    ],
         "r12": [["plant1"] , [[2  * charratio, 22], [4  * charratio, 24]], ["h3" , ""   , ""   , ""   ], ["move", ""    , "cheats", "extra"], [""]              ],
         "r13": [[""]       , [[14 * charratio, 17], [18 * charratio, 21]], ["h5" , ""   , ""   , "h4" ], ["move", "loot", "cheats", "extra"], ["shield"]        ],
         "r14": [["spider2"], [[15 * charratio, 14], [18 * charratio, 16]], [""   , ""   , ""   , "h5" ], ["move", ""    , "cheats", "extra"], [""]              ],
         "r15": [[""]       , [[14 * charratio, 8 ], [18 * charratio, 13]], ["h6" , "h7" , "h5" , ""   ], ["move", "loot", "cheats", "extra"], ["master sword"]  ],
         "r16": [[""]       , [[18 * charratio, 6 ], [20 * charratio, 10]], ["r17", ""   , ""   , ""   ], ["move", "loot", "cheats", "extra"], ["ability scroll"]],
         "r17": [["blob2"]  , [[18 * charratio, 3 ], [21 * charratio, 6 ]], [""   , ""   , "r16", "h6" ], ["move", ""    , "cheats", "extra"], [""]              ],
         "r18": [[""]       , [[14 * charratio, 2 ], [17 * charratio, 7 ]], [""   , "h6" , ""   , ""   ], ["move", "loot", "cheats", "extra"], ["potion"]        ],
         "r19": [["dragon"] , [[21 * charratio, 9 ], [25 * charratio, 13]], [""   , "end", ""   , "h7" ], ["move", ""    , "cheats", "extra"], [""]              ],
         "h1":  [[""]       , [[3  * charratio, 11], [7  * charratio, 12]], ["r3" , "r4" , "r2" , "r1" ], ["move", ""    , "cheats", "extra"], [""]              ],
         "h2":  [[""]       , [[8  * charratio, 7 ], [9  * charratio, 10]], [""   , "r5" , "r4" , "r6" ], ["move", ""    , "cheats", "extra"], [""]              ],
         "h3":  [[""]       , [[2  * charratio, 20], [3  * charratio, 22]], ["r11", ""   , "r12", ""   ], ["move", ""    , "cheats", "extra"], [""]              ],
         "h4":  [[""]       , [[12 * charratio, 18], [14 * charratio, 19]], [""   , "r13", ""   , "r9" ], ["move", ""    , "cheats", "extra"], [""]              ],
         "h5":  [[""]       , [[14 * charratio, 13], [15 * charratio, 17]], ["r15", "r14", "r13", ""   ], ["move", ""    , "cheats", "extra"], [""]              ],
         "h6":  [[""]       , [[17 * charratio, 5 ], [18 * charratio, 8 ]], [""   , "r17", "r15", "r18"], ["move", ""    , "cheats", "extra"], [""]              ],
         "h7":  [[""]       , [[18 * charratio, 11], [21 * charratio, 12]], [""   , "r19", ""   , "r15"], ["move", ""    , "cheats", "extra"], [""]              ],
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


# update house lines that belong tho the room, but not the rest
def updateroomlines(room):
    i = rooms[room][1][0][1]
    while i <= rooms[room][1][1][1]:
        updatehouseline(i)
        i = i + 1
