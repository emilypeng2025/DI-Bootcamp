#SEQUENCES AND COLLECTIONS IN PYTHON:
#organizing, storing and retrieving data

#LISTS
# USE CASES: to store and organize data that can be changed, ordered by index. 
# The most "flexible" collection

# creating a list = [] squared brackets 
# methods
# append()
# extend()
# remove()
# pop()
# sort()

# methods that creates a new list
# sorted()
# split()
# tasks = input('enter a task separated by coma: ')
# tasks_list = tasks.split(', ')
# print(tasks_list)

list_1 = [1,2,3,4,5]
list_2 = [6,7,8,9,10]

list_3 = [*list_1, *list_2]
print(list_3)

# TUPLES
# use cases:
# useful if you want to store information that shouldn't be change:
# password list, addresses, coordinates, id numbers

x, y = (4, 6) #unpacking a tuple

coordinates = (4, 6)
print(coordinates[1])

addresses = ('Ben Yhuda St', 'Hanamel St', 'Hayarden St', 'Hanamel St')
print(addresses.count('Hanamel St'))

# SETS
#Use cases: useful for data that you don't want to have duplicated. Ids,
# finding common elements between different collections
# 
# fruits = {'apple', 'banana', 'tomato', 'pineapple'} 
# vegetables = ['broccoli', 'carrot', 'potato', 'tomato']

# common = fruits.intersection(vegetables)
# print(common)


#DICTIONARIES
#Use cases: when we need a logical association between the data and the label

users = {"alice": {"age": 25, "email": ["alice@example.com", "alice@gmail.com" ]},
         "bob": {"age": 30, "email": "bob@example.com"}}

users.update({'john': {"age": 45, "email": "john@example.com"}})
print(users)

print(users['bob']['email'])
print(users['alice']['email'][1])

two_D_list = [['-', '-', '-'],
             ['-', '-', '-'],
             ['-', '-', '-']]

two_D_list[0][0] = 'x'
print(two_D_list)