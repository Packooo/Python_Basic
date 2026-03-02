##Coppying a list
foods = ['pizza', 'falafel', 'carrot cake']
friends_food = foods[:]

print("My favorite foods are:")
print(foods)
print("\nMy friends favorite foods are:")
print(friends_food)

##add food
foods.append("cannoli")
friends_food.append("ice cream")

print("\nMy favorite foods are:")
print(foods)
print("\nMy friends favorite foods are:")
print(friends_food)

print("the first three item in the list are: ")
print(foods[:3])

print("Three item in the middle of the list are: ")
print("1:3")

print("the last three item in the list are: ")
print(foods[-3:])