#exercise 1
def display_message():
    print("I am learning about functions in Python.")
display_message()

# Step 1: Define a Function
# Define a function named display_message().
# This function should not take any parameters.

# Step 2: Print a Message
# For example: “I am learning about functions in Python.”

# Step 3: Call the Function
# This will execute the code inside the function and print your message.




#exercise 2
def favorite_book(title):

    print(f"One of my favorite book is {title}")

favorite_book("Alice in Wonderland")

# Step 1: Define a Function with a Parameter
# Define a function named favorite_book().
# This function should accept one parameter called title.

# Step 2: Print a Message with the Title
# The function needs to output a message like “One of my favorite books is <title>”.

# Step 3: Call the Function with an Argument
# Call the favorite_book() function and provide a book title as an argument.
# For example: favorite_book("Alice in Wonderland").

#exercise 3
def describe_city(city, country="Unknown Country"):
    print(f"{city} is in {country}.")

describe_city("Paris")
describe_city("Reykjavik", "Iceland")

# Step 1: Define a Function with Parameters
# Define a function named describe_city().
# This function should accept two parameters: city and country.
# Give the country parameter a default value, such as “Unknown”.

# Step 2: Print a Message
# Inside the function, set up the code to display a sentence like “ is in “.
# Replace <city> and <country> with the parameter values.

# Step 3: Call the Function
# Call the describe_city() function with different city and country combinations.
# Try calling it with and without providing the country argument to see the default value in action.
# Example: describe_city("Reykjavik", "Iceland") and describe_city("Paris").

#exercise 4
import random
dice1 = random.randint(1,100)
def number(luckynumber):
    
    if luckynumber == dice1:
        print("Good job! SAME NUMBER!!")
    else:
        print(f"Unfortunately,{dice1} isn't equal to {luckynumber}")
number(input("Guess the lucky number (1-100) here: "))






#Exercise 5: Let’s Create Some Personalized Shirts!

def make_shirt(size="large", text="I love Python"):
        print(f"Message for shirt size {size}: {text}")

make_shirt()
make_shirt("large",)
make_shirt(size="medium",)
make_shirt()

# Exercise 6: Magicians…
magician_names = ['Harry Houdini','David BLaine','Criss Angel']
def show_magicians(magician_names):
     for magician in magician_names:
        print(magician)
def make_great(magicians):
    great_magicians = []
    for magician in magicians:
        great_magicians.append(f"The Great {magician}")
    return great_magicians
great_magicians = make_great(magician_names)
show_magicians(great_magicians)

# Exercise 7: Temperature Advice
import random

def get_random_temp():
    return random.randint(-10,40)

temperature = get_random_temp()
print(f"The temperature right now is {temperature}")

def main(temperature):
    if int(temperature) < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif int(temperature) <= 16:
        print("Quite chilly! Don't forget your coat.")
    elif int(temperature) <= 23:
        print("Nice weather.")
    elif int(temperature) <= 32:
        print("A bit warm, stay hydrated.")
    elif int(temperature) <= 40:
        print("It's really hot! Stay cool.")
main(temperature)
        
