##deli has run out of pastrami

sandwitch_orders = []
finished_sandwitches = []

print("The deli has run out of pastrami")

while True:
    order = input("Witch sandwitch would you like to order?('quit' to exit)")
    if order == 'quit':
        break
    else:
        sandwitch_orders.append(order)
        print(f"I made your {order} sandwitch!")

print("\nListing each sandwitch had been made: ")
for sandwitch in sandwitch_orders:
    if sandwitch == 'pastrami':
        sandwitch_orders.remove('pastrami')
    
for sandwitch in sandwitch_orders:
    print(sandwitch)