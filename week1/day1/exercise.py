#exercist 1
print("Hello world "*4)

#exercist 2
print((99**3)*8)

#exercist 3
#answers: False; True; False; False/wrong: cannot compare string with integer; False
print(bool(5 < 3))
print(bool(3 == 3))
print(bool(3 == "3"))
#print(bool("3" > 3))
print(bool("Hello" == "hello"))

#exercist 4
computer_brand = "Macbook"
print("I have a " + computer_brand + " computer.")

#exercist 5
name = "Emily Peng"
age = 37
shoe_size = 36
info = "My name is " + name + ", I am " + str(age) + " years old and my shoe size is " + str(shoe_size) + "."
print(info)

#exercist 6
a = 11
b = 9
if a > b:
    print("Helllo World")

#exercist 7
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")


#exercist 8
your_name = input("Enter your name: ")
if your_name == "Emily":
    print("Wow you and I have the same beautiful name!")
else:
    print("How come you don't have the same name with me?!")

#exercist 9
user_height = input("Enter your height in cm: ")
if int(user_height) >= 145:
    print("You are tall enough to ride the rollercoaster!")
else:
    print("You are not tall enough to ride the rollercoaster.")









