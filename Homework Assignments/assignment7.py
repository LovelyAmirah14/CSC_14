# Assignment 7 Banton, Amirah
seperate = "--------------------------------------------------"

# 7-1 Rental Car
rental_car = input("What kind of rental car would you like? ")
print(f"Let me see if I can find you a {rental_car}.")

print(seperate)

# 7-2 Restaurant Seating
party_size = int(input("How many people are in your dinner group? "))
if party_size > 8:
    print("You'll have to wait for a table.")
else:
    print("Your table is ready.")

print(seperate)

# 7-3 Multiples of Ten
number = int(input("Enter a number: "))
if number % 10 == 0:
    print(f"{number} is a multiple of ten.")
else:
    print(f"{number} is not a multiple of ten.")

print(seperate)

# 7-4 Pizza Toppings
topping = input("Enter a pizza topping you want: ")
print(f"Adding {topping} to your pizza.")
if topping.lower() != "anchovies":
    print("Adding extra cheese to your pizza.")
print("Your pizza is ready!")

print(seperate)

# 7-5 Movie Tickets
age = int(input("Enter your age: "))
if age < 3:
    price = 0
elif age <= 12:
    price = 10
else:
    price = 15
print(f"Your movie ticket price is ${price}.")

print(seperate)

# 7-6 Three Exits
while True:
    prompt = input("Enter a message (type 'quit' to exit): ")
    if prompt.lower() == 'quit':
        break
    print(f"You entered: {prompt}")
print("You have exited the program.")

print(seperate)

# 7-7 Infinity
while True:
    prompt = input("Enter a message (type 'exit' to stop): ")
    if prompt.lower() == 'exit':
        print("You have exited the program.")
        break
    print(f"You entered: {prompt}")

print(seperate)

# 7-8 Deli
sandwich_orders = ["turkey", "ham", "roast beef", "veggie", "tuna"]
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"Making your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)
print("All sandwiches are made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")

print(seperate)

# 7-9 No Pastrami
sandwich_orders = [
    "turkey", "pastrami", "ham", "pastrami", "roast beef", "pastrami", "veggie"
]
finished_sandwiches = []
print("Sorry, we're out of pastrami.")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"Making your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)
print("All sandwiches are made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")

print(seperate)

# 7-10 Dream Vacation
responses = {}
polling_active = True
while polling_active:
    name = input("What is your name? ")
    vacation = input("If you could visit one place in the world, where would you go? ")
    responses[name] = vacation
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() != 'yes':
        polling_active = False
print("\n--- Poll Results ---")
for name, vacation in responses.items():
    print(f"{name} would like to visit {vacation}.")

print(seperate)

# End of Assignment 7