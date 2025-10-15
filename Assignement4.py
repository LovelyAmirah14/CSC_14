# Assignment 3 Banton, Amirah
seperate = "--------------------------------------------------"

# 4-1 Pizzas
pizzas = ["Pepperoni", "Hawaiian", "Cheese", "Veggie"]
for pizza in pizzas:
    print("I like " + pizza + " pizza.")
print("I really love pizza!")

print(seperate)

# 4-2 Animals
animals = ["Dog", "Cat", "Rabbit"]
for animal in animals:
    print("A " + animal + " would make a great pet.")
print("Any of these animals would make a great pet!")

print(seperate)

# 4-3 Counting to Twenty
for value in range(1, 21):
    print(value)

print(seperate)

# 4-4 One Million
# for value in range(1, 1000001):
#     print(value)
# I commented this out because it will print 1-1,000,000 and it will take a while to load

print(seperate)

# 4-5 Summing a Million
million = list(range(1, 1000001))
print(min(million))
print(max(million))
print(sum(million))
# this is printing the minimum, maximum, and sum of the list

print(seperate)

# 4-6 Odd Numbers
for value in range(1, 21, 2):
    print(value)
# this is printing odd numbers from 1-20

print(seperate)

# 4-7 Threes
for value in range(3, 31, 3):
    print(value)
# this is printing the multiples of 3 from 3-30

print(seperate)

# 4-8 Cubes
cubes = []
for value in range(1, 11):
    cubes.append(value**3)
print(cubes)
# this is printing the cubes of numbers from 1-10

print(seperate)

# 4-9 Cube Comprehension
cubes = [value**3 for value in range(1, 11)]
print(cubes)
# this is printing the cubes of numbers from 1-10 using list comprehension

print(seperate)

# 4-10 Slices
players = ["Liv", "Tram", "Bri", "Rene", "Nashiyah"]
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
print("Here are the middle three players on my team:")
for player in players[1:4]:
    print(player.title())
print("Here are the last three players on my team:")
for player in players[-3:]:
    print(player.title())
# this is printing the first three, middle three, and last three players on my team

print(seperate)

# 4-11 My Pizzas, Your Pizzas
my_pizzas = ["Pepperoni", "Hawaiian", "Cheese", "Veggie"]
friend_pizzas = my_pizzas[:] # making a copy of my_pizzas
my_pizzas.append("BBQ Chicken") # adding a new pizza to my_pizzas
friend_pizzas.append("Meat Lovers") # adding a new pizza to friend_pizzas
print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
# this is printing my favorite pizzas and my friend's favorite pizzas

print(seperate)

# 4-12 More Loops
for pizza in my_pizzas:
    print("I like " + pizza + " pizza.")
print("I really love pizza!")
for pizza in friend_pizzas:
    print("My friend likes " + pizza + " pizza.")
print("My friend really loves pizza too!")
# this is printing my favorite pizzas and my friend's favorite pizzas with a message    

print(seperate)

# 4-13 Buffet
buffet = ("Italian", "Chinese", "Mexican", "American", "Japanese")
print("Original buffet menu:")
for food in buffet:
    print(food)
# this is printing the original buffet menu

# buffet[0] = "Indian" # this will give an error because tuples are immutable
# buffet[1] = "Thai"
# buffet[2] = "Korean"
# buffet[3] = "Vietnamese"
# buffet[4] = "French"
# the above lines will give an error because tuples are immutable
print("\nUpdated buffet menu:")
for food in buffet:
    print(food)
# this is printing the updated buffet menu (same as original because tuples are immutable)
# I commented out the lines that will give an error because tuples are immutable
# I can't change the tuple but I can print it again to show that it is the same

print(seperate)

# End of Assignment 4


