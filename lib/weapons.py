#This is intended to be a list of weapons

#weapon class

meleeWeapons = ['sword', 'axe', 'lance', 'bow']
magicWeapons = ['light', 'darkness', 'anima']


class Weapon:
    currentID = 0
    def __init__(self, name, weaponClass, weaponType, might, hit, crit, weight, range):
        self.id = self.currentID
        self.currentID+=1

        self.name = name
        self.weaponClass = weaponClass #intended to be 0 or 1, 0 for physical, 1 for magical
        self.weaponType = weaponType  # a number 0 to (2 or 3) (see arrays above)
        self.might = might
        self.hit = hit
        self.crit = crit
        self.weight = weight
        self.act_range = range


    def __repr__(self):
        return "< Weapon - mt:%s hit:%s crit:%s wt:%s range:%s>" % (self.might, self.hit, self.crit, self.weight, self.act_range)
        

weaponsList = []

