#exercist 1
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat1 = Cat ("Kitty", 3)
cat2 = Cat ("Garfield", 7)
cat3 = Cat ("Maomao", 9)
# print(cat1.__dict__)

def find_oldest_cat(cat1, cat2, cat3):
    oldest_cat = cat1
    for cat in (cat1, cat2, cat3):
        if cat.age > oldest_cat.age:
            oldest_cat = cat
    return oldest_cat

oldest_cat = find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")

#exercise 2:

class Dog:
    def __init__(self, dog_name, dog_height):
        self.name = dog_name
        self.height = dog_height
    def bark(self):
        print(f"{self.name} goes woof!")
    def jump(self):
        print(f"{self.name} jumps {self.height*2} cm high!")

davids_dog = Dog ("Snowball", 30)
sarahs_dog = Dog ("Pitzi", 10)

print(davids_dog.__dict__)
print(sarahs_dog.__dict__)
print(davids_dog.bark())
print(sarahs_dog.bark())
print(davids_dog.jump())
print(sarahs_dog.jump())

if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is bigger than {sarahs_dog.name}")
else:
    print (f"{sarahs_dog.name} is bigger than {davids_dog.name}")

#exercise 3 Who’s the song producer?

lyrics = []
class Song:
    def __init__(self,lyrics):
        self.lyrics=lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

# stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
# stairway.sing_me_a_song()

my_song = Song (lyrics)
my_song.sing_me_a_song()

#exercise 4 Afternoon at the Zoo

class Zoo:
    def __init__(self,zoo_name):
        self.animals = [] 
        self.name = zoo_name
    
    def add_animal(self, new_animal):
        if new_animal in self.animals:
            return self.animals
        else:
            self.animals.append(new_animal)
            return self.animals
    
    def get_animals(self):
        if self.animals:
            print(self.animals)
    
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            return self.animals

    def sort_animals(self):
        capitalized = [animal.capitalize() for animal in self.animals]
        capitalized.sort()
    
        animal_dict = {} #create dictionary with first letter as key
        for animal in capitalized:
            letter = animal[0] #first letter as key
            if letter not in animal_dict:
                animal_dict[letter] = [animal]
            else:
                animal_dict[letter].append(animal)
        
        return animal_dict

    def get_group(self):
        animal_dict = self.sort_animals()
        for key, value in animal_dict.items():
            print(f"{key}:{value}")

new_zoo = Zoo("New TLV Zoo")
print(new_zoo.name)




