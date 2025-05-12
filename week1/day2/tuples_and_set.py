#tuple 元组，是不可变的，一旦创建不能更改里面的元素。

#accessing by index

#?my_tuple = .range(0:11)
#workaround on how to change tuples:
temp_list = list(my_tuple) #this step you convert a tuple to a list
temp_list.extend('A','B','C') #change methods in lists
my_tuple = tuple(temp_list) 
print(my_tuple)

#easier way:
my_tuple += ('A','B','C')
# another method: .extend/ insert





#set {}
#not ordered: not possible to access by index
#dont allow duplicated elements


#not like list that you can create empty list like 
# empty_list[]
countries = {'Israel','USA','Brazil'}
names = {'Shimon','Hanna','Israel'}

