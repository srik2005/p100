class Atm:
    def __init__(self,card_no,pin_no):
        self.balance = 0
        print("The account is created")
        

    def deposit(self):
        amount = int(input("Enter the amount to be deposited: "))
        self.balance = self.balance + amount
        print ("Deposit is successful and the balance is %f" % self.balance)

    def withdraw(self):
        amount = int(input("Enter the amount for the withdrawal: "))
        if (self.balance >= amount):
            self.balance = self.balance - amount
            print("Withdrawal is Successfull and the balance is %f " % self.balance)

        else:
            print("Insuffient Balance!!")
        
acc = Atm('124','567')
acc.deposit()
acc.withdraw()
