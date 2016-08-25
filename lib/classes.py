import sys
import os

# A feature taken from Dungeons and Dragons! The initiative rolls and stats of each character,
# based on their combat stats, so this is a member of the CharacterClass class

class skillStats:
# Values:
# Acrobatics DEX
# Arcana INT 
# Athletics STR 
# Bluff CHA 
# Diplomacy CHA 
# Dungeoneering WIS 
# Endurance CON 
# Heal WIS 
# History INT 
# Insight WIS 
# Intimidate CHA 
# Nature WIS 
# Perception 
# Religion 
# Stealth 
# Streetwise 
# Thievery DEX
    def __init__(self, characterClassValue ):
        self.acrobatics = characterClassValue.strength
        self.arcana = characterClassValue.magic


#This is the character class for all combat characters, it contains all of their base, nonderived stats
class CharacterClass:

    ## base combat stats 
    # int hp
    # int level
    # int strength
    # int magic
    # int skill
    # int speed 
    # int luck 
    # int defence  
    # int resist 
    # int move 
    # int con 

    #class values
    maxLevel = 20


    #default constructor
    def __init__(self):
        self.name = "none"

        self.level = 1
        self.hp = 15 
        self.strength = 4
        self.skill = 4
        self.speed = 4
        self.luck = 4
        self.defence = 4
        self.resist = 4
        self.move = 4
        self.con = 3   
    
    #constructor
    def __init__(self, name, level, hp, strength, magic, skill, speed, luck, defence, resist, con, move):
        #base stats
        self.name = name
        self.level = level

        #combat stats
        self.hp = hp 
        self.strength = strength
        self.magic = magic
        self.skill = skill
        self.speed = speed
        self.luck = luck
        self.defence =  defence
        self.resist = resist
        self.con = con
        self.move = move



    def __repr__(self):
        return "< Character Class - level:%s hp:%s str:%s skill:%s spd:%s luck:%s def:%s res:%s con:%s move:%s >" % (self.level , self.hp, self.strength, self.skill, self.speed, self.luck, self.defence, self.resist, self.con, self.move)

class ClassCaps:
    #default constructor
    def __init__(self):


        self.level = 20
        self.hp = 40
        self.strength = 20
        self.skill = 20
        self.speed = 20
        self.luck = 20
        self.defence = 20
        self.resist = 20
        self.move = 20
        self.con = 20 
    
    #constructor
    def __init__(self, name, level, hp, strength, magic, skill, speed, luck, defence, resist, con, move):
        #base stats
        self.level = level

        #combat stats
        self.hp = hp 
        self.strength = strength
        self.magic = magic
        self.skill = skill
        self.speed = speed
        self.luck = luck
        self.defence =  defence
        self.resist = resist
        self.con = con
        self.move = move
