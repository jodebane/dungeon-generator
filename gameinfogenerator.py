#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Joseph Foley
#
# Created:     20/04/2019
# Copyright:   (c) Joseph Foley 2019
# Licence:     <your licence>
#cross-cultural sources : "-pur" means 'settlement' in various South Asian Languages, "-gawa" means river in Japanese
#-------------------------------------------------------------------------------
import random
from random import randrange
placetypes = ["castle", "caverns", "fortress", "bastion", "temple",
"mines", "palace"]
nameprefix = ["yunga", "stuga", "anta", "abame", "ince", "jodh", "mustabi",
"yala", "craigh", "trom", ""]
namesuffix = ["far", "rudith", "movski","gawa", "ford", "qo", "bhuntu" ,"mer", "pur"]

def getrandom(listparam):
    indexnum= randrange(0, len(listparam))
    return (listparam[indexnum])

getrandom(placetypes)


def storyintro():
    print("The ")
    print(getrandom(placetypes).capitalize())
    print("of ")
    print(getrandom(nameprefix).capitalize()+
    getrandom(namesuffix))

    
