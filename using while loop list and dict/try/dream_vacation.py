prompt = "if you could visit one place in the world, where would you go?"
places = []
while True:
    place = input(prompt)
    print("type 'quit' to exit")
    if place == 'quit':
        break
    else:
        places.append(place)
print("Results:")
for place in places:
    print(place)