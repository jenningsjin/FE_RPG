#This is the class that contains each of the character's growths: the chance they will gain stats
#on level up, there will be a number of growth patterns to select from, hence the data
class CharacterGrowths:
    #default constructor
    def __init__(self):
        self.hp = 30 
        self.strength = 30
        self.skill = 30
        self.speed = 30
        self.luck = 30
        self.defence = 30
        self.resist = 30
 
    #constructor
    def __init__(self, hp, strength, magic, skill, speed, luck, defence, resist):
        #combat stats
        self.hp = hp 
        self.strength = strength
        self.magic = magic
        self.skill = skill
        self.speed = speed
        self.luck = luck
        self.defence =  defence
        self.resist = resist
  