"""
Design a product class with: id, name, category, price, quantity.
Build a catalog class that manages a list of products.
Implement add_product(), remove_by_id(), search(name), update_price(id,price)
Bonus: add a low_stock_report() that shows all products with quantity < 10
"""


class Product:
    def __init__(self, id, name, category, price, quantity):
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"Product(id={self.id}, name='{self.name}', category='{self.category}', price={self.price}, quantity={self.quantity})"


class Catalog:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_by_id(self, id):
        self.products = [p for p in self.products if p.id != id]

    def search(self, name):
        return [p for p in self.products if name.lower() in p.name.lower()]

    def update_price(self, id, price):
        for p in self.products:
            if p.id == id:
                p.price = price
                return
        raise ValueError(f"No product with id {id}")

    def low_stock_report(self):
        return [p for p in self.products if p.quantity < 10]


# --- Demo ---
if __name__ == "__main__":
    catalog = Catalog()
    catalog.add_product(Product(1, "Laptop", "Electronics", 999.99, 15))
    catalog.add_product(Product(2, "USB Cable", "Accessories", 9.99, 3))
    catalog.add_product(Product(3, "Wireless Mouse", "Electronics", 29.99, 8))
    catalog.add_product(Product(4, "Desk Lamp", "Office", 24.99, 50))

    print("All products:")
    for p in catalog.products:
        print(" ", p)

    print("\nSearch 'wireless':")
    for p in catalog.search("wireless"):
        print(" ", p)

    catalog.update_price(1, 899.99)
    print("\nAfter price update on Laptop:")
    print(" ", catalog.search("Laptop")[0])

    catalog.remove_by_id(4)
    print("\nAfter removing Desk Lamp:")
    for p in catalog.products:
        print(" ", p)

    print("\nLow stock report (quantity < 10):")
    for p in catalog.low_stock_report():
        print(" ", p)
