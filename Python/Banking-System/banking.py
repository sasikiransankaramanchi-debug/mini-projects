class Account:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def account_details(self):
        print("Account Number:", self.acc_no)
        print("Account Holder:", self.name)
        print("Current Balance:", self.balance)
        
    def debit(self):
        a = int(input("enter the amount to withdraw: "))
        print("the total balance is: ",self.balance)
        if(a>self.balance):
            print("you have insufficient balance")
        else:
            self.balance = self.balance - a
            print("you have withdrawn: ",a)
            print("the remaining balance is: ",self.balance)

    def credit(self):
        a = int(input("enter the amount to deposit: "))
        print("the total balance is: ",self.balance)
        self.balance= self.balance + a
        print("you have deposited: ",a)
        print("the remaining balance is: ",self.balance)

    def total_balance(self):
        print("the total balance with acc no:",self.acc_no,"is:",self.balance)

accounts = [
     Account(100100, "Sasikiran", 50000),
    Account(200200, "Rahul", 60000),
    Account(300300, "Kiran", 70000),
    Account(400400, "Arun", 80000),
    Account(500500, "Ravi", 90000)
]        

acc_no = int(input("Enter your account number: "))

# Search for the account
selected_account = None

for account in accounts:
    if account.acc_no == acc_no:
        selected_account = account
        break


# Check whether account exists
if selected_account is None:
    print("Account not found")

else:

    print("\nWelcome", selected_account.name)
    while True:

        print("\n========== BANK ACCOUNT ==========")
        print("1. Account Details")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Check Balance")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            selected_account.account_details()

        elif choice == 2:
            selected_account.debit()

        elif choice == 3:
            selected_account.credit()

        elif choice == 4:
            print("Current Balance:", selected_account.balance)

        elif choice == 5:
            print("Thank you for using the Bank Account System")
            break

        else:
            print("Invalid choice")
