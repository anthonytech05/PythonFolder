
# i would write this over here 

"""
this section of 
code would 
be used to 
point out where 
we discovered 
bugs 
..CODE DOCUMENTATION 
"""

customer_name = "John Rufus"
cash_at_hand = 5700

price_of_bag = 95000

GOLD = '\033[1;33m'
GREEN = '\033[1;32m'
BOLD ='\033[1m'
RESET = '\033[0m'

print(GREEN + "="*40 + RESET)
print(GOLD + 'SHOPRITE'.center(40) + RESET)
print(GREEN + "="*40 + RESET)
print(f'Welcome {customer_name}, you can use your NGN{cash_at_hand} to shop at discounted price')
print(f'BAG PRICE :    NGN{price_of_bag:,.2f}')
print(GREEN + "-"*40 + RESET)