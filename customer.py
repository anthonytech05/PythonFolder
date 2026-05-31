"""
Add a top_up(phone, amount) method to CustomerRegistry that increases a customer's
balance.
Add a delete(phone) method that removes a customer from the list and saves.
Print the total combined balance of all customers.
"""

import os
import json

DATA_FILE = "customers.json"


class Customer:
    def __init__(self, name, phone, email, balance=0):
        self.name = name
        self.phone = phone
        self.email = email
        self.balance = balance

    def to_dict(self):
        """Convert object to dictionary for JSON storage."""
        return {"name": self.name, "phone": self.phone,
                "email": self.email, "balance": self.balance}

    @classmethod
    def from_dict(cls, data):
        """Create a Customer from a dictionary."""
        return cls(data["name"], data["phone"],
                   data["email"], data.get("balance", 0))


class CustomerRegistry:
    def __init__(self):
        self.customers = self._load()

    def _load(self):
        if not os.path.exists(DATA_FILE):
            return []
        with open(DATA_FILE) as f:
            return [Customer.from_dict(d) for d in json.load(f)]

    def save(self):
        with open(DATA_FILE, "w") as f:
            json.dump([c.to_dict() for c in self.customers], f, indent=4)
        print("Registry saved.")

    def add(self, customer):
        self.customers.append(customer)
        self.save()
        print(f"Added: {customer.name}")

    def find(self, phone):
        return next((c for c in self.customers if c.phone == phone), None)

    def list_all(self):
        print(f"\n  {'NAME':<20} {'PHONE':<15} {'BALANCE':>12}")
        print("  " + "-" * 50)
        for c in self.customers:
            print(f"  {c.name:<20} {c.phone:<15} {c.balance:>12.2f}")
        print()

    def top_up(self, phone, amount):
        customer = self.find(phone)
        if customer is None:
            print(f"Customer with phone {phone} not found.")
            return
        customer.balance += amount
        self.save()
        print(f"Topped up {customer.name}'s balance by {amount:.2f}. New balance: {customer.balance:.2f}")

    def delete(self, phone):
        customer = self.find(phone)
        if customer is None:
            print(f"Customer with phone {phone} not found.")
            return
        self.customers.remove(customer)
        self.save()
        print(f"Deleted: {customer.name}")

    def total_balance(self):
        return sum(c.balance for c in self.customers)


if __name__ == "__main__":
    registry = CustomerRegistry()

    registry.add(Customer("Alice Smith", "555-0101", "alice@example.com", 100.00))
    registry.add(Customer("Bob Jones",  "555-0102", "bob@example.com",   250.00))
    registry.add(Customer("Carol White","555-0103", "carol@example.com",  50.00))

    registry.list_all()

    registry.top_up("555-0101", 75.00)
    registry.top_up("555-9999", 10.00)

    registry.delete("555-0102")
    registry.delete("555-8888")

    registry.list_all()

    print(f"Total combined balance: {registry.total_balance():.2f}")
