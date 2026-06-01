game_inventory = {"swords": 3, "potions": 5, "shields": 1}
print(game_inventory.get("potions", 0)) # Prints: 5
print(game_inventory.get("diamonds", 0)) 