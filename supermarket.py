print("="*40)
print('WELCOME TO JAX SUPERMARKET')
print('='*40)

total = 0.0
while True:
    item = input('Enter item price or type done:')

    if item.lower() == 'done':
        break
    try:
        price = float(item)
        if price <0:
            print('price cannot be negative. try again')
            continue
        total += price
    except ValueError:
        print('invalid input. Please enter a valid number.')
print("\nTotal amount pay:", total)
