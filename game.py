class Person:

    def __init__(self,type_person,health=100,armor=0,atack=10):
        self.money = 1800
        self.type_person = type_person
        self.health = health
        self.armor = armor
        self.atack = atack
        self.position = 0

    def win_round(self):
        self.money += 1000

    def lose_round(self):
        self.money += 500

    def buy_armor(self):
        price_armor = 500
        if self.money >= price_armor:
            self.money = self.money - price_armor
            self.armor += 100

    def buy_weapon(self,weapon_name):
        self.weapon_name = weapon_name
        if weapon_name == 'Deagle':
            price = 800
            if self.money >= price:
                self.money = self.money - price
        if weapon_name == 'AK47':
             price1 = 1500
             if self.money >= price1:
                 self.money = self.money - price1
             else:
                 print('Не хватает денег')

    def move(self,position1):
        self.position = self.position + position1

class Counter_Terrorist(Person):

    def __init__(self,type_person,health=100,armor=0,atack=10):
        super().__init__(type_person)
        self.de_mine = False

    def defuse(self):
        if self.de_mine == False:
            timer = 10
            return timer
        elif self.de_mine == True:
            timer = 5
            return timer

    def defuse_bomb(self,bomb):
        if bomb == True:
            print('Можно разминировать')
        else:
            print('Бобма не обнаружена')

    def add_weapon_ct(self,name_weapon_ct):
        if name_weapon_ct == 'M4A1':
            self.atack= self.atack + 24

class Terrorist(Person):

    def __init__(self,type_person,health=100,armor=0,atack=10):
        super().__init__(type_person)
        self.mine = False

    def bomb(self):
        self.mine = True

    def add_weapon_t(self,name_weapon_t):
        if name_weapon_t == 'AK47':
            self.atack = self.atack + 30

class Fight:

    def __init__(self,health,atack):
        self.health = health
        self.atack = atack

    def __add__(self, other):
        result = self.health - other.atack
        return result


ct1 = Counter_Terrorist(type_person='SWAT')
tt1 = Terrorist(type_person='GTA')
ct1.add_weapon_ct(name_weapon_ct='M4A1')
tt1.add_weapon_t(name_weapon_t='AK47')
ct1.move(position1=20)
tt1.move(position1=30)
if 0 < (ct1.position - tt1.position) <= 5 or 0 < (tt1.position - ct1.position) <= 5:
    fight1 = Fight(ct1.health,ct1.atack)
    fight2 = Fight(tt1.health,tt1.atack)
    result1 = fight1 + fight2
    result2 = fight2 + fight1
    print(f'COUNTER-TERRORIST: DMG = {ct1.atack} HP = {ct1.health}, TERRORIST : DMG = {tt1.atack} HP = {tt1.health}')
    print(f'COUNTER-TERRORIST: {result1} TERRORIST: {result2}')
    print(f'COUNTER-TERRORIST POSITION: {ct1.position}, TERRORIST POSITION: {tt1.position}')
else:
    print(f'COUNTER-TERRORIST: DMG = {ct1.atack} HP = {ct1.health}, TERRORIST : DMG = {tt1.atack} HP = {tt1.health}')
    print(f'COUNTER-TERRORIST POSITION: {ct1.position}, TERRORIST POSITION: {tt1.position}')
    print('Враги не встретились')



