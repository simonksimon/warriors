class Army:
    def __init__(self):
        self.soldiers = []
        self.size = 0
    def add_units(self, class_unit, amount):
        for _ in range(amount):
            self.soldiers.insert(0, class_unit())
        self.size += amount

class Warrior:
    def __init__(self, health=50, attack=5):
        self.health = health
        self.attack = attack
    @property
    def is_alive(self):
        return self.health > 0

class Knight(Warrior):
    def __init__(self, health=50):
        super().__init__(health, 7)

class Battle:
    def fight(self, army1, army2):
        while army1.size > 0 and army2.size > 0:
            attack1 = army1.soldiers[0].attack
            attack2 = army2.soldiers[0].attack
            army2.soldiers[0].health -= attack1
            if army2.soldiers[0].is_alive == True:
                army1.soldiers[0].health -= attack2
            if not army1.soldiers[0].is_alive:
                army1.soldiers.pop(0)
                army1.size -= 1
            elif not army2.soldiers[0].is_alive:
                army2.soldiers.pop(0)
                army2.size -= 1
        print(army1.size)
        print(army2.size)
        return army1.size > 0

def fight(w1, w2):
    attack1 = w1.attack
    attack2 = w2.attack
    while w1.is_alive == True and w2.is_alive == True:
        w2.health -= attack1
        health2 = w2.health
        health1 = w1.health
        if w2.is_alive == True:
            w1.health -= attack2
            health1 = w1.health
            health2 = w2.health
        if w1.is_alive == False:
            return False
        elif w2.is_alive == False:
            return True

chuck = Warrior()
bruce = Warrior()
carl = Knight()
dave = Warrior()
mark = Warrior()
print(fight(bruce, mark))
my_army = Army()
my_army.add_units(Warrior, 1)
enemy_army = Army()
enemy_army.add_units(Warrior, 2)
battle = Battle()
print(battle.fight(my_army, enemy_army))