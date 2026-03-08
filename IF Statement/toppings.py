requested_toppings = 'mushroom'

if requested_toppings != 'anchovies':
    print("Hold the anchovies!")

##Testing multiple conditions
requested_toppings = ['mushroom', 'extra cheese']

if 'mushroom' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinnished making your pizza")


##checking special item
requested_toppings = ['mushroom', 'green pepper', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green pepper':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinnished making your pizza")


##Checking list is not empty
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}")
    print("Finnished making your pizza")
else:
    print("Are you sure you want a plain pizza?")


##Using multiple lists
available_toppings = ['mushroom', 'olives', 'green pepper', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushroom', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_toppings}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinnished making your pizza")
