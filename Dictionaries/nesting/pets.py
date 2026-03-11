pets = {
    'cat': {
        'name': 'Mochi',
        'owner': 'Mitori',
        'age': 2,
    },

    'dog': {
        'name': 'Pochi',
        'owner': 'Sasi',
        'age': 3,
    },

    'bird': {
        'name': 'Pippo',
        'owner': 'Mita',
        'age': 1,
    },
}

for pet, info in pets.items():
    print(f"\nPet: {pet}")
    for key, value in info.items():
        print(f"\t{key}: {value}")