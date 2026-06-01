game_inventory = {"swords": 3, "potions": 5, "shields": 1}
print(game_inventory.get("potions", 0)) # Prints: 5
print(game_inventory.get("diamonds", 0)) 


#looping through dictionaries
movie_ratings = {
    "Micheal": 9.0,
    "Thunderbolts": 7.7,
    "Hokum": 8.6
}
print("--- MOVIE NAMES ---")
for movie in movie_ratings.keys():
    print(movie)
print("\n--- RATINGS ---")
for rating in movie_ratings.values():
    print(rating)
print("\n--- FULL REVIEW ---")
for movie, rating in movie_ratings.items():
    print(movie + " has a rating of " + str(rating))