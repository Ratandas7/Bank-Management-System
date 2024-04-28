import random

class User:
    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.account_number = random.randint(20000000, 99999999)
        self.transaction_history = []
        self.loan_taken = 0
        self.loan_times = 0

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited {amount} Taka")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew {amount} Taka")

        else:
            print("Withdrawal amount exceeded")

    def check_balance(self):
        return self.balance

    def check_transaction_history(self):
        return self.transaction_history

    def take_loan(self, amount):
        if self.loan_times < 2:
            self.loan_taken += amount
            self.balance += amount
            self.loan_times += 1
            self.transaction_history.append(f"Took a loan of {amount} Taka")

        else:
            print("You have already taken maximum loans.")

    def transfer(self, amount, recipient):
        if self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f"Transferred {amount} Taka to {recipient.name}")

        else:
            print("Not enough funds to transfer")

class Admin:
    def __init__(self):
        self.users = []
        self.loan_feature_enabled = True

    def create_account(self, name, email, address, account_type):
        user = User(name, email, address, account_type)
        self.users.append(user)
        return user

    def delete_account(self, user):
        self.users.remove(user)

    def get_all_accounts(self):
        return self.users

    def total_balance(self):
        total_balance = sum(user.balance for user in self.users)
        return total_balance

    def total_loan_amount(self):
        total_loan = sum(user.loan_taken for user in self.users)
        return total_loan

    def loan_feature(self):
        self.loan_feature_enabled = not self.loan_feature_enabled
        status = "enabled" if self.loan_feature_enabled else "disabled"
        print(f"Loan feature is now {status}.")

class Bank:
    def __init__(self):
        self.admin = Admin()
        self.current_user = None

    def user_menu(self):
        while True:
            print("\nUser Menu:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Check Transaction History")
            print("5. Take Loan")
            print("6. Transfer Money")
            print("7. Logout")

            choice = input("Enter your choice: ")

            if choice == "1":
                amount = float(input("Enter amount to deposit: "))
                self.current_user.deposit(amount)
            
            elif choice == "2":
                amount = float(input("Enter amount to withdraw: "))
                if self.admin.loan_feature_enabled:
                    self.current_user.withdraw(amount)

                else:
                    print("Bank is bankrupt!! You Cannot withdraw deposited amount.")

            elif choice == "3":
                print("Available Balance:", self.current_user.check_balance())

            elif choice == "4":
                print("Transaction History:", self.current_user.check_transaction_history())

            elif choice == "5":
                if self.admin.loan_feature_enabled:
                    amount = float(input("Enter loan amount: "))
                    self.current_user.take_loan(amount)

                else:
                    print("Loan feature is currently disabled by admin.")

            elif choice == "6":
                recipient_name = input("Enter recipient's name: ")

                recipient = None
                for user in self.admin.get_all_accounts():
                    if user.name == recipient_name:
                        recipient = user
                        break

                if recipient:
                    amount = float(input("Enter amount to transfer: "))
                    self.current_user.transfer(amount, recipient)

                else:
                    print("Account does not exist.")

            elif choice == "7":
                print("Logged out successfully.")
                break

            else:
                print("Invalid choice.")

    def admin_menu(self):
        while True:
            print("\nAdmin Menu:")
            print("1. Create Account")
            print("2. Delete Account")
            print("3. All User Accounts List")
            print("4. Check Total Balance")
            print("5. Check Total Loan Amount")
            print("6. Loan Feature (On/Off)")
            print("7. Logout")

            choice = input("Enter your choice: ")

            if choice == "1":
                name = input("Enter user name: ")
                email = input("Enter user email: ")
                address = input("Enter user address: ")
                account_type = input("Enter account type (Savings/Current): ")
                user = self.admin.create_account(name, email, address, account_type)
                print("Account created successfully. Account number:", user.account_number)
            
            elif choice == "2":
                account_number = int(input("Enter account number to delete: "))

                user = None
                for account in self.admin.get_all_accounts():
                    if account.account_number == account_number:
                        user = account
                        break

                if user:
                    self.admin.delete_account(user)
                    print("Account deleted successfully.")

                else:
                    print("Account not found.")

            elif choice == "3":
                print("All Accounts:")
                for user in self.admin.get_all_accounts():
                    print(f"Name: {user.name}, Account Number: {user.account_number}")

            elif choice == "4":
                print("Total Balance:", self.admin.total_balance())

            elif choice == "5":
                print("Total Loan Amount:", self.admin.total_loan_amount())

            elif choice == "6":
                self.admin.loan_feature()

            elif choice == "7":
                print("Logged out successfully.")
                break

            else:
                print("Invalid choice.")
    
    def run(self):
        while True:
            print("\nWelcome to ABC BANK")
            print("1. User Login")
            print("2. Admin Login")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                account_number = int(input("Enter your account number: "))

                user = None
                for u in self.admin.get_all_accounts():
                    if u.account_number == account_number:
                        user = u
                        break

                if user:
                    print("Login successful.")
                    self.current_user = user
                    self.user_menu()

                else:
                    print("Account not found.")

            elif choice == "2":
                admin_username = input("Enter Username: ")
                admin_password = input("Enter Password: ")

                if admin_username == "admin" and admin_password == "admin123":
                    print("Login successful.")
                    self.admin_menu()

                else:
                    print("Incorrect password.")

            elif choice == "3":
                print("Thank you for using our Bank. Goodbye!")
                break

            else:
                print("Invalid choice.")

bank_system = Bank()
bank_system.run()