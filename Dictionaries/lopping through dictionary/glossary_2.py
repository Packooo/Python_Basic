glossary = {
    'variable': 'A named storage location in memory that holds a value.',
    'function': 'A block of reusable code that performs a specific task.',
    'loop': 'A control structure that repeatedly executes a block of code.',
    'list': 'An ordered collection of items that can be of different data types.',
    'dictionary': 'A collection of key-value pairs where each key is unique.'
}

for term, definition in glossary.items():
    print(f"{term.title()}: {definition}")
print("original glossary.")

#add more term in glossary
glossary['tuple'] = 'An immutable ordered collection of items.'
glossary['set'] = 'An unordered collection of unique items.'
glossary['conditional'] = 'A statement that performs different actions based on a condition.'
glossary['module'] = 'A file containing Python definitions and statements that can be imported and used in other programs.'
glossary['exception'] = 'An event that occurs during the execution of a program that disrupts the normal flow of instructions.'

for term, definition in glossary.items():
    print(f"{term.title()}: {definition}")