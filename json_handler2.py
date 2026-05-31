import json 
import os 
STORAGE_PATH = 'C:/Users/CHIDI/OneDrive/Desktop/Pythonfolder/customers.json'

if os.path.exists(STORAGE_PATH) :
    reader = open(STORAGE_PATH,'r')
    customers = json.load(reader)
    print(type(customers))
    print(customers[0])
    reader.close()
else :
    print('file path does not exist!')


customer1 =  {
        "name": "Peter",
        "phone": "234-0103",
        "email": "peter@example.com",
        "balance": 200.0
    }

def addDataToCustomers():
    # load the previous data 
    former_data = open(STORAGE_PATH,'r')
    customers : list = json.load(former_data)
    former_data.close()
    # now after converting the json data stored to a native data
    # we can now reopen for writing sake 
    with open(STORAGE_PATH,'w') as fp :
        customers.append(customer1)
        # after appending the customer to the list of all custoomers we can now dump the full list of customer back to the json storage facility
        json.dump(customers,fp)
        print('stored successfully')    
    
addDataToCustomers()
# reader = open(STORAGE_PATH,'r')
# data = reader.read()
# print(data)
# print(type(data))
# print(data[0])
# reader.close()

# # converting to native data 
# data = json.loads(data)
# print(data)
# print(type(data))
# print(data[0])