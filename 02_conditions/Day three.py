    # 1. Get the user's age and convert it to a whole number (Integer)
age_input = input("Enter your age: ")
age = int(age_input)

# 2. Make the decision
if age < 12:
    # This runs ONLY if age is less than 12
    price = 8
    print("You get the child discount!")

elif age >= 65:
    # This runs ONLY if they aren't a child, but are 65 or older
    price = 10
    print("You get the senior discount!")

else:
    # This runs if NONE of the conditions above were true
    price = 15
    print("Regular ticket pricing applies.")

# 3. Print the final result
print("Your total is: $" + str(price))