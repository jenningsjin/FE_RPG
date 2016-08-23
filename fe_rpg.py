import sys
import os
import re
import random

# Data imports, these are all the base classes that are used in the game proper,
# the respective files also hold all of the data for all of their item 
# e.g. data/weapons.py also has the array that holds all of the different weapons in the game 
from lib.weapons import *
from lib.classes import *
from lib.characterGrowth import *

## NOTE: The number of classes and varsr I can't name what I want to, e.g. class, str, def, etc. 
##      Is surprisingly high... a lot of them seem to be keywords in Python



# The most imfamous of Fire Emblem Gameplay Elements returns as a function!
# This is actually how the FE7+ RNG works
def RNG():
    return ( random.randint(0,100) + random.randint(0,100) )/2

# This is the class for a character proper
class Character:
    def __init__(self, characterClassObj, characterGrowthsObj, Inventory):
        self.stats = characterClassObj
        self.growths = characterGrowthsObj
        self.weaponList = Inventory
        self.weapon = Inventory.front()

        # These are the three derived stats that affect combat. They are somewhat tricky to deal
        # with in that they are constantly changing:
        #      1) When Base stats change (level up)
        #      2) When weapons are equipped 
        self.avoid = self.setAvoid(self.weapon)
        self.hit = self.setHit(self.weapon)
        self.attackSpeed = self.calcAttackSpeed(self.weapon.weight)

    def calcAttackSpeed(self, weaponWeight):
        return self.stats.speed - weaponWeight - self.stats.con

    def setAttackSpeed(self, weapon):
        self.attackSpeed = self.calcAttackSpeed(weapon.weight)
        return

    def calcAvoid(self, weaponWeight): 
        return self.calcAttackSpeed(weaponWeight) + self.stats.luck
     
    def setAvoid(self, weapon):
        self.avoid = self.calcAvoid(weapon.weight) 
        return

    def calcHit(self, baseHit):
        return self.stats.skill*2 + baseHit + self.stats.luck/2 

    def setHit(self, weapon):
        self.hit = self.calcHit(weapon.hit)
        return

    # Equiping a new weapon changes the weapon but also changes all the 
    # derived stats
    def equipWeapon(self, weapon):
        self.weapon = weapon
        self.setAttackSpeed(self.weapon)
        self.setAvoid(self.weapon)
        self.setHit(self.weapon)
        return

    # At level up, we do an RNG roll against each of the characters growths
    # to see which stats improve.
    def levelUp():
        self.stats.level+=1
        #once we see what stats 
        self.setAttackSpeed(self.weapon)
        self.setAvoid(self.weapon)
        self.setHit(self.weapon)


#Bows do not affect the Triangle Otherwise:
# Physical: Swords > Axes > Lances > Swords
# Magical:  Light > Darkness > Anima > Light
def weaponTriangle( attacker_weapon, defender_weapon):
    if attacker_weapon.weaponType == 3 or defender.weaponType == 3: # if it's bow
        return 0

    elif (attacker_weapon.weaponType - defender.weaponType) == 0:
        return 0

    elif (attacker_weapon.weaponType - defender.weaponType) == -1:
        return 15

    elif (attacker_weapon.weaponType - defender.weaponType) == -2:
        return -15
    
    elif (attacker_weapon.weaponType - defender.weaponType) == 1:
        return -15

    elif (attacker_weapon.weaponType - defender.weaponType) == 2:
        return 15

#attacker and defender are both 'Character' Objects
def combatHitResult( attacker, defender ):
    accuracy = attacker.hit - defender.avoid + weaponTriangle(attacker.weapon, defender.weapon)
    # if accuracy < 0:
    #     accuracy = 0
    return accuracy > RNG()




if __name__ == '__main__':
    print 'filler'
    # IronSword = Weapon("iron sword", 4, 85, 0, 4, 1)
    # print IronSword

    # Kevin = Character(1, 16, 4, 7, 9, 0, 2, 0, 5, 5)
    # print Kevin 

    # Kevin.setHit(IronSword)
    # print "set hitrate:" + str(Kevin.hit)

    # for i in xrange(50):
    #     print RNG()
