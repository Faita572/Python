# Our starting database
phone_book = {
    "Lada": "555-1234",
    "Khem": "555-4567",
    "Rin": "555-8901"
}

print("--- PHONE BOOK LOOKUP ---")
search_name = input("Enter a name to look up their number: ")

# Convert to lowercase so it matches our keys perfectly
clean_name = search_name.lower()

# Check if the name exists inside our dictionary keys
if clean_name in phone_book:
    number = phone_book[clean_name]
    print(search_name + "'s number is " + number)
else:
    print("Sorry, " + search_name + " was not found in the phone book.")