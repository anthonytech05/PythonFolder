def add(a,b):
    return a + b

def subtracts(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        print('Error cannot divide by zero')
        return None
    
def modulo(a,b):
    return a % b

def power(a,b):
    return a ** b

history = []

while True:
    print("\n==== MINI CALCULATOR ====")
    print('[1] Add')
    print('[2] Subtract')
    print('[3] Multiply')
    print('[4] Divide')
    print('[5] Modulo')
    print('[6] Power')
    print('[7] Exit')

    choice = input('Choose an option: ')

    if choice == '7':
        print('Goodbye')
        break

    if choice in ["1", "2", "3", "4", "5", "6"]:
        num1 = float(input('Enter first nummber: '))
        num2 = float(input('Enter second number: '))

        result = None
        operation = ""

        if choice == '1':
            result = add(num1, num2)
            operation = "+"

        elif choice == '2':
            result = subtracts(num1, num2)
            operation = "-"

        elif choice == '3':
            result = multiply(num1, num2)
            operation = "*"

        elif choice == '4':
            result = divide(num1, num2)
            operation = "/"

        elif choice == '5':
            result = modulo(num1, num2)
            operation = "%"

        elif choice == '6':
            result = power(num1, num2)
            operation = "**"

        if result is not None:
            calculation = f"{num1} {operation} {num2} = {result}"
            print('Result:', result)

            history.append(calculation)

            if len(history) > 5:
                history.pop(0)

            print("\n----- Last 5 Calculations -----")
            for item in history:
                print(item)

        else:
            print('Invalid optional! Please choose from 1 to 7.')