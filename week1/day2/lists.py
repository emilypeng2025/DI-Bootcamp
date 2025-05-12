# # #list

# # #syntax
# # some_list = list('item 1') #this one is used to convert other sequence to a list
# # other_list = ['item 1'] # This one is used to create an empty list

# # print(some_list)
# # print(other_list)

# # #accessing by index
# # print(some_list[1])

# # my_list = []

# # #methods for lists
# # my_list.append('A')
# # print(my_list)

# # ?????
# # character_name = ['Phoebe', 'Rachel', 'Monica', 'Ross']
# # my_fav_character_name = character_name.extend('Joey')
# # print (my_fav_character_name)

# # ???
# # names = []
# # names.append('JOEY','Ross')
# # print (names)

# # names.extend('Monica', 'Ross')

# num_list = (list(range(1,8))
# print(number_list)

# #string slicing
# print(num_list[0:5])

#sorted()
#.sort() 
#sorted didnt change the order

# example
# fruits = ['banana','orange','lime','apple']
# sorted_fruits=fruits.sort()
# print(sorted_fruits)


list1 = [5, 20, 10, 15, 20, 25, 50, 20]
print(list1.index(20))

#or
if list1.index(20):
    index_found = list1.index(20)
    list1.insert(index_found, 200)
    list1.remove(20)
    print (list1)
else:
    print('element not found')

#which method to usd to replace? insert


