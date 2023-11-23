    #davaleba2
input_names = input("Enter names: ")

names = input_names.split()

filtered_names = [name for name in names if name[0].isupper()]

result_length = len(filtered_names)

print("Length of Filtered List:", result_length)





    #davaleba1
import random

input_numbers = input("Enter some numbers: ")

numbers = list(map(float, input_numbers.split()))

random_number = random.choice(numbers)

result = list(map(lambda x: x * random_number, numbers))

print("The number that gets multiplied:", random_number)
print("Result List:", result)



   
   
   
    #davaleba3
input_numbers = input("Enter numbers: ")

numbers = list(map(float, input_numbers.split()))

positive_numbers = list(filter(lambda x: x > 0, numbers))
negative_numbers = list(filter(lambda x: x < 0, numbers))

sum_positive = sum(positive_numbers)
sum_negative = sum(negative_numbers)

print("Positive Numbers:", positive_numbers)
print("Sum of Positive Numbers:", sum_positive)
print("Negative Numbers:", negative_numbers)
print("Sum of Negative Numbers:", sum_negative)



  
  
  
    #davaleba4
class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        try:
            amount = float(amount)
            if amount > 0:
                self.balance += amount
                print(f"Deposited {amount:.2f} Dollars. New balance: {self.balance:.2f} Dollars")
            else:
                print("Deposit amount must be a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

    def login(self, entered_account_number):
        try:
            entered_account_number = int(entered_account_number)
            if entered_account_number == self.account_number:
                print("Login successful!")
                print(f"Current balance: {self.balance:.2f} Dollars")
            else:
                print("Account number is incorrect. Login failed.")
        except ValueError:
            print("Invalid input. Please enter a valid account number.")

if __name__ == "__main__":
    account_number = 12345 
    bank_account = BankAccount(account_number)

    while True:
        print("\nBank Menu:")
        print("1. Deposit Money")
        print("2. Login to Account")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            deposit_amount = input("Enter the deposit amount: ")
            bank_account.deposit(deposit_amount)
        elif choice == '2':
            entered_account_number = input("Enter your account number: ")
            bank_account.login(entered_account_number)
        elif choice == '3':
            print("Exiting the bank application. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")





