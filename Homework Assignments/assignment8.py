# Assignement 8 Banton, Amirah
seperate = "--------------------------------------------------"

# 8-1 Message

def display_message():
    print("In this chapter I am learning about functions, arguments, and using lists and disctionaries in Python.")

display_message()

print(seperate)

# 8-2 Favorite Book

def favorite_book(title):
    print(f"One of my favorite books is {title}.")
    
book_title = input("Enter in your favorite book title:")
favorite_book(book_title)

print(seperate)

# 8-3 T-Shirt

def make_shirt(size, text):
    print(f"Making a {size} size shirt with the message saying {text}.")

size_pos = input("Enter your shirt size ex. Small, Medium, Large, Extra Large, XXL etc :")
text_pos = input("Enter in what you want the shirt message to be:")
make_shirt(size_pos,text_pos)

print(seperate)

# 8-4 Large Shirts (default)

def make_shirt_default(size='Large',message='I love Python'):
    print(f"Shirt size: {size} — Message: \"{message}\"")

make_shirt_default()

make_shirt_default(size='Medium')

size_custom = input("Enter a shirt size for a custom message: ")
message_custom = input("Enter the custom message: ")
make_shirt_default(size=size_custom, message=message_custom)

print(seperate)

# 8-5 Cities

def describe_city(city, country = 'United States'):
    print(f"{city.title()} is in {country.title()}.")

for i in range(1, 4):
        city_in = input(f"Please Enter a city #{i}: ")
# For at least one, allow user to press Enter to use default country
country_in = input(f"Enter country for {city_in} (press Enter for default '{'United States'}'): ")
if country_in.strip() == "":
        describe_city(city_in)
else:
        describe_city(city_in, country_in)

print(seperate)

# 8-6 City Names

def city_country(city, country):
    return f"{city.title()}, {country.title()}"

pairs = [
("santiago", "chile"),
("reykjavik", "iceland"),
("lagos", "nigeria")
]
print("8-6 City-country pairs:")
for c, co in pairs:
    print(city_country(c, co))

print(seperate)

# 8-7 Album

def make_album(artist, title, songs=None):
     album = {'artist': artist.title(), 'title': title.title()}
     if songs is not None:
          album['songs'] = songs
          return album

album1 = make_album('adele', '25')
album2 = make_album('pink floyd', 'the dark side of the moon')
album3 = make_album('the weeknd', 'after hours', songs=14)

print("8-7 Albums:")
print(album1)
print(album2)
print(album3)

print(seperate)

# 8-8 User Albums

print("8-8 Make albums (type 'q' at any prompt to quit):")
while True:
    artist = input("Enter artist name (or 'q' to quit): ")
    if artist.lower() == 'q':
        break
    title = input("Enter album title (or 'q' to quit): ")
    if title.lower() == 'q':
        break
    songs_in = input("Enter number of songs (or press Enter if unknown): ")
    if songs_in.strip().lower() == 'q':
        break
    songs_val = None
    if songs_in.strip() != '':
        try:
        songs_val = int(songs_in)
    except ValueError: print("Number of songs invalid, storing as unknown.")
        songs_val = None
    created = make_album(artist, title, songs=songs_val)
print("Created album dictionary:", created)
print("Exiting album creator.")

print(seperate)

# 8-8 Messages
def show_messages(messages):
    for message in messages:
        print(message)
def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

messages_list = ["Hello!", "How are you?", "Goodbye!"]
sent_list = []  
show_messages(messages_list[:])
send_messages(messages_list, sent_list)
print("Messages after sending:")
show_messages(messages_list)
print("Sent messages:")
show_messages(sent_list)

print(seperate)

# 8-10 Sending Messages
def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)
messages_list = ["Hello!", "How are you?", "Goodbye!"]
sent_list = []  
send_messages(messages_list[:], sent_list)
print("Messages after sending:")
for message in messages_list:
    print(message)
print("Sent messages:")
for message in sent_list:
    print(message)

print(seperate)

# 8-11 Archived Messages
def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)
messages_list = ["Hello!", "How are you?", "Goodbye!"]
sent_list = []  
send_messages(messages_list[:], sent_list)
print("Messages after sending:")
for message in messages_list:
    print(message)
print("Sent messages:")
for message in sent_list:
    print(message)

print(seperate)

# 8-12 Sandwiches
def make_sandwich(*ingredients):
    print("Making a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")
make_sandwich("turkey", "lettuce", "tomato")
make_sandwich("peanut butter", "jelly")
make_sandwich("ham", "cheese", "mustard", "pickles")

print(seperate)

# 8-13 User Profile
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first.title()
    profile['last_name'] = last.title()
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('amirah', 'banton', location='new york', field='computer science')
print("User Profile:")
for key, value in user_profile.items():
    print(f"{key}: {value}")

print(seperate)

# 8-14 Cars
def make_car(manufacturer, model, **options):
    car = {}
    car['manufacturer'] = manufacturer.title()
    car['model'] = model.title()
    for key, value in options.items():
        car[key] = value
    return car
car1 = make_car('subaru', 'outback', color='blue', tow_package=True)
car2 = make_car('tesla', 'model s', color='red', autopilot=True)
print("Car 1:")
for key, value in car1.items():
    print(f"{key}: {value}")
print("\nCar 2:")
for key, value in car2.items():
    print(f"{key}: {value}")

print(seperate)

# 8-15 Printing Models
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
unprinted = ['phone case', 'robot pendant', 'dodecahedron']
completed = []
print_models(unprinted[:], completed)
print("Unprinted designs after function call:")
for design in unprinted:
    print(design)
print("Completed models:")
for model in completed:
    print(model)

print(seperate)

# 8-16 Imports
# This would normally be in a separate file named pizza.py
def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
# In the main file
make_pizza(16, 'pepperoni', 'mushrooms', 'green peppers')
make_pizza(12, 'extra cheese')  

print(seperate)

# 8-17 Styling Functions
# This would normally be in a separate file named styling.py
def show_magicians(magicians):
    for magician in magicians:
        print(magician)
def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = "The Great " + magicians[i]
# In the main file
magician_names = ['alice', 'bob', 'carol']
print("Original magicians:")
show_magicians(magician_names)
great_magicians = magician_names[:]
make_great(great_magicians)
print("\nGreat magicians:")
show_magicians(great_magicians)
print("\nOriginal magicians after make_great call:")
show_magicians(magician_names)

print(seperate)