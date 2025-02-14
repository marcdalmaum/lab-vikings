import random

# Soldier


class Soldier:

    def __init__(self, health, strength):
        self.health= health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health-= damage


# Viking


class Viking (Soldier):

    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def receiveDamage(self, damage):
        self.health-= damage
        self.damage = damage  
        if self.health > 0:
            return f'{self.name} has received {self.damage} points of damage'
        else:
            return f'{self.name} has died in act of combat'
    
    def battleCry(self):
        return 'Odin Owns You All!'


# Saxon


class Saxon (Soldier):

    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.health-= damage
        self.damage = damage  
        if self.health > 0:
            return f'A Saxon has received {self.damage} points of damage'
        else:
            return 'A Saxon has died in combat'


# War


class War:

    def __init__(self):

        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):

        self.vikingArmy.append(Viking)

    def addSaxon(self, Saxon):

        self.saxonArmy.append(Saxon)

    def vikingAttack(self):

        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        sax_dam = saxon.receiveDamage(viking.strength)
        if saxon.health <= 0:
            self.saxonArmy.pop(0)
        return sax_dam

    def saxonAttack(self):

        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        vik_dam = viking.receiveDamage(saxon.strength)
        if viking.health <= 0:
            self.vikingArmy.pop(0)
        return vik_dam

    def showStatus(self):
        
        if len(self.saxonArmy) <= 0:
            return 'Vikings have won the war of the century!'
        elif len(self.vikingArmy) <= 0:
            return 'Saxons have fought for their lives and survive another day...'
        elif len(self.saxonArmy) > 0 and len(self.vikingArmy) > 0:
            return 'Vikings and Saxons are still in the thick of battle.'