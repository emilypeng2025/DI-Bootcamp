#review week1 basics
#variable: declare a variable

#basic data types
#sequences:
#collections
#functions: 
#arguemeent: positional arguements, keywords arguements, default arguments,*args,**kwargs
#"call the function"
#methods: are functions that are part of a class scope

#review of day1 OOP
#OOP
#class
#objects

class Animal:
    def __init__(self, name, family, legs):
        self.name = name #self:object .name key =name value  (in dictionary if you need to print to check behind the scene: print(object.__dict__))
        self.family = family
        self.legs = legs
        self.full_name = f"{name} {family}"

class Dog(Animal):
    def __init__(self, name, family, legs, trained, age):
        super().__init__(name, family, legs)
        self.trained = trained 
        self.age = age
    def bark(self):
        print(f'A {self.name} is barking')

    def sleep(self):
        return f'{self.name} is sleeping'

class Cat(Animal):
    def get_crazy(self):
        print(f"{self.name} is running with its {self.legs} legs in full power")

class Aliens:
    def __init__(self, personal_name, planet):
        self.personal_name = personal_name
        self.planet = planet
    # def fly(self):

cat1 = Cat("Kitty", "Hello", 4)
cat1.get_crazy()

dog1 = Dog ("barak","Good", 3, True, "9")
print(dog1.name)
