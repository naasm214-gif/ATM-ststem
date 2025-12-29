class login:
    def __init__(self,pin,account_no):
        self.id_no = ""
        self.pin = pin
        self.account_no = account_no


class sign_up:
    def __init__(self):
        self.balance = 0
        self.pin = ""
        self.menu()
          
    def menu(self):
        while True:
            print("""
                ATM MENU 
            1. Create PIN
            2. Deposit
            3. Withdraw
            4. Check Balance
            5. Exit
            """)

            choice = input("Enter choice: ")

            if choice == "1":
                self.create_pin()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                self.check_balance()
            elif choice == "5":
                print("Thank you for using ATM")
                break
            else:
                print("Invalid choice")

    def create_pin(self):
        p = input("Enter new PIN: ")
        print("PIN created successfully")
        self.pin=p

    def deposit(self):
        amount = int(input("Enter deposit amount: "))
        self.balance += amount
        print("Deposit successful")

    def withdraw(self):
        entered_pin = input("Enter PIN: ")
        if entered_pin == self.pin:
            amount = int(input("Enter withdraw amount: "))
            if amount <= self.balance:
                self.balance -= amount
                print("Withdraw successful")
            else:
                print("Insufficient balance")
        else:
            print("Wrong PIN")

    def check_balance(self):
        entered_pin = input("Enter PIN: ")
        if entered_pin == self.pin:
            print("Your balance is:", self.balance)
        else:
            print("Wrong PIN")


login_account = login()
sign_up_account = sign_up()

print("====== Well come to ATM System ======== ")
user = int(input("""New account / press 1 
                 Login account / press 2
                 """))
if user==1 :
    sign_up_account()
elif user==2:
    login_account()

else:
    print("Wrong typing")
