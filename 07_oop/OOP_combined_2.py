#A streaming service
#You shouldn't be able to change your subscription status or password without passing safety checks
# Encapsulation makes sure that your data is hidden using double underscores __.

class StreamingAccount:
    def __init__(self, email, password):
        self.email = email
        self.__password = password
        self.__is_premium = False

    # A safe way to update the password (Setter)
    def update_password(self, old_pass, new_pass):
        if old_pass == self.__password:
            self.__password = new_pass
            print("Password updated successfully!")
        else:
            print("Error: Old password did not match. Access denied.")

    # A safe way to upgrade the account
    def purchase_premium(self, payment_amount):
        if payment_amount >= 15.00:
            self.__is_premium = True
            print("Thank you! Your account is now Premium")
            
    def check_premium_status(self):
        return self.__is_premium
    
    #To create premium or family accounts, they need to inherit the data from the
    #StreamingAccount class but add extra features

    # FamilyAccount inherits everything from StreamingAccount
class FamilyAccount(StreamingAccount):
    def __init__(self, email, password, profile_limit):
        # super() calls the parent class's __init__ to set up email and password
        super().__init__(email, password)
        self.profile_limit = profile_limit
        
    def show_family_dashboard(self):
        print(f"Family Dashboard active with {self.profile_limit} user profiles allowed.")

# Testing our classes
# Create a regular account
user_1 = StreamingAccount("anna@email.com", "supersecure123")

# Try to update password with the wrong old password
user_1.update_password("wrong_password", "new_password_456")

# Upgrade to premium
user_1.purchase_premium(15.00)
print(f"Is user premium? {user_1.check_premium_status()}")

# Create a family account
user_2 = FamilyAccount("barbie@email.com", "familysecure456", 5)
user_2.show_family_dashboard()