""""
Write a script: fuel_budget.py
Ask: How much money do you have? (use a variable, not input() yet)
Define the current pump price per litre.
Calculate how many litres you can afford.
Also calculate litres if the price increases by 10%.
Print a formatted comparison showing both scenarios.
"""


GREY = '\033[1;30m' 
RED = '\033[1;31m'
GREEN = '\033[1;32m'
GOLD = '\033[1;33m'
BLUE = '\033[1;34m'
BOLD ='\033[1m'
RESET = '\033[0m'

# Set your available money (no input() yet)
money = 20000  # change this value as needed

# Current pump price per litre
price_per_litre = 650  # example price in your currency

# Calculate litres you can afford at current price
litres_now = money / price_per_litre

# Increase price by 10%
increased_price = price_per_litre * 1.10

# Calculate litres you can afford after price increase
litres_after_increase = money / increased_price

# Print formatted comparison
print( BLUE + "FUEL BUDGET COMPARISON" + RESET)
print("-" * 30)
print(f"Available money: NGN{money:,.2f}")
print(f"Current price per litre: ₦{price_per_litre:.2f}")
print(f"Litres you can buy now: {litres_now:.2f}L")
print()
print(f"Price after 10% increase: ₦{increased_price:.2f}")
print(f"Litres you can buy after increase: {litres_after_increase:.2f}L")