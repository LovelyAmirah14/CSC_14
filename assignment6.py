# Assignment 6 Banton, Amirah
seperate = "--------------------------------------------------"

# 6-1 Person
person = {
    "first_name": "Amirah",
    "last_name": "Banton",
    "age": 17,
    "city": "Reading",
}   
print(person["first_name"])
print(person["last_name"])
print(person["age"])
print(person["city"])

print(seperate)

# 6-2 Favorite Numbers
favorite_numbers = {
    "Amirah": 14,
    "Sariah": 6,
    "Nyah": 7,
    "Emma": 23,
    "Keya": 7
}

print(f"Amirah's favorite number is {favorite_numbers['Amirah']}.")
print(f"Sariah's favorite number is {favorite_numbers['Sariah']}.")
print(f"Nyah's favorite number is {favorite_numbers['Nyah']}.")
print(f"Emma's favorite number is {favorite_numbers['Emma']}.")
print(f"Keya's favorite number is {favorite_numbers['Keya']}.")

print(seperate)

# 6-3 Glossary
glossary = {
    "string": "A sequence of characters.",
    "integer": "A whole number, positive or negative, without decimals.",
    "float": "A number that has a decimal point.",
    "list": "A collection of items in a particular order.",
    "dictionary": "A collection of key-value pairs.",
}

print(f"String: {glossary['string']}")
print(f"Integer: {glossary['integer']}")
print(f"Float: {glossary['float']}")
print(f"List: {glossary['list']}")
print(f"Dictionary: {glossary['dictionary']}")

print(seperate)

# 6-4 Glossary 2
for term, definition in glossary.items():
    print(f"{term.capitalize()}: {definition}")

print(seperate)

# 6-5 Rivers
rivers = {
    "nile": "egypt",
    "amazon": "brazil",
    "mississippi": "united states",
}   
for river, country in rivers.items():
    print(f"The {river.capitalize()} runs through {country.title()}.")

print(seperate)

print("The rivers in the dictionary are:")
for river in rivers.keys():
    print(river.capitalize())

print(seperate)

print("The countries in the dictionary are:")
for country in rivers.values():
    print(country.title())  

print(seperate)

# 6-6 Polling
favorite_languages = {
    "Sariah": "python",
    "Emma": "c",
    "Nyah": "ruby",
    "phil": "python",
}
people_to_poll = ["Keya", "sarah", "Nyah", "phil", "linda", "Sariah"]
for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you for taking the poll, {person.title()}!")
    else:
        print(f"Please take our poll, {person.title()}.")

print(seperate)

# 6-7 People
people = [
    {
        "first_name": "Amirah",
        "last_name": "Banton",
        "age": 17,
        "city": "Reading",
    },
    {
        "first_name": "Sariah",
        "last_name": "Smith",
        "age": 18,
        "city": "New York",
    },
    {
        "first_name": "Nyah",
        "last_name": "Johnson",
        "age": 19,
        "city": "Newark",
    },
]
for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    age = person['age']
    city = person['city']
    print(f"{full_name}, Age: {age}, City: {city}")

print(seperate)

# 6-8 Pets
pets = [
    {
        "type": "dog",
        "name": "Kobe",
        "owner": "Amirah",
    },
    {
        "type": "cat",
        "name": "Chi Chi",
        "owner": "Sariah",
    },
    {
        "type": "cat",
        "name": "Theo",
        "owner": "Nyah",
    },
]
for pet in pets:
    pet_type = pet['type']
    name = pet['name']
    owner = pet['owner']
    print(f"{name} is a {pet_type} owned by {owner}.")

print(seperate)

# 6-9 Favorite Places
favorite_places = {
    "Amirah": ["Paris", "Tokyo", "London"], 
    "Sariah": ["Dominican Republic", "Japan", "Disney World"],
    "Emma": ["Hawaii", "Saint Thomas", "Belize", "Honduras"],
}
for person, places in favorite_places.items():
    places_formatted = ', '.join(place.title() for place in places)
    print(f"{person}'s favorite places are: {places_formatted}.")

print(seperate)

# 6-10 Favorite Numbers
favorite_numbers = {
    "Amirah": [14, 7, 3],
    "Sariah": [6, 9],
    "Nyah": [7, 11, 13],
}
for person, numbers in favorite_numbers.items():
    numbers_formatted = ', '.join(str(number) for number in numbers)
    print(f"{person}'s favorite numbers are: {numbers_formatted}.")

print(seperate)

# 6-11 Cities
cities = {
    "paris": {
        "country": "france",
        "population": "2.1 million",
        "fact": "Known as the City of Light.",
    },
    "tokyo": {
        "country": "japan",
        "population": "14 million",
        "fact": "Famous for its cherry blossoms.",
    },
    "london": {
        "country": "england",
        "population": "9 million",
        "fact": "Home to the historic Tower of London.",
    },
}
for city, info in cities.items():
    country = info['country'].title()
    population = info['population']
    fact = info['fact']
    print(f"{city.title()} is in {country}. It has a population of {population} and is {fact}")

print(seperate)

# 6-12 Extensions
# I have already done extensions in previous exercises such as using lists as values in dictionaries (6-9 and 6-10) and nesting dictionaries (6-11).
# These exercises demonstrate my understanding of more complex data structures in Python.
# Therefore, I consider these exercises as my extensions for this assignment.
print("Extensions have been demonstrated in exercises 6-9, 6-10, and 6-11.")

print(seperate)

# End of assignment 6

