#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Joseph Foley
#
# Created:     03/04/2019
# Copyright:   (c) Joseph Foley 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random;


smallmonsters = ["goblin warrior", "kobold miner",
"fire elemental", "orc grunt", "water elemental"]

mediummonsters = ["orc warrior", "kobold slinger", "crimson dragon hatchling"
,"goblin mob boss", "cat warrior", "cat archer", "steel dragon hatchling"]

objects = ["treasure chest", "old map", "trapdoor", "rusty dagger", "spell scroll" ]

def randomchoice(listname):
    gennum = random.randrange(0,(len(listname)-1))

    return listname[gennum]





# small room (2-4 entities)

def generatesmallroom():
    entitynum = random.randrange(2,4)
    smallroominfo=[]
    smallroominfo.append("SMALL ROOM")
#adds small monsters or objects, 3/10 chance it is an object
    for i in range(0, entitynum):
        getnum = random.randrange(0,10)
        if (getnum <= 7):
            smallroominfo.append(str(randomchoice(smallmonsters)))
        elif (getnum > 7):
            smallroominfo.append(str(randomchoice(objects)))


    print(smallroominfo)





# medium room (3-8 entities)
def generatemediumroom():
    entitynum = random.randrange(3,8)
    mediumroominfo=[]
    mediumroominfo.append("MEDIUM ROOM")
#adds combination of small monsters, medium monsters, and objects
    for i in range(0, entitynum):
        getnum = random.randrange(0,10)
        if (getnum <= 3):
            mediumroominfo.append(str(randomchoice(smallmonsters)))
        elif (getnum >= 3 and getnum <=7 ):
            mediumroominfo.append(str(randomchoice(mediummonsters)))
        elif (getnum > 7):
            mediumroominfo.append(str(randomchoice(objects)))
    print(mediumroominfo)
# large room (5-12 entities)


generatesmallroom()
generatesmallroom()
generatemediumroom()
