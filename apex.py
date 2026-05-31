print("="*40)
print("WELCOME TO APEX FUEL STATION")
print('='*40)

total = 0.0
count = 0
highest = 0
amount = 0

while True:
    amount = input('Enter item amount or type done: ')

    if amount.lower() == 'done':
        break
    try:
        amount = float(amount)
        if amount < 0:
            print('Negative amounts are not allowed!')
            continue
        total += amount
        count += 1

        if amount > highest:
            highest = amount

    except ValueError:
        print('Invalid input. Please enter a valid numbers only.')
if count > 0:
    average = total / count
else:
    average = 0

    print("\n------ RECEIPT ------")
    print("\nTotal amount to pay:", total)
    print("Number of items entered:", count)
    print("Average amount:", average)
    print("Highest item amount:", highest)