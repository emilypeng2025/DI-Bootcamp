#sequences and collections in Python


#lists
#use cases: ordered by index


#creating a list - []
#methods:
#.append()
#.clear()
#.extend()
#.pop()
#.insert()
#.remove()
#.sort

#methods that create a new list
#sorted()
#split()
tasks = input ('enter a task: ')
task_list = tasks.split()
print(task_list)

list_1 = [1,2.3,4,5]
list_2 = [6,7,8,9,10]

list_3 = [*list_1,*list_2]
print(list_3)

#tuples
#use cases: 
# immutable, useful if you want to store information that shouldnt be changed: password list, addresses, coordinates, id numbers

x,y= (4,6) #unpacking a tuple #() and at least two elements inside not 1


#sets
#useful for data that you dont want to have duplicated. eg IDs
#finding common elements between different collections

fruits = {'apple','banana','tomato','pineapple'}
vegetable ={'tomato','cucumber','onion','lettuc'}

common = fruits.intersections(vegetable)
print(common)

#dictionaries
#key and value pairs
#Use cases: when we need a logical association between the data and the label

user_information = {'name':'Juliana','age':35,'address':"TLV"}

users = {"alice":{"age":25, "email":["alice@example.com","alice@gmail.com"]}
         "Jonh":{"age":24, "email":"john@example.com"}
         }

