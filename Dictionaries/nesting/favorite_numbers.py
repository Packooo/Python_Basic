people_0 = {
    'first_name': 'Mitori',
    'last_name': 'Yukimoto',
    'age': 25,
    'city': 'Miyagi',
    'favorite_numbers': [1, 2, 3, 4, 5]
}

people_1 = {
    'first_name': 'Makoto',
    'last_name': 'Yukimoto',
    'age': 23,
    'city': 'Kanto',
    'favorite_numbers': [1, 2, 3, 4, 5]
}

people_2 = {
    'first_name': 'Chika',
    'last_name': 'Yukimoto',
    'age': 21,
    'city': 'Tochigi',
    'favorite_numbers': [1, 2, 3, 4, 5]
}

peoples = [people_0, people_1, people_2]

for people in peoples:
    full_name = f"{people['first_name']} {people['last_name']}"
    print(f"\nFull Name: {full_name.title()} has favorite numbers: {people['favorite_numbers']}")