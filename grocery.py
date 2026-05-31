# Grocery Receipt

item_name = input("Enter item name: ")


try :
    price = float(input("Enter price per item: "))
    quantity = int(input("Enter quantity: "))
    tax_rate = float(input("Enter tax rate (%): "))

    subtotal = price * quantity
    tax_amount = subtotal * tax_rate / 100
    total = subtotal + tax_amount


    print("="*40)

    print("SHOPRITE".center(50))

    print("Cairo Rd Lusaka".center(50))

    print("="*40)

    print(f"Item:        {item_name:<20} {price:>7.2f}")

    print(f"Subtotal:{'':>26}{subtotal:>7.2f}")

    print(f"Tax ({tax_rate:.0f}%):{'':>23}{tax_amount:>7.2f}")

    print("-"*40)

    print(f"TOTAL:{'':>29}{total:>7.2f}")

    print("="*40)

except ValueError as e :
    print(e)

except TypeError as e :
    print(e)

except Exception as error :
    print('An error occurred!')
    print(error)


print('Application proceeds as if nothing happens')
