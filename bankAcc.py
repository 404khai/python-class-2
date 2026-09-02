class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    # THIS IS AN EXAMPLE OF ENCAPSULATION IN THE SENSE THAT balance CAN ONLY BE MODIFIED OR ACCESSED THROUGH THIS DEPOSIT FUNCTION
    # Encapsulation means keeping related data and behaviour together and controlling how data is accessed or modified.
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount


# THIS WILL RETURN AN ERROR...YOU CAN'T MODIFY OR ACCESS BALANCE OUTSIDE THE CLASS OR WITHOUT THE DEPOSIT FUNCTION IN THE CLASS
# def deposit2(amount2):
#     balance += amount2
    
myAcc = BankAccount(400)

myAcc.deposit(500)
print(myAcc.balance)
