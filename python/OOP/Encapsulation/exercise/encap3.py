class BankAccount:
    def __init__(self):
        self._checking = 0.0
        self._savings = 0.0

    # Getter for checking
    def get_checking(self):
        return self._checking

    # Setter for checking
    def set_checking(self, amount):
        self._checking = amount

    # Getter for savings
    def get_savings(self):
        return self._savings

    # Setter for savings
    def set_savings(self, amount):
        self._savings = amount

# Initialize an object of the BankAccount class
my_account = BankAccount()

# Set checking and savings balances
my_account.set_checking(523.48)
print(my_account.get_checking())  # Output: 523.48

my_account.set_savings(386.15)
print(my_account.get_savings())   # Output: 386.15
