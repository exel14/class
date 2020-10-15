class Person:

    def __init__(self,type_person,health=100,armor=0,atack=10):
        self.money = 1800
        self.type_person = type_person
        self.health = health
        self.armor = armor
        self.atack = atack

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
class Terrorist(Person):

    def __init__(self,type_person,health=100,armor=0,atack=10):
        super().__init__(type_person)
        self.mine = False

    def bomb(self):
        self.mine = True

person1 = Person('ct')
person1.win_round()
person1.lose_round()
person1.buy_weapon('Deagle',)
person1.buy_weapon('AK47')
person1.buy_armor()
person2 = Counter_Terrorist(type_person='SWAT')
person2.defuse()
person2.de_mine = True
person2.defuse()
person3 = Terrorist(type_person='IGIL')
person3.bomb()
print(person1.money,person1.armor,person2.defuse())


