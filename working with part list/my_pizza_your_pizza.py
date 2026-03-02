pizzas = ["pepperoni", "cheese", "veggie"]
friend_pizzas = pizzas[:]

##add new pizza to original list
pizzas.append("burger")
friend_pizzas.append("egg")

print("original pizza list are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)