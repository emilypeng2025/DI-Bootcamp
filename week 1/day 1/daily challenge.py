#building up a string

#1
string = input("write a sentence here: ")
character_count = len(string)
if character_count < 10:
    print("String not long enough.")
elif character_count > 10:
    print("String too long.")
else:
    print("Perfect string")

print(string[0])
print(string[-1])

for character in string:
    print(character)

for character in range(1, len(string)+1):
    print(string[:character])

#random.shuffle
import random
all_letters= list(string)
random.shuffle(all_letters)
shuffled = "".join(all_letters)
print(shuffled)