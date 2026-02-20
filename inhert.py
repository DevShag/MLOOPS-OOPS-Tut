# Simple inheritance

# Base class
class Animal:
    def __init__(self, name):
        self.name = name


    def speak(self):
        print(f"{self.name} make a sound.")



# Derived class
class Dog(Animal):

    def __init__(self, name):
        super().__init__(name)
        self.behaviour = 'friendly'

    def speak(self):
        print(f"{self.name} barks.")



# Create an instance of Animal
animal = Animal("Generic Animal")
animal.speak()


# Create an instance of Dog
dog = Dog("Buddyl")
dog.speak()
