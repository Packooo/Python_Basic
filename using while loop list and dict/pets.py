##remove all instances of a value from a list

pet = ['cat', 'dog', 'cat', 'goldfish', 'cat', 'rabbit', 'cat']

print(pet)


while 'cat' in pet:
    pet.remove('cat')

print(pet)