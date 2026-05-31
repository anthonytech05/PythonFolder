customer_name = "Daniel Musa"
transaction_date = "2026-05-12"
account_balance = "850000"
transfer_amount = "12500.75"
pin_attempt = "3"
account_active = "True"
loan_cleared =  "1"


account_balance = int(account_balance)
transfer_amount = float(transfer_amount)
pin_attempt = int(pin_attempt)
account_active = bool(account_active)
loan_cleared = bool(loan_cleared)


 
print(type(customer_name), customer_name)
print(type(transaction_date), customer_name)
print(type(account_balance), account_balance)
print(type(transfer_amount), transfer_amount)
print(type(pin_attempt), pin_attempt)
print(type(account_active), account_active)
print(type(loan_cleared), loan_cleared)
