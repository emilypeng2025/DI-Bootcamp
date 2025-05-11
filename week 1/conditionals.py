# conditionals : if statements

#syntax
# if condition:
#     <indented block of code>

#game to guess a number

# secret_number = 55
# user_number = int(input("guess a number: "))

# if user_number == secret_number:
#     print("you guessed it right!")
# else:
#     print("sorry, not the right number")

#exercise

number = int(input("write a number between 1 and 100: "))

if number % 3 and number % 5 == 0:
    print("FizzBuzz")
    
elif number % 3 == 0:
    print("Fizz")

elif number % 5 == 0:
    print("Buzz")

else:
    print("not valid")

