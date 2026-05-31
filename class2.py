well_name = "EK-07"
date = "2026-05-04"
shut_in_pressure = "1450"
flowing_tubing_pressure = "892.5"
choke_size = "32"
well_flowing = "True"
oil_sample_taken = "0"


shut_in_pressure = int(shut_in_pressure)
flowing_tubing_pressure = float(flowing_tubing_pressure)
choke_size = int(choke_size)

well_flowing = well_flowing == "True"   
oil_sample_taken = oil_sample_taken == "1"  

print(type(well_name), well_name)
print(type(date), date)
print(type(shut_in_pressure), shut_in_pressure)
print(type(flowing_tubing_pressure), flowing_tubing_pressure)
print(type(choke_size), choke_size)
print(type(well_flowing), well_flowing)
print(type(oil_sample_taken), oil_sample_taken)



# user input
company_name = input('what is the name of your company :')
net_profit = input('How much do you guys generate yearly :')
period_of_existence = input('For how long have your company been operational :')

total_amount_generated = float(net_profit) * float(period_of_existence)
print('Company name is '+ company_name + 'with a yearly net profit of $' + net_profit)
print(total_amount_generated)
