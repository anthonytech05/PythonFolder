"""
Task: Fruit Inventory
Create a Python dictionary with:
1. Fruit names as keys
2. Quantities as values
Do this:
- Add 3 fruits with quantities
- Print the dictionary
- Change one fruit's quantity
- Print the updated dictionary

Start with:
inventory = {}
Example output:
{'apples': 5, 'bananas': 10, 'oranges': 7}
{'apples': 5, 'bananas': 20, 'oranges': 7}
"""

inventory = {}

inventory['apples'] = 5
inventory['bananas'] = 10
inventory['oranges'] = 7

print(inventory)

inventory['bananas'] = 30

print(inventory)
