class Pizza:

    def __init__(self,name,price):
        self.name = name
        self.price = price
        self.items = []

    def __str__(self):
        return self.name

    def add_pizza(self,pizza):
        self.items.append(pizza)

    def __repr__(self):
        return f'Пицца {self.name}'

    def to_order(self,money):
        result = money - self.price
        return result

new_elem = Pizza ('Peperoni',400)
new_elem.add_pizza(new_elem)
print(new_elem.items)
print(new_elem,to_order)






