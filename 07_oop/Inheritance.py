# The Parent Class
class Enemy:
    def __init__(self, name):
        self.name = name
        self.health = 50

    def attack(self):
        print(self.name + " lunges forward to attack!")

# The Child Class
#It inherits from the parent class using parenthesis
class Wizard(Enemy):
    def cast_spell(self):
        print(self.name + " fires a blazing fireball!")

scary_wizard = Wizard("Merlin")
scary_wizard.attack() 
scary_wizard.cast_spell() 


### Inheritance is just like "A family tree"
# Instead of writing a brand new class from scratch... a new class can "inherit" (copy) all the variables and functions from an existing class