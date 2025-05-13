#review list
# shopping_list = ["milk", "eggs", "bread"]
# shopping_list.append("butter")
# shopping_list.remove("eggs")
# print(shopping_list[0])

#dictionary 
# my_dog = {
#     'name': 'Rufus',
#     'age': 4
# }
# print(my_dog['name'])
# print('The name of my dog is:',my_dog['name'])

# my_dog.update({
#     'name': 'Snow'
# })
# print(my_dog['name'])

# my_dog['age'] = 3
# print(my_dog['age'])
# print(my_dog.items())
# for key,value in my_dog.items():
#     print(key, '->',value)

# my_dog.update({
#     'best_friends': {
#         'name': 'Felix',
#         'age': 4.5
# }
               
# })
# print(my_dog.items)

# sample_dict = { 
#    "class":{ 
#       "student":{ 
#          "name":"Mike",
#          "marks":{ 
#             "physics":70,
#             "history":80
#          }
#       }
#    }
# }
# print(sample_dict['class']['student']['marks']['history'])
# print(sample_dict.keys)
# print(sample_dict.values)

# rick_dict = {
#     'first_name':'Rick',
#     'last_name':'Sanchez'
# }
# print(rick_dict['first_name'])


# rick_dict = {
#     'first_name':'Rick',
#     'last_name':'Sanchez'
# }
# print(rick_dict.keys())
# print(rick_dict.values())
# print(rick_dict['first_name'])
# print(rick_dict.items())

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}
del sample_dict["name"]
print(sample_dict)