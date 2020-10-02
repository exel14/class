class Planet:
    """Этот класс описывает личность!"""

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return f'Планета: {self.name}!'

list_of_planet = ['Earth','Mars','Mercury','Venus','Saturn','Pluton','Jupyter','Neptun']

solary_system = []

for planet in list_of_planet:
    new_planet = Planet(planet)
    solary_system.append(new_planet)

print(solary_system)