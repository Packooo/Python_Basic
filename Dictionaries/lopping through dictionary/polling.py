favorites_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

peoples = ['jen', 'phil', 'edward', 'james']

for people in peoples:
    if people in favorites_languages.keys():
        print(f"{people}, thank you for taking the poll")
    else:
        print(f"{people}, you should take the poll")