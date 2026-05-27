# 1. Create a list of video games
video_games = ["Minecraft", "Zelda", "Cyberpunk", "Mario"]
# 2. Accessing items using their position
print("The first game is: " + video_games[0])
print("The third game is: " + video_games[2])
# 3. Changing an item in the list
video_games[1] = "Metroid"
# 4. Adding a new item to the end of the list
video_games.append("Halo")
print(video_games)

#Grocery list program that accepts user input
# 1. Start with an empty list
grocery_list = []
print("--- INTERACTIVE GROCERY LIST ---")
print("Type your items one by one. When you are finished, type 'stop'.")
print("--------------------------------")
# 2. Use a while loop to keep asking for items
while True:
    user_item = input("Enter an item: ")
    if user_item.lower() == "stop":
        break
    else:
        grocery_list.append(user_item)
        print("Added: " + user_item)
# 3. Once the loop breaks, show the final list
print("\n--- YOUR FINAL GROCERY LIST ---")
for item in grocery_list:
    print("- " + item)