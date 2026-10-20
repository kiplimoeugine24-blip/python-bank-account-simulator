account_balance = 0.00
def bank_account_simulator(operation):
    global account_balance

    if operation == "deposit":
        amount = float(input("Enter the amount to deposit: "))
        if amount > 0:
    
           account_balance += amount
           print(f"Deposited: ${amount:.2f}. New balance: ${account_balance:.2f}")
        elif amount <= 0:
           print("Enter a valid positive amount")
    elif operation == "withdraw":
        amount = float(input("Enter the amount to withdraw: "))
        if 0 < amount <= account_balance:
            account_balance -= amount
            print(f"Withdrew: ${amount:.2f}. New balance: ${account_balance:.2f}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")
    elif operation == "check_balance":
     print(f"Current balance: ${account_balance:.2f}")
    elif operation == "exit":
     print("Exiting the bank account simulator.")

    else:
      print("Invalid operation. Please try again.")
while True:
    print("\nBank Account Simulator")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    
    choice = input("Choose an operation (1-4): ")
    
    if choice == "1":
        bank_account_simulator("deposit")
    elif choice == "2":
        bank_account_simulator("withdraw")
    elif choice == "3":
        bank_account_simulator("check_balance")
    elif choice == "4":
        bank_account_simulator("exit")
        break
    else:
        print("Invalid choice. Please select a valid operation.")