class Account:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}₹. New balance: {self.balance}₹")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}₹. New balance: {self.balance}₹")
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"\nAccount Number: {self.account_number}\nAccount Holder: {self.account_holder}\nBalance: {self.balance}₹"


bank_account = Account("123456789", "Radhey Patil", 1000)
print(bank_account)

while True:
    print()
    print(" 1.deposit \n 2.withdraw \n 3.check account info \n 4.exit")
    
    option=int(input("\nenter your choice: "))
    if(option==1):
        amount=int(input("enter amount to deposit"))
        bank_account.deposit(amount)
    elif(option==2):
        withdraw_amount=int(input("enter amount to withdraw"))
        bank_account.withdraw(withdraw_amount)
    elif(option==3):
        print(bank_account)
    elif(option==4):
        break    
    else:
        print("wrong input choosen")




    
