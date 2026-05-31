"""
create an empty list cart = []
Allow the user to add items (name + price) as dictionaries to the cart.
show the cart contents in a formatted table.
Calcualte and show the total price.
Allow the user to remove an item by name.
"""

cart = []


def add_item(name, price):
    cart.append({"name": name, "price": price})
    print(f'"{name}" added to cart.')


def remove_item(name):
    for item in cart:
        if item["name"].lower() == name.lower():
            cart.remove(item)
            print(f'"{name}" removed from cart.')
            return
    print(f'"{name}" not found in cart.')


def show_cart():
    if not cart:
        print("Your cart is empty.")
        return
    print(f"\n{'Item':<20} {'Price':>10}")
    print("-" * 32)
    for item in cart:
        print(f"{item['name']:<20} ${item['price']:>9.2f}")
    print("-" * 32)
    total = sum(item["price"] for item in cart)
    print(f"{'Total':<20} ${total:>9.2f}\n")


def main():
    while True:
        print("\n1. Add item\n2. Remove item\n3. View cart\n4. Quit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = input("Item name: ").strip()
            try:
                price = float(input("Item price: $").strip())
                add_item(name, price)
            except ValueError:
                print("Invalid price. Please enter a number.")
        elif choice == "2":
            name = input("Item name to remove: ").strip()
            remove_item(name)
        elif choice == "3":
            show_cart()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-4.")


main()
