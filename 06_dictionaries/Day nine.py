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

# A loop containing dictionaries
classroom = {
    "Alex": {"Math": 95, "Science": 88},
    "Sarah": {"Math": 99, "Science": 94},
    "James": {"Math": 72, "Science": 80}
}

#Nested loops to access nested dictionaries
sarah_profile = classroom["Sarah"] 
print(sarah_profile) # Prints: {'Math': 99, 'Science': 94}

for subject, grade in sarah_profile.items():
    print(f"Sarah's {subject} Grade: {grade}")