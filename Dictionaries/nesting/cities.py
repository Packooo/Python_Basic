cities = {
    'miyagi' : {
        'country': 'Japan',
        'population': 1000000,
        'fact': 'beautiful'
    },

    'solo' : {
        'country': 'Indonesia',
        'population': 1000000,
        'fact': 'have tembok ratapan solo'
    },

    'tokyo' : {
        'country': 'Japan',
        'population': 1000000,
        'fact': 'have beautiful temple'
    }
}

for city, city_info in cities.items():
    print(f"\nCity: {city.title()}")
    print(f"Country: {city_info['country']}")
    print(f"Population: {city_info['population']}")
    print(f"Fact: {city_info['fact'].title()}")