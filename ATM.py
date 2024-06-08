def withdraw(i):
    while True:
        try:
            amount = int(input("Enter amount: "))
            if amount <= 0:
                print("Amount must be a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid amount.")
    pinno = int(input("Enter PIN: "))
    if pinno != pin[i]:
        print("PIN is incorrect.")
    else:
        if amount > bal[i]:
            print("Insufficient balance.")
        else:
            bal[i] -= amount
            print("Withdrawal successful.")
            print("Do you want to check available balance? y/n")
            if input().lower() == 'y':
                print("Available balance: ", bal[i])
                print("Thank you for banking.")
            else:
                print("Thank you for banking.")

def deposit(i):
    while True:
        try:
            amount = int(input("Enter amount: "))
            if amount <= 0 or amount % 100 != 0:
                print("Amount must be a multiple of 100.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid amount.")
    bal[i] += amount
    print("Deposit successful.")
    print("Do you want to check available balance? y/n")
    if input().lower() == 'y':
        print("Available balance: ", bal[i])
        print("Thank you for banking.")
    else:
        print("Thank you for banking.")

def account_balance(i):
    print("Available balance: ", bal[i])
    print("Thank you for banking.")

def change_password(i):
    while True:
        new_password = input("Enter new password: ")
        confirm_password = input("Confirm new password: ")
        if new_password != confirm_password:
            print("Passwords do not match. Please try again.")
        else:
            pswd[i] = new_password
            print("Password changed successfully.")
            break

def ATM(i):
    attempts = 3
    while attempts > 0:
        pass_code = input("Enter your password: ")
        if pass_code == pswd[i]:
            print("Password is correct.")
            break
        else:
            print("Password is incorrect and", attempts, "more attempts are left.")
            attempts -= 1
    if attempts == 0:
        print("Login failed.")
        return False
    else:
        while True:
            print("1. Withdraw")
            print("2. Deposit")
            print("3. Account balance")
            print("4. Change password")
            print("5. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                withdraw(i)
            elif choice == 2:
                deposit(i)
            elif choice == 3:
                account_balance(i)
            elif choice == 4:
                change_password(i)
            elif choice == 5:
                print("Thank you for banking.")
                return True
            else:
                print("Invalid choice. Please try again.")

user = ['sai', 'sushma', 'akhila']
pswd = ['sai2', 'sushma25', 'akhila5']
pin = [2043, 2002, 2025]
bal = [25000, 30000, 5000]

print("Enter user name:")
user_name = input()
if user_name in user:
    i = user.index(user_name)
    if ATM(i):
        print("Logged in successfully")
    else:
        print("login failed")
else:
    print("user not exist")