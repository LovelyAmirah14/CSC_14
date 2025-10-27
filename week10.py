class Pet:
    def __init__(self,type,name,age):
        self.type = type
        self.name = name
        self.age = age
        
    def age_in_dog_years():
        if self.type == "dog":
            return self.age * 7
        else:
            return "Not a dog"

p = Pet("Dog", "Buddy", 13)
a = Pet("Cat", "Catty", 16)

print(f"I have a pet that's a {p.type} named {p.name} and is {p.age} years old.")