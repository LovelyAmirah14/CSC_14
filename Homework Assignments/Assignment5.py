# Assignment 5 Banton, Amirah
seperate = "--------------------------------------------------"

# 5-1 Conditional Tests
bed = "queen"
print("Is the bed == 'Queen'? I predict it to be true.")
print(bed == "Queen") #false 1
print("Oh maybe I spelled it wrong, for some reason it's lowercase?")
print(bed == "queen") #true 1
print("Is the bed == 'king'? I predict it to not be true.")
print(bed == "king") # false 2
print("Is the bed != 'king'? I predict it to be true.")
print(bed != "king") # true 2
print("Possibly it changed to == 'twin'? I predict it to be true possibly.")
print(bed == "twin") # false 3

print(seperate)

# 5-2 More Conditional Tests
food = "Cupcake"
print("Is the food == 'cake'? I predict it to be true.")
print(food == "cake") # false 4
print("I wonder if it's a type of cake, maybe like a cupcake?")
print(food == "Cupcake") # true 4
print("Yep, its a cupcake!!")

car = "Audi"
print("Is the car == 'ferrari'? I really hope so it would be super dope.")
print(car == "ferrari") # false 5
print("Hmm, maybe it's a different type of car like an Audi?")
print(car == "Audi") # true 5
print("Yesss it's an Audi!")    

print(seperate)

# 5-3 Alien Colors #1
alien_color = "green"
if alien_color == "green":
    print("You just earned 5 points!") 
if alien_color != "green":
    print("You just earned 10 points!")

print(seperate)

# 5-4 Alien Colors #2
alien_color = "yellow"
if alien_color == "green":
    print("You just earned 5 points!")
if alien_color != "green":
    print("You just earned 10 points!")

print(seperate)

# 5-5 Alien Colors #3
alien_color = "red"
if alien_color == "green":
    print("You just earned 5 points!")
elif alien_color == "yellow":
    print("You just earned 10 points!")
elif alien_color == "red":
    print("You just earned 15 points!")

print(seperate)

# 5-6 Stages of Life
age = 18
if age < 2:
    print("The person is a wee little baby.")
elif age >= 2 and age < 4:
    print("That child is in their terrible toddler years.")
elif age >= 4 and age < 13:
    print(" They are a fun lovely kid.")
elif age >= 13 and age < 20:
    print("They are basically a teen and semi adult.")
elif age >= 20 and age < 65:
    print("They are a full grown adult.")
elif age >= 65:
    print("They are an elderly person.")
print(f"The person is {age} years old.")


print(seperate)

# 5-7 Favorite Fruit
favorite_fruits = ["mango", "banana", "strawberry"]
if "blueberry" in favorite_fruits:
    print(" I don't know why that was there I don't like blueberries.")
if "mango" in favorite_fruits:
    print("Mangoes especially dried are super good and one of my favorite.")
if "banana" in favorite_fruits:
    print("Bananas are great in smoothies and as a snack.")
if "kiwi" in favorite_fruits:
    print("Kiwis are ok I guess but not my favorite.")
if "strawberry" in favorite_fruits:
    print("Strawberries are delicious especially with nutella and a crepe.")

print(seperate)

# 5-8 Hello Admin
usernames = ["admin", "user1", "user2", "user3", "user4"]
for username in usernames:
    if username == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")

print(seperate)

# 5-9 No Users
usernames = []
if usernames:
    for username in usernames:
        print(f"Hello {username}, thank you for logging in again.")
else:
    print("We need to find some users!")

print(seperate)

# 5-10 Checking Usernames
current_users = ["user1", "user2", "user3", "user4", "user5"]
new_users = ["User1", "user6", "user7", "user2", "user8"]
for new_user in new_users:
    if new_user.lower() in [user.lower() for user in current_users]:
        print(f"Sorry {new_user}, that username is already taken. Please enter a new username.")
    else:
        print(f"Great, {new_user} is still available.")

print(seperate)

# 5-11 Ordinal Numbers
numbers = list(range(1,10))
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")

print(seperate)

# End of Assignment 5