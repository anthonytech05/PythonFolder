"""
File: currency_converter.py
Define exchange rate variables: USD_RATE = 1580, GBP_RATE = 2010, EUR_RATE = 1710
Define an amount: naira_amount = 50000
Calculate the equivalent in USD, GBP, and EUR.
Print a formatted conversion report with all three results.
BONUS: Add a 1.5% international transfer fee and show the amount after the fee.
BONUS: Show the conversion both ways (Naira → USD and USD → Naira)
"""


GREY = '\033[1;30m'
RED = '\033[1;31m'
GREEN = '\033[1;32m'
GOLD = '\033[1;33m'
BLUE = '\033[1;34m'
BOLD ='\033[1m'
RESET = '\033[0m'



USD_RATE = 1580
GBP_RATE = 2010
EUR_RATE = 1710


naira_amount = 50000


usd_amount = naira_amount / USD_RATE
gbp_amount = naira_amount / GBP_RATE
eur_amount = naira_amount / EUR_RATE


fee_rate = 0.015
naira_after_fee = naira_amount * (1 - fee_rate)

usd_after_fee = naira_after_fee / USD_RATE
gbp_after_fee = naira_after_fee / GBP_RATE
eur_after_fee = naira_after_fee / EUR_RATE


usd_to_naira = usd_amount * USD_RATE  


print(GREEN + "CURRENCY CONVERSION REPORT" + RESET)
print("-" * 40)

print(f"Original Amount: ₦{naira_amount:,.2f}")
print()

print("Naira → Foreign Currency:")
print(f"USD: ${usd_amount:.2f}")
print(f"GBP: £{gbp_amount:.2f}")
print(f"EUR: €{eur_amount:.2f}")
print()

print("After 1.5% Transfer Fee:")
print(f"Remaining Naira: ₦{naira_after_fee:,.2f}")
print(f"USD: ${usd_after_fee:.2f}")
print(f"GBP: £{gbp_after_fee:.2f}")
print(f"EUR: €{eur_after_fee:.2f}")
print()

print("Reverse Conversion (USD → Naira):")
print(f"${usd_amount:.2f} = ₦{usd_to_naira:,.2f}")