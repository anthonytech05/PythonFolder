facebook_user1  = {
    "username": "james34",
    "age" : 24,
    "email" : "james34@gmail.com"
}


# CRUD
print(facebook_user1)
print(type(facebook_user1))

# READ 
user_name = facebook_user1["username"]
user_age = facebook_user1.get('age',46)
print(f'Username : {user_name}\nAge : {user_age}')

# update 
facebook_user1["age"] += 20
facebook_user1.update(username='jamie_4', address ='23 Arubayi Street airport Rd')
print(f'After updating facebook user 1')
print(facebook_user1)


# dELETE
# facebook_user1.clear()
# del(facebook_user1['age'])
print(facebook_user1)

# REFERENCED DATA TYPE 
fbk1 = facebook_user1.copy() 
fbk1.clear()
print(fbk1)
print(facebook_user1)


# looping
for key in facebook_user1 : 
    print(key)
    print(facebook_user1.get(key))
    print("---------------\n")