"""
Create a function called confirmName it takes in two parameter list_of_name and name_to_confirm which are of data type list and a string respectively.. the function confirms if the name_to_, confirm is in the list if so it returns the actual position of that name (not index position) otherwise it returns -1.
"""

def confirmName(list_of_name, name_to_confirm):
    if name_to_confirm in list_of_name:
        return list_of_name.index(name_to_confirm) + 1
    return -1


names = ["Alice", "Bob", "Charlie", "Diana"]

print(confirmName(names, "Charlie")) 
print(confirmName(names, "Bob"))      
print(confirmName(names, "Eve"))     
print(confirmName(names, "Alice"))    
