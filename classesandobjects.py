class Dog:
    # class attribute - same value for species for each instance of the class
    species = "Canis familiaris"

    # constructor
    def __init__(self, name, age):
# these are  instance attributes - specific to the instance
        self.name = name
        self.age= age
    def bark(self):
        print("Woof!")

my_dog = Dog("Buddy", 3)

print(my_dog.species)
my_dog.bark()

patients = [
    Dog("Buddy", 4),
    Dog("Max", 8),
    Dog("Charlie", 1)
]
for patient in patients:
    print(patient.age)


    # Inheritance!

# class inherits properties and methods from another class

class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Animal makes a sound")
class Dog(Animal): # dog inherits name, but speak is redefined specifically for dog.
    def speak(self):
        print(f"{self.name} says Woof!")      
