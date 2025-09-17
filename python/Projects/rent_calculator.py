rent =int(input("\nEnter your flat rent: "))
food = int(input("Enter total amount of food ordered: "))
electricity_spend =int(input("Enter the total of electricity spend: "))
charge_per_unit =int(input("Enter the charge per unit: "))
persons =int(input("Total number of pergitsons in flat: "))

current_bill = electricity_spend * charge_per_unit
output = (rent + food + current_bill) // persons

print ("\nEach person will pay: " , output)
 