#exercise Pets
class Pets:
    def __init__(self, animals):
        self.animals = animals
    
    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat(Pets):
    def __init__(self, animals, meow, name, age):
        super().__init__(animals)
        self.meow = meow
        self.name = name
        self.age = age
    def walk(self):
        return f"{self.name} is walking around"

class Siamese(Cat):
    def __init__(self, animals, meow, name, age, origin):
        super().__init__(animals, meow, name, age)
        self.origin = origin

class Bengal(Cat):
    def __init__(self, animals, meow, name, age, sounds):
        super().__init__(animals, meow, name, age)
        self.sounds = sounds

all_cats = [Siamese(True,True, "Sasa", 4, "Thailand",), Bengal(True,True,"Cutie", 4, "special")]

sarah_pets = Pets (all_cats)
sarah_pets.walk()

#exercise 2 Dogs
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    def bark(self): 
        return f"{self.name} is barking"
    def run_speed(self):
        return self.weight/self.age * 10
    def fight(self, other_dog):
        if (self.run_speed() * self.weight) > (other_dog.run_speed()*other_dog.weight):
            return f"{self.name} won"
        else:
            return f"{other_dog.name} won"

#######################################
dog1 = Dog ("Barak", 4, 10)
dog2 = Dog ("Mia", 5, 15)        

print(dog1.bark())
print(dog2.run_speed())
print(dog1.fight(dog2))

