CORRECT_PIN = "1234"
balance = 150000.00

print("=" * 40)
print(" WELCOME TO PYBANK ATM")
print("=" * 40)

pin = input("Enter your 4-digit PIN: ")

if pin != CORRECT_PIN:
    print("Incorrect PIN. Card retained. Contact your bank.")
else:
    print(f"PIN correct. Balance: N{balance:,.2f}")
    
    action = input("Choose: [1] Withdraw [2] Check Balance [3] Deposit: ")
    
    transaction_type = None
    amount = 0

    if action == "1": 
        try:
            amount = float(input("Enter amount to withdraw: N"))
            
            if amount <= 0:
                print("Amount must be positive.")
            elif amount % 500 != 0:
                print("Amount must be in multiples of N500.")
            elif amount > balance:
                print("Insufficient funds.")
            elif amount > 50000:
                print("Daily withdrawal limit is N50,000.")
            else:
                balance -= amount
                transaction_type = "Withdrawal"
                print(f"Dispensing N{amount:,.2f}.")
        
        except ValueError:
            print("Invalid amount entered.")

    elif action == "2": 
        transaction_type = "Balance Check"
        print(f"Current balance: N{balance:,.2f}")

    elif action == "3": 
        try:
            amount = float(input("Enter amount to deposit: N"))
            
            if amount <= 0:
                print("Amount must be positive.")
            elif amount % 500 != 0:
                print("Deposit must be in multiples of N500.")
            else:
                balance += amount
                transaction_type = "Deposit"
                print(f"N{amount:,.2f} deposited successfully.")
        
        except ValueError:
            print("Invalid amount entered.")

    else:
        print("Invalid option selected.")

   
    if transaction_type:
        print("=" * 30)
        print("        TRANSACTION RECEIPT")
        print("=" * 30)
        print(f"Type: {transaction_type}")
        if action != "2":
            print(f"Amount: N{amount:,.2f}")
        print(f"Available Balance: N{balance:,.2f}")
        print("=" * 30)

    print("Thank you for banking with PyBank!")