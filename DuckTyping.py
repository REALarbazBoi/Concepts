# Example 1
def driver(car):
    car.drive()

class Creta:

    def drive(self):
        print("Creta is driving")

class Mercedes:

    def drive(self):
        print("Mercedes is driving")

c = Creta()
driver(c)

m = Mercedes()
driver(m)

# Example 2

def PetLover(pet):
    pet.talk()
    if hasattr(pet, "walk"):
        pet.walk()

class Duck:
    def talk(self):
        print("Duck is talking")

    def walk(self):
        print("Duck is walking")

class Dog:
    def talk(self):
        print("Dog is talking")



k = Duck()
PetLover(k)

d = Dog()
PetLover(d)