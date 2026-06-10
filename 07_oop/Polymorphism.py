class Warrior:
    def use_ability(self):
        print("The Warrior uses: Blade Storm!")

class Medic:
    def use_ability(self):
        print("The Medic uses: Health Drone!")

# We put two completely different types of objects into a single list
party_members = [Warrior(), Medic()]

# We loop through them and call the EXACT same function name
for member in party_members:
    member.use_ability() 


### Polymorphism is like "Many shapes"
# It means that different types of objects can be treated as the same type through a common interface (like a shared function name)
#