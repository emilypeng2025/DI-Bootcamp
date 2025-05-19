from exercisew2d2 import Dog
import random

#exercise 3 
class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        print(self.bark())
        self.train = True
    
    def play(self, *args):
        name1 = [self.name] + [dog.name for dog in args]
        names_str =", ".join(name1)
        print(f"{names_str} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
            print(f"{self.name} {random.choice(tricks)}")

        
dog_a = PetDog ("Pink", 4, 10, True)
dog_b = PetDog ("JJ", 5, 15) 
dog_a.train()
dog_a.play(dog_a, dog_b)
dog_a.do_a_trick()

#exercise 4 family and person classes
class Person:
    def __init__(self, first_name, age, last_name=""):
        self.first_name = first_name
        self.age = age
        self.last_name = last_name
    def is_18(self):
        if self.age >= 18:
            return True
        else:
            return False

class Family:
    def __init__(self, last_name, members=[]):
        self.last_name = last_name
        self.members = members
    
    def born(self, first_name, age):
        new_person = Person(first_name, age)
        new_person.last_name = self.last_name
        self.members.append(new_person)

    def check_majority(self, first_name):
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
                    print("You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                return # once you found the person, finish this function
        print("This person is not in the family.")
    
    def family_presentation(self):
        print(f"family name: {self.last_name}")
        print("family members: ")
        for member in self.members:
            print(f"{member.first_name}, {member.age} years old")

example_family = Family ("Peng")
example_family.born ("Emily", 20)
example_family.born ("Yali", 7)

example_family.family_presentation()
example_family.check_majority("Emily")
example_family.check_majority("Yali")







    
    