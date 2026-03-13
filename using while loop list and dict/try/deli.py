sandwitch_orders = []
finished_sandwitches = []

while True:
    order = input("Witch sandwitch would you like to order?('quit' to exit)")
    if order == 'quit':
        break
    else:
        sandwitch_orders.append(order)
        print(f"I made your {order} sandwitch!")
print("\nListing each sandwitch had been made: ")
for sandwitch in sandwitch_orders:
    print(sandwitch)