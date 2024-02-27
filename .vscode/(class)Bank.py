class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount} in your account successfully."
     
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance."
        else:
            self.balance -= amount
            return f"Withdrawn {amount} from your account successfully."

    def check_balance(self):
        return f"Your current balance is {self.balance}."

    def customer_details(self):
        return f"Customer name: {self.customer_name}\nAccount number: {self.account_number}\nAccount balance: {self.balance}\nAccount opening date: {self.date_of_opening}"

# Create an instance of the BankAccount class
bank_account = BankAccount(345556, 679098830000, "12-02-2021", "John Doe")

# Loop for user interaction
while True:
    print("\nChoose an option:")
    print("1. Deposit")
    print("2. Check Balance")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        amount = float(input("Enter the amount to deposit: "))
        print(bank_account.deposit(amount))
    elif choice == '2':
        print(bank_account.check_balance())
    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: "))
        print(bank_account.withdraw(amount))
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please select a valid option.")
