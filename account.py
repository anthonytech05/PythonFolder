GREY = '\033[1;30m'
RED = '\033[1;31m'
GREEN = '\033[1;32m'
GOLD = '\033[1;33m'
BLUE = '\033[1;34m'
BOLD ='\033[1m'
RESET = '\033[0m'


yearly_balance = 58750000
tax_rate = 12.5

yearly_balance = 58750000
tax_rate = 12.5 / 100

tax_amount = yearly_balance * tax_rate
remaining_balance = yearly_balance - tax_amount


print("====== ACCOUNT BALANCE REPORT ======")
print(BLUE + f"Tax amount {RESET} {GREEN}   NGN{tax_amount:,.3f}" + RESET)
print(GOLD + f"balance:  NGN{remaining_balance:,}" + RESET)
print(GREEN + f"Tax rate {RESET}  {BLUE}   NGN{tax_rate:,}%" + RESET) 