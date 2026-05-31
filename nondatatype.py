prices = []
print(prices)
prices.append(15)
prices.append(20)
prices.append(5)
print(prices)

prices.extend([45.67,34.2,32.98])

try :
    # removing by value 
    prices.remove(200)
except ValueError as ve :
    print(f'ERROR : {ve}')

prices.pop(1)
print(prices)

# prices.clear()
# print(prices)


# del(prices)
# print(prices)


prices.insert(0,200)
print(prices)

# read 
price1 = prices[0]
print(f'First price ${price1}')

position = prices.index(34.2)
print(f'Position {position}')


# know how to loop 
for value in prices :
    print(value)


names = ['john','andy','john','peter','rita','anita','john','peter']

def replaceNameOccurrence(list_to_search_from : list , name_to_search : str, name_to_replace_with : str ) -> list :
    new_list = []
    for name in list_to_search_from : 
        if name == name_to_search :
            new_list.append(name_to_replace_with)
        else :
            new_list.append(name)
    return new_list

new_names = replaceNameOccurrence(names, 'john','bayo')
print(new_names)
new_names = replaceNameOccurrence(names, 'peter','drogba')
print(new_names)