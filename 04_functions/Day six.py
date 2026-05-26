def create_welcome_message(username, city):
    print("--- WELCOME ---")
    print("Welcome back, " + username + "!")
    print("Checking the current weather in " + city + " for you...")
user_name_input = input("What is your name? ")
user_city_input = input("What city are you in? ")
create_welcome_message(user_name_input, user_city_input)

"""We are taking the user's input outside the first function and taking it as an argument

1. Define the function
2. Take the user inout
3. Call the function using the user input data
"""