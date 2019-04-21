#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Joseph Foley
#
# Created:     16/04/2019
# Copyright:   (c) Joseph Foley 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random
import roomgenerator
import gameinfogenerator
import bossgenerator
##story intro

def openingtext():
    gameinfogenerator.storyintro()

##first, third stage - genarate series of rooms, 
def stage():
    smallrooms = random.randrange(2,5)
    for i in range(0, smallrooms):
        roomgenerator.generatesmallroom()

    mediumrooms = random.randrange(5,8)

    for i in range(0, mediumrooms):
        roomgenerator.generatemediumroom()

    largerooms = random.randrange(1,4)
    for i in range(0, largerooms):
        roomgenerator.generatelargeroom()


##second and fourth stage - generate boss room

def boss_stage():
    bossgenerator.generateboss();



def generatestages():
    openingtext()
    stage()
    boss_stage()
    stage()
    boss_stage()

##call function
generatestages()
