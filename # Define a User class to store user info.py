# Define a User class to store user information
class User:
    def __init__(self, user_id, pin, balance=0):
        self.user_id = user_id
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited ${amount}")
            return True
        return False

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
            return True
        return False

    def transfer(self, recipient, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f"Transferred ${amount} to {recipient.user_id}")
            recipient.transaction_history.append(f"Received ${amount} from {self.user_id}")
            return True
        return False

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transaction_history


# Create a simple ATM class to handle user interactions
class ATM:
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        self.users[user.user_id] = user

    def authenticate_user(self, user_id, pin):
        if user_id in self.users and self.users[user_id].pin == pin:
            return self.users[user_id]
        return None

    def display_menu(self):
        print("\nATM Menu:")
        print("1. Display Transaction History")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. Quit")

    def run(self):
        while True:
            print("\nWelcome to the Python ATM!")
            user_id = input("Enter your User ID: ")
            pin = input("Enter your PIN: ")

            user = self.authenticate_user(user_id, pin)

            if user:
                print(f"Welcome, {user.user_id}!")
                while True:
                    self.display_menu()
                    choice = input("Enter your choice: ")

                    if choice == "1":
                        print("\nTransaction History:")
                        for transaction in user.get_transaction_history():
                            print(transaction)
                    elif choice == "2":
                        amount = float(input("Enter the deposit amount: $"))
                        if user.deposit(amount):
                            print("Deposit successful.")
                        else:
                            print("Invalid deposit amount.")
                    elif choice == "3":
                        amount = float(input("Enter the withdrawal amount: $"))
                        if user.withdraw(amount):
                            print("Withdrawal successful.")
                        else:
                            print("Invalid withdrawal amount.")
                    elif choice == "4":
                        recipient_id = input("Enter recipient's User ID: ")
                        if recipient_id in self.users:
                            recipient = self.users[recipient_id]
                            amount = float(input("Enter the transfer amount: $"))
                            if user.transfer(recipient, amount):
                                print("Transfer successful.")
                            else:
                                print("Invalid transfer amount.")
                        else:
                            print("Recipient not found.")
                    elif choice == "5":
                        print("Thank you for using the Python ATM!")
                        return
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Invalid User ID or PIN. Please try again.")


# Sample usage
if __name__ == "__main__":
    atm = ATM()
    user1 = User("user1", "1234", 1000)
    user2 = User("user2", "5678", 500)
    atm.add_user(user1)
    atm.add_user(user2)
    atm.run()
