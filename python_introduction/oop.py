class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return "Woof wooof"
    

dog = Dog("Tony","German Shepherd")

print(f"My dog, {dog.name} is a {dog.breed} and barks {dog.bark()}")


class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Lion(Animal):
    def speak(self):
        return f"{self.name} roars"

class Elephant(Animal):
    def speak(self):
        return f"{self.name} trumpets"
    
zoo = [
    Lion("Simba"),
    Elephant("Dumbo")
]

for animal in zoo:
    print(animal.speak())