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
            print("Thank you! Your account is now Premium ✨")
            
    def check_premium_status(self):
        return self.__is_premium