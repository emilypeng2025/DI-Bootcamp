#Challenge 1: Sorting

first_input = input("Write some words here, using',' between each word: ")
#word_numbers = first_input.count(",") 
no_comma = first_input.replace(","," ")
word_list = no_comma.split() #split the strings to words based on spaces
word_list.sort() #list can use.sort()
result = ",".join(word_list) #use list .join()

print(result)

#challenge 2: longest word

#first try: use the dictionary to access both key and value, compare value length
# the_sentence = input("Please write a sentence: ")
# word_list = the_sentence.split() #split the sentence into a list of words

# my_dictionary = {}

# for N, word in enumerate(word_list):
#     my_dictionary[N] = word

# # print(my_dictionary)
# longest_length = 0
# longest_index = 0

# for i in my_dictionary:
#     if len(my_dictionary[N])>longest_length:
#         longest_length =len(my_dictionary[i])
#         longest_index = i

# print(f"The longer word is {my_dictionary[longest_index]}")

#method 2 without the dictionary:
# the_sentence = input("Please write a sentence: ")
# word_list = the_sentence.split()

# longest_index = 0
# longest_length = 0

# for i in range(len(word_list)):
#     if len(word_list[i]) > longest_length:
#         longest_length = len(word_list[i])
#         longest_index = i

# print(f"The longest word is {word_list[longest_index]}")

def longest_word(words):
    longest = ""
    for word in (words):
        if len(word) > len(longest):
            longest = word
    return longest

sentence = input("Please write a sentence: ")
word_list = sentence.split()

the_longest_word = longest_word(word_list)
print(f"{the_longest_word} is the longest word")