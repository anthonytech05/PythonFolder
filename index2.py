total_number_of_people = 2345
price_of_bag = 23.58
is_present = False 
empty = None 

# sentence1 = total_number_of_people + " people are ready to buy our bag at rate of $ " + price_of_bag
sentence1 = f'{total_number_of_people} people are ready to buy our bag at rate of ${price_of_bag}'
print(sentence1)

# formatting of numbers for readability purpose 
balance = 560450
population = 354647854859489

# 45,305  4500.50, 
print(f"Balance : NGN{balance:,.2f}")
print(f"Tnad Population : {population:,}")







print(type(total_number_of_people))
print(type(price_of_bag))
print(type(is_present))
print(type(empty))

