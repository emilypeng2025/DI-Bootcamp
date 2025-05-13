#Challenge 1: Multiples of a Number

number = int(input("write a number: "))
length = int(input("write a length: "))

multiples = []

for i in range(1, length + 1):
    multiples.append(number * i)

print(multiples)

#Challenge 2: Remove Consecutive Duplicate Letters
word = input("Enter a word: ")
unique_character = [] #this is to store unrepeated characters here as a list

character_listed = list(word)

for character in character_listed:
    if character not in unique_character:
        unique_character.append(character)

result = '' . join(unique_character)
print(result)


# Challenge 2: Remove Consecutive Duplicate Letters


# Key Python Topics:
# input() function
# Strings and string manipulation
# Loops (for or while)
# Conditional statements (if)


# Instructions:
# 1. Ask the user for a string.
# 2. Write a program that processes the string to remove consecutive duplicate letters.

# The new string should only contain unique consecutive letters.
# For example, “ppoeemm” should become “poem” (removes consecutive duplicates like ‘pp’, ‘ee’, and ‘mm’).
# 3. The program should print the modified string.



# Example 1:

# Input:
# user’s word: "ppoeemm"
# Output:
# "poem"



# Example 2:

# Input:
# user’s word: "wiiiinnnnd"
# Output:
# "wind"



# Example 3:

# Input:
# user’s word: "ttiiitllleeee"
# Output:
# "title"



# Example 4:

# Input:
# user’s word: "cccccaaarrrbbonnnnn"
# Output:
# "carbon"



# Notes:
# The final string will not include any consecutive duplicates, but non-consecutive duplicates are allowed.
# Example: In "carbon", the two ‘r’s are allowed because they are not consecutive.
