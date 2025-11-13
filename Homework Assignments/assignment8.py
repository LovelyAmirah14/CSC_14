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