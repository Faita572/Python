user_profile = {
    "username": "faita572",
    "level": 4,
    "is_online": True,
    "language": "Python"
}

print("Welcome back, " + user_profile["username"])
print("Your current level is: " + str(user_profile["level"]))

user_profile["level"] = 5 
user_profile["xp_points"] = 1250

print(user_profile)