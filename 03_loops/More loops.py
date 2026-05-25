health = 100

print("Entering the boss battle!")

# This loop keeps going until health drops to 0 or below
while health > 0:
    print("Current Health: " + str(health) + "%")

    # Player takes damage each turn
    health = health - 30
    print("Ouch! Took 30 damage.")

print("Game Over!")

lucky_number = 7
for i in range(1, 11):
    print("Checking number: " + str(i))
    if i == lucky_number:
        print("Found it! Stopping the search.")
        break