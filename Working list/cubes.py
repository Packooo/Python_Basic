cubes = []
for cube in range(1,11):
    cubes.append(cube**3)
print(cubes)

#or

cubes = [cube**3 for cube in range(1,11)]
print(cubes)