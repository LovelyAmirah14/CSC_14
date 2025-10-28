import random

spanish = ["perro", "gato", "bajo",]
english = ["dog", "cat", "beach"]

i = random.randint(0, len(spanish)-1)
print(spanish[i])
print("What word is this in English?")
answer = input()
if answer == english[i]:
    print("You did it!")
else:
    print(f"Sorry, the answer is {english[i]}")