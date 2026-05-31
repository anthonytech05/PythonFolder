# Practical — Inventory Manager (inventory.py)
# ================================================
# FUEL STATION INVENTORY MANAGER — Module 4
# ================================================

inventory = {
    "PMS": {"price": 617.0, "stock": 50000, "unit": "litres"},
    "AGO": {"price": 980.0, "stock": 30000, "unit": "litres"},
    "LPG": {"price": 450.0, "stock": 5000, "unit": "kg"},
}


def show_inventory():
    print("\n" + "=" * 65)
    print(f"{'PRODUCT':<10} {'PRICE':>10} {'STOCK':>15} {'VALUE':>15}")
    print("-" * 65)

    for code, info in inventory.items():
        value = info["price"] * info["stock"]

        print(
            f"{code:<10} "
            f"N{info['price']:>9,.2f} "
            f"{info['stock']:>8,} {info['unit']:<7} "
            f"N{value:>12,.0f}"
        )

    print("=" * 65)


def add_stock(product_code, amount):
    if product_code in inventory:
        inventory[product_code]["stock"] += amount
        print(f"Added {amount:,} units to {product_code}.")
    else:
        print(f"Product {product_code} not found.")


def sell_fuel(product_code, amount):
    if product_code not in inventory:
        print("Product not found.")
        return

    if amount > inventory[product_code]["stock"]:
        print("Insufficient stock!")
        return

    inventory[product_code]["stock"] -= amount

    revenue = inventory[product_code]["price"] * amount

    print(f"Sold {amount:,} units. Revenue: N{revenue:,.2f}")


# LOW STOCK ALERT FUNCTION
def low_stock_alert():
    print("\nLOW STOCK ALERTS")

    low_stock_found = False

    for code, info in inventory.items():
        if info["stock"] < 5000:
            print(
                f"WARNING: {code} stock is low "
                f"({info['stock']:,} {info['unit']})"
            )
            low_stock_found = True

    if not low_stock_found:
        print("All products have sufficient stock.")


# TOTAL INVENTORY VALUE FUNCTION
def total_value():
    total = 0

    for info in inventory.values():
        total += info["price"] * info["stock"]

    return total


# ADD NEW PRODUCT FROM COMMAND LINE
def add_new_product():
    print("\nADD NEW PRODUCT")

    code = input("Enter product code: ").upper()
    price = float(input("Enter product price: "))
    stock = int(input("Enter product stock: "))
    unit = input("Enter unit (litres/kg): ")

    inventory[code] = {
        "price": price,
        "stock": stock,
        "unit": unit
    }

    print(f"{code} added successfully!")


# ======================
# DEMO
# ======================

show_inventory()

sell_fuel("PMS", 200)

add_stock("AGO", 10000)

low_stock_alert()

print(f"\nTotal Inventory Value: N{total_value():,.2f}")

add_new_product()

show_inventory()