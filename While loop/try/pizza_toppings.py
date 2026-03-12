toppings = []

while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ")
    if topping.lower() == 'quit':
        break
    toppings.append(topping)
    print(f"Adding {topping} to your pizza.")
    print(f"Your pizza toppings are: "f"{', '.join(toppings)}")