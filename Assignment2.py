# Assignment 2 Banton, Amirah
seperate = "--------------------------------------------------"

# 2-1 Simple Message
message = "I'm steve"
print(message)

print(seperate)

# 2-2 Simple Messages
words = "You're amazing and cool,"
print(words)
words = "but you have some flaws you could fix." # setting the variable to something else
print(words) # this is printing the new changes variable.

print(seperate)

# Book notes 
# When wanting to call uppercase or lowercase you can call the variable (variable).upper or (variable).lower
# example 
name = "Ada Lovelace"
print(name.upper())
print(name.lower())
# You can combine first name and last name together

print(seperate)

# 2-3 Personal Message
name = "Amirah"
print("Hey "+ (name) + ", How's your day?") # calling the variable and incorparting it within the sentence

print(seperate)

# 2-4 Name Cases
print(name.lower()) # setting my name to lowercase
print(name.upper()) # setting my name to uppercase
print(name.title()) # setting my name to title which capitalizes the first letter within my name

print(seperate)

# 2-5 Famous Quote 
print("Yumeko Jabami once said, 'If you want to earn something, you need to reach out for it. Pro-athletes give up their teenage years to train. Business owners put up collateral to borrow money. That's how it always works. to make make your ambitions come true, you have to take risks. The larger the ambition the greater the risk. That might involve time or enough work to affect your lifepan... So make your choice. Live in peace as a wannabe or risk losing it all to reach the very top. You're the one who needs to decide.'")
# this is a really long quote but I truly love it from this anime

print(seperate)

# 2-6 Famouse Quote 2
quote = "If you want to earn something, you need to reach out for it. Pro-athletes give up their teenage years to train. Business owners put up collateral to borrow money. That's how it always works. to make make your ambitions come true, you have to take risks. The larger the ambition the greater the risk. That might involve time or enough work to affect your lifepan... So make your choice. Live in peace as a wannabe or risk losing it all to reach the very top. You're the one who needs to decide."
print("Yumeko Jabami once said, " + (quote))
      
print(seperate)

# 2-7 Stripping Names
# I am gonna use my name still from the previous method for personal message name = "Amirah"
print("This is my name stripped on the right " + name.rstrip() + "\n" + name.lstrip() + "\t" + name.strip())