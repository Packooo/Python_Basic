players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("here is the first three players on my team:")
print(players[:3])

print("here are the middle three players on my team:")
print(players[1:4])

print("here are the last three players on my team:")
print(players[-3:])


##looping through a slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

