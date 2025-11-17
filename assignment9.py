# Assignment 9 Banton, Amirah
seperate = "--------------------------------------------------"

# 9-1 Restaurant
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant is called {self.restaurant_name} and it serves {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

# Creating an instance
restaurant = Restaurant("Golden Plate", "Italian")

# Printing attributes
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

# Calling methods
restaurant.describe_restaurant()
restaurant.open_restaurant()

print(seperate)

# 9-2 Three Restaurants
restaurant1 = Restaurant("Sushi World", "Japanese")
restaurant2 = Restaurant("Taco Town", "Mexican")
restaurant3 = Restaurant("Burger Barn", "American")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()   

print(seperate) 

# 9-3 Users
class User:
    def __init__(self, first_name, last_name, age, location, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.email = email

    def describe_user(self):
        print(f"User Profile:")
        print(f" Name: {self.first_name} {self.last_name}")
        print(f" Age: {self.age}")
        print(f" Location: {self.location}")
        print(f" Email: {self.email}")
        print()

    def greet_user(self):
        print(f"Welcome back, {self.first_name}!\n")

# Creating several user instances
user1 = User("Amirah", "Banton", 18, "New York", "amirah@example.com")
user2 = User("Liam", "Johnson", 22, "California", "liam@example.com")
user3 = User("Sofia", "Martinez", 20, "Texas", "sofia@example.com")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()

print(seperate) 

# 9-4 Number Served
class RestaurantWithServed(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.number_served = 0

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, additional_served):
        self.number_served += additional_served
# Creating an instance
restaurant_served = RestaurantWithServed("Pasta Palace", "Italian")
restaurant_served.describe_restaurant()
print(f"Number served: {restaurant_served.number_served}")
restaurant_served.set_number_served(50)
print(f"Number served after setting: {restaurant_served.number_served}")
restaurant_served.increment_number_served(25)
print(f"Number served after incrementing: {restaurant_served.number_served}")

print(seperate)

# 9-5 Login Attempts

class User:
    def __init__(self, first_name, last_name, age, location, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.email = email
        self.login_attempts = 0  # New attribute

    def describe_user(self):
        print(f"User Profile:")
        print(f" Name: {self.first_name} {self.last_name}")
        print(f" Age: {self.age}")
        print(f" Location: {self.location}")
        print(f" Email: {self.email}")
        print(f" Login Attempts: {self.login_attempts}")
        print()

    def greet_user(self):
        print(f"Welcome back, {self.first_name}!\n")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


# Make an instance of User
user = User("Amirah", "Banton", 18, "New York", "amirah@example.com")

# Increment login attempts several times
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

# Print login attempts
print("Login attempts after incrementing:", user.login_attempts)

# Reset login attempts
user.reset_login_attempts()

# Print again to ensure it was reset
print("Login attempts after reset:", user.login_attempts)

print(seperate)

# 9-6 Ice Cream Stand
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type="Ice Cream"):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def add_flavor(self, flavor):
        self.flavors.append(flavor)

    def display_flavors(self):
        print(f"Available flavors at {self.restaurant_name}:")
        for flavor in self.flavors:
            print(f"- {flavor}")
# Creating an instance
ice_cream_stand = IceCreamStand("Sweet Treats")
ice_cream_stand.add_flavor("Vanilla")
ice_cream_stand.add_flavor("Chocolate")
ice_cream_stand.add_flavor("Strawberry")
ice_cream_stand.display_flavors()

print(seperate)

# 9-7 Admin
class User:
    def __init__(self, first_name, last_name, age, location, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print(f"User Profile:")
        print(f" Name: {self.first_name} {self.last_name}")
        print(f" Age: {self.age}")
        print(f" Location: {self.location}")
        print(f" Email: {self.email}")
        print()

    def greet_user(self):
        print(f"Welcome back, {self.first_name}!\n")


class Admin(User):
    def __init__(self, first_name, last_name, age, location, email):
        super().__init__(first_name, last_name, age, location, email)
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user"
        ]

    def show_privileges(self):
        print("Administrator Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


# Create an Admin instance
admin1 = Admin("Amirah", "Banton", 18, "New York", "amirah@example.com")
admin1.show_privileges()

print(seperate)

# 9-8 Privileges
class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            privileges = [
                "can add post",
                "can delete post",
                "can ban user"
            ]
        self.privileges = privileges

    def show_privileges(self):
        print("Administrator Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    def __init__(self, first_name, last_name, age, location, email):
        super().__init__(first_name, last_name, age, location, email)
        self.privileges = Privileges()  # Instance of Privileges class


# Create an Admin instance using the Privileges class
admin2 = Admin("Liam", "Johnson", 22, "California", "liam@example.com")
admin2.privileges.show_privileges()

print(seperate)

# 9-9 Battery Upgrade
class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")
        return range

    def upgrade_battery(self):
        if self.battery_size < 65:
            self.battery_size = 65
            print("Battery upgraded to 65 kWh.")
        else:
            print("Battery is already upgraded.")


class ElectricCar:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.battery = Battery()

    def describe_car(self):
        print(f"{self.year} {self.make} {self.model}")


# Make an electric car with default battery size (40)
my_ecar = ElectricCar("Tesla", "Model 3", 2025)

print("Before upgrade:")
my_ecar.battery.get_range()

print("\nUpgrading battery...")
my_ecar.battery.upgrade_battery()

print("\nAfter upgrade:")
my_ecar.battery.get_range()

print(seperate)

# 9-10 Imported Restaurant
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant is called {self.restaurant_name} and serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

# Using the Restaurant class
restaurant_imported = Restaurant("Global Eats", "International")
restaurant_imported.describe_restaurant()
restaurant_imported.open_restaurant()   

print(seperate)

# 9-11 Imported Admin
class User:
    def __init__(self, first_name, last_name, age, location, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.email = email

class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            privileges = ["can add post", "can delete post", "can ban user"]
        self.privileges = privileges

    def show_privileges(self):
        print("Administrator Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    def __init__(self, first_name, last_name, age, location, email):
        super().__init__(first_name, last_name, age, location, email)
        self.privileges = Privileges()

# Using the Admin class
from user import Admin

admin1 = Admin("Amirah", "Banton", 18, "New York", "amirah@example.com")
admin1.privileges.show_privileges()

print(seperate)

# 9-12 Multiple Modules
class User:
    def __init__(self, first_name, last_name, age, location, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.email = email
from user import User

class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            privileges = ["can add post", "can delete post", "can ban user"]
        self.privileges = privileges

    def show_privileges(self):
        print("Administrator Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    def __init__(self, first_name, last_name, age, location, email):
        super().__init__(first_name, last_name, age, location, email)
        self.privileges = Privileges()
from admin import Admin

admin2 = Admin("Liam", "Johnson", 22, "California", "liam@example.com")
admin2.privileges.show_privileges()

print(seperate)

# 9-13 Dice

import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(random.randint(1, self.sides))


# 6-sided die, rolled 10 times
die_6 = Die()
print("Rolling 6-sided die:")
for _ in range(10):
    die_6.roll_die()

print("\nRolling 10-sided die:")
die_10 = Die(10)
for _ in range(10):
    die_10.roll_die()

print("\nRolling 20-sided die:")
die_20 = Die(20)
for _ in range(10):
    die_20.roll_die()

print(seperate)

# 9-14 Lottery
import random

items = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
         'A', 'B', 'C', 'D', 'E')

winning_ticket = random.sample(items, 4)

print("Any ticket matching these 4 characters wins a prize:")
print(winning_ticket)
user_ticket = random.sample(items, 4)
print("Your ticket:")
print(user_ticket)
if user_ticket == winning_ticket:
    print("Congratulations! You have the winning ticket!")
else:
    print("Sorry, better luck next time.")

print(seperate)

# 9-15 Lottery Analysis
import random

# Possible items
items = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
         'A', 'B', 'C', 'D', 'E')

# Your ticket
my_ticket = ['A', 3, 7, 'D']

count_attempts = 0
won = False

while not won:
    count_attempts += 1
    drawn = random.sample(items, 4)
    if sorted(drawn) == sorted(my_ticket):
        won = True

print(f"It took {count_attempts} attempts to win the lottery!")

print(seperate)

# End of assignment 9 
