# Jeremiah Pineda
# SWDV630
# WEEk 2 Assignment


class CheckingAccount:

    def __init__(self, name, address, acct_number, initial_balance):
        # public attributes
        self.name = name
        self.address = address
        self.accountNumber = acct_number

        # private attribute
        self.__balance = initial_balance
        self.__begBalance = initial_balance
        self.__transAmount = 0

        # deposit,withdrawal, for Printout
        self.__transType = ''

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_account_number(self):
        return self.accountNumber

    def check_balance(self):
        return self.__balance

    def withdraw(self, debit):
        print("Withdrawing " + str(debit) + " from " + self.name + " account")
        if self.check_balance() < debit:
            print ("Insufficient funds from account " + str(self.accountNumber) + " Name: " + self.name)
        else:
            self.__balance = self.check_balance() - debit
            self.__transAmount = debit
            self.__transType = 'Withdrawal'

        return self.check_balance()

    def deposit(self, credit):
        self.__balance = self.check_balance() + credit
        self.__transAmount = credit
        self.__transType = 'Deposit'

        return self.check_balance()

    def print_receipt(self):
        print("\n__________________________________________")
        print()
        print("Transaction Report")
        print()
        print("Name: " + self.name)
        print("Address: " + self.address)
        print("Account Number: " + str(self.accountNumber))
        print()
        print("__________________________________________")
        print("Beginning Balance: " + str(self.__begBalance))
        print("__________________________________________")
        print()
        print("Transaction type: {}".format(self.__transType))
        print("\nTransaction Amount: ${:.>11}".format(self.__transAmount))
        print("Balance: ${:.>22}".format(self.check_balance()))
        print()
        print("__________________________________________")
        # Just to have the correct display between withdrawal and deposit
        self.__begBalance = self.__balance


def check_balances(c1, c2, c3):
    print("\n********************************************")
    print("           CHECKING BALANCES")
    print("********************************************")
    print("Customer 1 Balance: {}".format(c1.check_balance()))
    print("Customer 2 Balance: {}".format(c2.check_balance()))
    print("Customer 3 Balance: {}".format(c3.check_balance()))
    print("*******************************************")


def print_receipts(c1, c2, c3):
    c1.print_receipt()
    c2.print_receipt()
    c3.print_receipt()
    print("*******************************************")

# DRIVER APP
def main():
    # Instantiate objects
    customer1 = CheckingAccount("Steve Roger", "144 ST NW Champagne DR, CA 90210", 8854345, 1000)
    customer2 = CheckingAccount("Shirley Temple", "1 Mahogany Dr., Phoenix AZ 85005", 88433451, 200)
    customer3 = CheckingAccount("Bell Anderson", "895 South Paw St. Bellview, FL 34420", 88433422, 0)

    # Check Balances
    check_balances(customer1, customer2, customer3)

    # Withdrawals
    print("********************************************")
    print("           MAKING WITHDRAWALS")
    print("********************************************")
    customer1.withdraw(50)
    customer2.withdraw(10)
    customer3.withdraw(20)

    # Check Balances
    check_balances(customer1, customer2, customer3)
    print_receipts(customer1, customer2, customer3)

    # Deposit money
    print("********************************************")
    print("           MAKING DEPOSITS")
    print("********************************************")
    customer1.deposit(45)
    customer2.deposit(15)
    customer3.deposit(100)

    # Check Balance
    print_receipts(customer1, customer2, customer3)
    check_balances(customer1, customer2, customer3)


main()




