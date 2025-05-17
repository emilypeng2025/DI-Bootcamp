#OOP

#2 VIDEOS
# OOP

# class BigObject:
#     pass


# obj1 = BigObject()
# obj2 = BigObject()
# obj3 = BigObject()

# print(type(None))
# print(type(True))
# print(type(5))
# print(type(5.5))
# print(type('hi'))
# print(type([]))
# print(type(()))
# print(type({}))
# print(type(obj1))
# print(type(obj2))


#review of the week: day 5 online learning
picture = [[0,0,0,1,0,0,0],
           [0,0,1,1,1,0,0],
           [0,1,1,1,1,1,0],
           [1,1,1,1,1,1,1],
           [0,0,0,1,0,0,0],
           [0,0,0,1,0,0,0]]
#task: replace "0" with "", and "1" with ""

letters = []
for letters in picture:
    for number in letters: 
        if (number == 1):
            print("*", end="")
        else: 
            print(" ", end="")
    print("")
    
