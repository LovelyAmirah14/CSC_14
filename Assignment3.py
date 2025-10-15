# Assignment 3 Banton, Amirah
seperate = "--------------------------------------------------"

# 3-1 Names 
names = ["Amirah", "Tramanee", "Mckenzie", "Hunter"]
print(names[0]) # prints the first name on the list starts at 0
print(names[1])
print(names[2])
print(names[3]) # print the last name on the list 

print(seperate)

# 3-2 Greetings
print("Sincerly from: " + names[0])
print("Hey, you just got a new tattoo right " + names[1] + "?")
print("Your getting your nails done on sunday " + names[2] + " that sounds so good!")
print("Jeez " + names[3] + " you sure have a lot of assignments due soon!")

print(seperate)

# 3-3 Your Own List
valorantguns = ["Vandal", "Ghost", "Phantom", "Sherrif"]
print("My favorite gun in the game is a " + valorantguns[0] + " but when you first start out my go to for headshots is definitely a " + valorantguns[1] + ".")

print(seperate)

# 3-4 Guest List
guest_list = ["Amirah", "Tramanee", "Mckenzie", "Hunter"]
print(guest_list[0] + " is hosting a party this weekend and they are doing invite only.")
print("Hey " + guest_list[1] + ", would you like to come to my party?")
print("Hey " + guest_list[2] + ", would you like to come to my party?")
print("Hey " + guest_list[3] + ", would you like to come to my party?") 

print(seperate)

# 3-5 Changing Guest List
print(guest_list[2] + " can't come to the party because she is getting her nails on Sunday I totally forgot")
guest_list[2] = "Gabby" # Mckenzie can't come so I texted gabby and she can come now
print("THE OFFICIAL GUEST LIST: " + guest_list[0] + ", " + guest_list[1] + ", " + guest_list[2] + ", " + guest_list[3]) # printing the new guest list

print(seperate)

# 3-6 More Guests
print(" More people can come to the party because I upgraded the table sending out more invites now!")
guest_list.insert(0, "Olivia")
guest_list.insert(2, "Sisi")
guest_list.append("Rene'Sia")
print("THE OFFICIAL GUEST LIST: " + guest_list[0] + ", " + guest_list[1] + ", " + guest_list[2] + ", " + guest_list[3] + ", " + guest_list[4] + ", " + guest_list[5] + ", " + guest_list[6]) # printing the new guest list

# 3-7 Shrinking Guest List

print("OH NO! The new table won't arrive on time and I can only invite two people to the party now.")
removed_guest = guest_list.pop() # removing the last person on the list
print("Sorry " + removed_guest + ", I can't invite you to the party.")
removed_guest = guest_list.pop() # removing the last person on the list
print("Sorry " + removed_guest + ", I can't invite you to the party.")
removed_guest = guest_list.pop() # removing the last person on the list
print("Sorry " + removed_guest + ", I can't invite you to the party.")
removed_guest = guest_list.pop() # removing the last person on the list
print("Sorry " + removed_guest + ", I can't invite you to the party.")
print("THE OFFICIAL GUEST LIST: " + guest_list[0] + ", "
        + guest_list[1]) # printing the new guest list
del guest_list[1] # removing the last two people on the list
del guest_list[0]
print(guest_list) # printing the empty list

print(seperate)

# 3-8 Seeing the World
places = ["Japan", "Italy", "Greece", "France", "Spain"]
print(places) # original order
print(sorted(places)) # alphabetical order
print(places) # original order
print(sorted(places, reverse=True)) # reverse alphabetical order
print(places) # original order
places.reverse() # reversing the list
print(places) # printing the reversed list
places.reverse() # reversing the list back to original
print(places) # printing the original list
places.sort() # sorting the list in alphabetical order
print(places) # printing the sorted list
places.sort(reverse=True) # sorting the list in reverse alphabetical order 
print(places) # printing the reverse sorted list

print(seperate)

# 3-9 Dinner Guests
print("I am inviting " + str(len(guest_list)) + " people to my party.") # printing the number of people invited to the party
# there is no one invited to the party so it prints 0
print("I am inviting " + str(len(places)) + " places I want to visit.") # printing the number of places I want to visit
# there is 5 places I want to visit so it prints 5

print(seperate)

# 3-10 Every Function
# I have already done every function in the previous exercises.
# I have used len(), append(), insert(), pop(), del(), sort(), sorted(), reverse(), and print() functions in the previous exercises.
# I have not used remove() function yet.
# I will use remove() function to remove a specific item from a list.
places.remove("Greece") # removing Greece from the list of places
print(places) # printing the list after removing Greece
# now the list of places is ['Spain', 'Italy', 'France', 'Japan'] after removing Greece

print(seperate)
# End of Assignment 3