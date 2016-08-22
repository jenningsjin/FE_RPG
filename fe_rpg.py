import sys
import os
import re
import random

from data.weapons import *
#The most imfamous of Fire Emblem Gameplay Elements returns as a function!
def RNG():
    return ( random.randint(0,100) + random.randint(0,100) )/2

# #The class for each Weapons, the global list of weapons is located in weapons.py 
# class Weapon:
#     currentID = 0
#     def __init__(self, name, might, hit, crit, weight, range):
#         self.id = self.currentID
#         self.currentID+=1

#         self.name = name
#         self.might = might
#         self.hit = hit
#         self.crit = crit
#         self.weight = weight
#         self.act_range = range


#     def __repr__(self):
#         return "< Weapon - mt:%s hit:%s crit:%s wt:%s range:%s>" % (self.might, self.hit, self.crit, self.weight, self.act_range)

class Character:
    #This is the character class for all combat characters

    ## base combat stats 
    # int hp
    # int level

    # int strength
    # int skill
    # int speed 
    # int luck 
    # int defence  
    # int resist 
    # int move 
    # int con 

    #class values
    maxLevel = 20
    def __init__(self):
        self.hp = 15 
        self.strength = 0
        self.skill = 0
        self.speed = 0
        self.luck = 0
        self.defence = 0
        self.resist = 0
        self.move = 4
        self.con = 3   
    
    def __init__(self, level, hp, strength, skill, speed, luck, defence, resist, con, move):
        #base stats
        self.level = level
        self.hp = hp 
        self.strength = strength
        self.skill = skill
        self.speed = speed
        self.luck = luck
        self.defence =  defence
        self.resist = resist
        self.con = con
        self.move = move


        #derived stats
        self.avoid = 0
        self.hit = 0


    def calcAttackSpeed(self, weaponWeight ):
        return self.speed - weaponWeight - self.con

    def calcAvoid(self, weaponWeight): 
        return self.calcAttackSpeed(weaponWeight) + self.luck
     
    def setAvoid(self, weapon):
        self.avoid = self.calcAvoid(weapon.weight) 
        return

    def calcHit(self, baseHit):
        return self.skill*2 + baseHit + self.luck/2 

    def setHit(self, weapon):
        self.hit = self.calcHit(weapon.hit)
        return

    def equipWeapon(self, weapon):
        self.Weapon 
        return

    def __repr__(self):
        return "< Character - level:%s hp:%s str:%s skill:%s spd:%s luck:%s def:%s res:%s con:%s move:%s >" % (self.level , self.hp, self.strength, self.skill, self.speed, self.luck, self.defence, self.resist, self.con, self.move)


# class         



def combatHitResult( attacker, defender ):
    accuracy = attacker.hit - defender.avoid
    # if accuracy < 0:
    #     accuracy = 0
    return accuracy > RNG()




if __name__ == '__main__':
    # IronSword = Weapon("iron sword", 4, 85, 0, 4, 1)
    # print IronSword

    Kevin = Character(1, 16, 4, 7, 9, 0, 2, 0, 5, 5)
    print Kevin 

    # Kevin.setHit(IronSword)
    # print "set hitrate:" + str(Kevin.hit)

    # for i in xrange(50):
    #     print RNG()
