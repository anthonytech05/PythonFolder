GREY = '\033[1;30m'
RED = '\033[1;31m'
GREEN = '\033[1;32m'
GOLD = '\033[1;33m'
BLUE = '\033[1;34m'
BOLD ='\033[1m'
RESET = '\033[0m'

"""
As an accountant you are tasked to document the amount to be charged on a user balance, present the tax rate to be applied the user balance, show the balance that would be left afterthe tax has been applied in a well structured readable format and layout 

year_balance = 42305860
tax = 8.5 
"""


year_balance = 4238560
tax = 8.5 / 100

tax_amount = year_balance * tax
remaining_balance = year_balance - tax_amount

print(GREY + "="*50 + RESET)
print(f'{GREEN} {"TAX RECEIPT".center(50)} {RESET}')
print(GREY + "="*50 + RESET)
print(BLUE + f"Tax amount {RESET} | {RED} NGN{tax_amount:,.3f}" + RESET)
print(GOLD + f"balance:NGN{remaining_balance:,}" + RESET)
# print(f'{"END":<10} I AM HERE')
print(GREY + "="*50 + RESET)