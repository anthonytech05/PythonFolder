import json 


prices = ['34','56','78']
print(prices)
print(type(prices))
print(prices[1])
print("+"*15)
# json : serialize / deserilize 

prices_stringified = json.dumps(prices)
print(prices_stringified)
print(prices_stringified[1])
print(type(prices_stringified))


# deserialize 
data = """
    [34,67,45,34,23]
"""
print(type(data))
print(data)
print("="*10)
native_data = json.loads(data)
print(type(native_data))
print(native_data)
