class BankAccount:
    def __init__(self, owner, starting_balance):
        self.owner = owner
        self.__balance = starting_balance  # The '__' makes this private!

    # A controlled way to check the balance (Getter)
    def show_balance(self):
        print(self.owner + "'s balance is: $" + str(self.__balance))

    # A controlled way to change the balance with safety checks (Setter)
    def deposit(self, amount):
        if amount > 0:
            self.__balance = self.__balance + amount
            print("Deposited $" + str(amount))
        else:
            print("Error: You can't deposit a negative number!")

account = BankAccount("Alex", 100)

account.deposit(50)
account.show_balance()  # Balance is safely updated to $150