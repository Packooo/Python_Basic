##Loping through dictionary
favorites_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

for name, language in favorites_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

##lopping through all the keys in a dictionary
for name in favorites_languages:
    print(name.title())
#rather than writing code like this:
for name in favorites_languages.keys():
    print(name.title())

#another example
favorites_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

friends = ['phil', 'sarah']
for name in favorites_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorites_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
#User the key to find out the value associated with that key.
#checking if a person was polled
if 'erin' not in favorites_languages.keys():
    print("Erin, please take our poll!")


##Looping through dictionary key in a particular order
favorites_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

for name in sorted(favorites_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

##Lopping through all values in dictionary
favorites_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

print("The following languages have been mentioned:")
for language in favorites_languages.values():
    print(language.title())
#Unique values
print("The following languages have been mentioned (unique values):")
for language in set(favorites_languages.values()):
    print(language.title())
    