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

#Currency converter
def convert_usd_to_inr(usd_amount):
    # Let's assume 1 USD = 95.41 INR
    exchange_rate = 95.41
    inr_result = usd_amount * exchange_rate
    return inr_result

# 2. Get input from the user
raw_input = input("Enter the amount in USD ($): ")
clean_usd = float(raw_input)
final_inr = convert_usd_to_inr(clean_usd)
print("Total value: ₹" + str(final_inr))