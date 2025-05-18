#WHAT IS OOP
#WHAT IS OBJECT

# class Dog:
#     pass

# #an instance (or object) of class Dog is created:
# shelter_dog = Dog()
 
# #how to create with the attribute
# shelter_dog.color = "Black"
# print(shelter_dog.color)

# pitbull = Dog()
# print(pitbull.color) #output :AttributeError: 'Dog' object has no attribute 'color'

class Dog:
    
    def __init__(self, name, color, breed, age): #if need funtion, always need to pass self
        print("creating object")
        self.name = name
        self.color = color
        self.breed = breed
        self.age = age 

#creating the instances of Dog after creating the __ini__()



#exercise: create two objects(instances) of the class Dog
class Dog:

    def __init__(self, name, color, breed, age):
        print('creating object')
        self.name = name
        self.color = color
        self.breed = breed
        self.age = age
    #this is a method(inside a class)
    #how to create a method
    def bark(self): 
        print(f"{self.name} is barking")
    def walk(self, meters):
        print(f"{self.name} is walking {meters} meters")
    def birthday(self): 
        self.age += 1
    def rename(self,new_name):
        self.name = new_name

shelter_dog = Dog ("Rex", "black", "shelter", 5)
husky_dog = Dog ("Thunder","black and white", "husky", 4)
Chihuahua_dog = Dog ("Little","brown","Chihuahua",6)
husky_dog.bark()
Chihuahua_dog.walk(500)
shelter_dog.birthday()
print(shelter_dog.age)
shelter_dog.rename("Emily")
print(shelter_dog.name)
print(vars(shelter_dog))

# print(husky_dog.__dict__)
# print(Chihuahua_dog.__dict__)

# my_dogs = [shelter_dog,husky_dog,Chihuahua_dog]
# print(my_dogs)

# for dog in my_dogs:
#     print(dog.name)

# print(type(husky_dog))

# print(help(str))

# my_dogs_objects = [obj for obj in globals().values() if isinstance(obj. Dog)]

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

## create an instance of the class
p = Point(3,4)
a = Point (100,200)

## access the attributes
print("p.x is:", p.x)
print("p.y is:", p.y)
print("p.a is:", a.x)


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"{self.name} says woof!!")
    def dance(self):
        print(f"{self.name} turns around chasing his tail")

Chihuahua = Dog ("Lola", 2)
Bulldog = Dog ("Barak", 9)
Bulldog.dance()