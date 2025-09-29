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

