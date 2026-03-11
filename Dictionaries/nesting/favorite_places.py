favorite_places = {    
    'Mitori': ['Tokyo', 'Kyoto', 'Osaka'],
    'Sasi': ['Hokkaido', 'Hiroshima', 'Fukuoka'],
    'Mita': ['Aomori', 'Nagoya', 'Kanagawa'],
}

for name, places in favorite_places.items():
    print(f"\n{name}'s favorite places are: ")
    for place in places:
        print(f"\t{place}")
