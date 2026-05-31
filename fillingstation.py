#filling station

fuel_name = input("Enter fuel type: ")

try :
    price = float(input("Enter price per litre: "))
    litres = int(input("Enter number of litres to be purchased: "))
    vat_rate = float(input("Enter vate rate (%)"))


    subtotal = price * litres
    vat_amount = subtotal * vat_rate / 100
    total = subtotal + vat_amount

    
    
    print("="*40)

    print("MEGA FUEL STATION".center(50))

    print("Victoria Island".center(50))

    print("="*40)

    print(f"Fuel:           {fuel_name:<20} {price:>7.2f}")

    print(f"Subtotal:{'':>26} {subtotal:>7.2f}")

    print(f"Tax ({vat_rate:.0f}%):{'':>23} {vat_amount:>7.2f}")

    print("-"*40)

    print(f"TOTAL:{'':>29}{total:>7.2f}")

    print("="*40)

except ValueError as e :
    print(e)

except TypeError as e :
    print(e)

except Exception as error :
    print('An error occured')
    print(error)


print('Application proceeds as if nothing happens')


