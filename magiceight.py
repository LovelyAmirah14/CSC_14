import random
answers =["yes","no", "maybe", "unlikely", "perhaps"]
print("What do you want to know?")
uestion = input()
answer = random.choice(answers)
print(answer)