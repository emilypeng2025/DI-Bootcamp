#Exercise 1: Favorite Numbers

# Instructions:

# Create a set called my_fav_numbers and populate it with your favorite numbers.
# Add two new numbers to the set.
# Remove the last number you added to the set.
# Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.
# Note: Sets are unordered collections, so ensure no duplicate numbers are added.

my_fav_numbers = {8, 10, 11, 15, 22, 24}
my_fav_numbers.add(88)
print(my_fav_numbers)

my_fav_numbers.add(100)
print(my_fav_numbers)

#another method: use .update()
my_fav_numbers.update([88,100])
print(my_fav_numbers)


my_fav_numbers.remove(100)
print(my_fav_numbers)

my_fav_numbers.remove(88)
print(my_fav_numbers)

#another method: use -=
my_fav_numbers -={88, 100}


friend_fav_numbers ={1, 2, 3, 4, 5}
our_fav_numbers = my_fav_numbers. union(friend_fav_numbers)
print(our_fav_numbers)



#exercise 2

# Instructions:
# Given a tuple of integers, try to add more integers to the tuple.
# Hint: Tuples are immutable, meaning they cannot be changed after creation. Think about why you can’t add more integers to a tuple.

students_number = (32, 45, 50)
# tuples cannot use add or insert nor += students_number += (25) 
# change tuple to list and change list: 
students_number_list = list(students_number)
students_number_list.insert(0,25)
students_number_list.insert(4,100)
students_number = tuple(students_number_list)
print(students_number)

#reasons why tuples cannot be changed once established? it is FASTER to deal with the elements

#Exercise 3: List Manipulation
#Instructions:
# You have a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# Remove "Banana" from the list.
# Remove "Blueberries" from the list.
# Add "Kiwi" to the end of the list.
# Add "Apples" to the beginning of the list.
# Count how many times "Apples" appear in the list.
# Empty the list.
# Print the final state of the list.

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
print(basket)

del basket[2]
print(basket)

basket.append("Kiwi")
print(basket)

basket.insert(0, "Apples")
print(basket)

basket = ['Apples', 'Apples', 'Oranges', 'Kiwi']
print(basket.count('Apples'))

print(basket.clear())

print(basket)


#Exercise 4: Floats
# Instructions:

# Recap: What is a float? What’s the difference between a float and an integer? 
# a float is a decimal that is with a decimal point
# Create a list containing the following sequence of mixed floats and integers:
# 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.
# Avoid hard-coding each number manually.
# Think: Can you generate this sequence using a loop or another method?

list1 =[1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]

list3=[]
num = 1.5
while num <= 5:
    list3.append(num) #this step put num into list3
    num += 0.5

print(list3)

# use.apend to put the output into a list [].


#2nd solution:
list2 = []
for i in range (3,11):
    list2.append(i*0.5)
print(list2)

#Exercise 5: For Loop
# Instructions:
# Write a for loop to print all numbers from 1 to 20, inclusive.
# Write another for loop that prints every number from 1 to 20 where the index is even.

for i in range(1,21):
    print(i)

for i in range(1, 21, 2):
    print(i)

#Exercise 6: While Loop
# Instructions:

# Write a while loop that keeps asking the user to enter their name.
# Stop the loop if the user’s input is your name.

my_name = "Emily"
user_name = input("Please write your name: ")

original_input = user_name

while user_name != my_name:
    print("You have a nice name!")
    user_name = input("Can you try to guess my name? (or 'exit'to quit)")
    print(f"I am Emily. Welcome, {original_input}!")
    break
else:
    print(f"I am Emily, nice to meet you,{original_input}!")

#Exercise 7: Favorite Fruits
# Instructions:
# Ask the user to input their favorite fruits (they can input several fruits, separated by spaces).
# Store these fruits in a list.
# Ask the user to input the name of any fruit.
# If the fruit is in their list of favorite fruits, print:
# "You chose one of your favorite fruits! Enjoy!"
# If not, print:
# "You chose a new fruit. I hope you enjoy it!"

user_fav_fruits = input("Write what fruits you like, seperate each fruit by spaces: ")
fruit_list =user_fav_fruits.split()
print("The fruits you like are: ",fruit_list)

one_fruit = input("Name one fruit that you are thinking of now: ")
if one_fruit in fruit_list:
    print("You chose one of your favorite fruits! Enjoy!")
else: 
    print("You chose a new fruit. I hope you enjoy it!")

#Exercise 8: Pizza Toppings
# Instructions:
# Write a loop that asks the user to enter pizza toppings one by one.
# Stop the loop when the user types 'quit'.
# For each topping entered, print:
# "Adding [topping] to your pizza."
# After exiting the loop, print all the toppings and the total cost of the pizza.
# The base price is $10, and each topping adds $2.50.

#common pizza toppings: cheese, sausage, pepperoni, mushroom, green peppers, onions, olives...
toppings =[]
count = int(input("How many toppings do you want on your pizza?" ))
price_per_topping = 2.50
total_price = 10

for i in range(count):
    topping = input(f"Please enter topping #{i+1}: ")
    print(f"Adding {topping} to your pizza.")
    toppings.append(topping)
    total_price += price_per_topping
print("You chose: ", toppings)

order_conclude = input("confirm your order: yes/no ")
if order_conclude == "yes":
    print("Total price is: $", total_price)

#Exercise 9: Cinemax Tickets

# Instructions:
# Ask for the age of each person in a family who wants to buy a movie ticket.
# Calculate the total cost based on the following rules:
# Free for people under 3.
# $10 for people aged 3 to 12.
# $15 for anyone over 12.
# Print the total ticket cost.

total_price = 0
count_tickets = int(input("How many tickets do you need? "))
for i in range(count_tickets):
    age = int(input(f"How old is person #{i+1}?"))

    if age < 3:
        price = 0
    elif age < 12:
        price = 10
    else:
        price = 15
    
    total_price = i + price 
    print(f"Person #{i+1} is {age} years old, ticket price: ${price}")

print("\nTotal price for all tickets is: $ ", total_price) 


#Exercise 10: Sandwich Orders
# Instructions:
# Using the list:
# sandwich_orders = ["Tuna", "Pastrami", "Avocado", "Pastrami", "Egg", "Chicken", "Pastrami"]
# The deli has run out of “Pastrami”, so use a loop to remove all instances of “Pastrami” from the list.
# Prepare each sandwich, one by one, and move them to a list called finished_sandwiches.
# Print a message for each sandwich made, such as: "I made your Tuna sandwich."
# Print the final list of all finished sandwiches.

sandwich_orders = ["Tuna", "Pastrami", "Avocado", "Pastrami", "Egg", "Chicken", "Pastrami"]
while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")

print (sandwich_orders)


finished_sandwiches =['Tuna', 'Avocado', 'Egg', 'Chicken']

while finished_sandwiches:
    item = finished_sandwiches.pop(0)
    print(f"I made you a {item} sandwich")

print("finished sandwiches:", finished_sandwiches)


