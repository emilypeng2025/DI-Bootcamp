# FILE I/O - INPUT/ OUTPUT

# OLD SCHOOL WAY OF OPENING A FILE WITH PYTHON
# file_object = open(r'C:\Users\julia\OneDrive\Desktop\DI-Bootcamp-april2025\W2\D4\file_io.py')
# print(file_object)

# MODERN PYTHON WAY (AUTOMATICALLY CLOSED)
# with open(r'C:\Users\julia\OneDrive\Desktop\DI-Bootcamp-april2025\W2\D4\secrets.txt', encoding='utf-8') as file_obj:
#     #READING METHODS: the default mode of open()

#     output = file_obj.read() #returns the whole content of the file
#     output = file_obj.readline() #returns one line
#     output = file_obj.readlines() #returns a list where each line is an element
#     print(output)

# WRITING ON THE FILE
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f'{dir_path}/secrets.txt', 'a', encoding='utf-8') as file_obj:
    # we can define the mode: 'w' to write and delete what was in the file before
    # 'a' to append a new line to the file

    names = ['Aragorn \n', 'Gandalf\n', 'Saruman\n']
    file_obj.writelines(names)
    print('names added sucessfully')





# import os
# dir_path = os.path.dirname(os.path.realpath(__file__))


# #the old style way opening a file
# file_object = open (r"/Users/emilypeng/Desktop/DI-BOotcamp/week2/day4/secrets.txt")
# print(file_object)

# file_object = open("file.txt")
# # 执行操作
# file_object.close()  # 需要记得手动关闭

# the modern way, compared to the old way, python way, automatically closed
# with open(r"/Users/emilypeng/Desktop/DI-BOotcamp/week2/day4/starwars.txt", "a", encoding="utf-8")as starwars_file:
#     # output = file_obj.readlines()
#     # # for line in open("starwars.txt"):
#     # print(output)
#     # output = starwars_file.read()
#     # print(output)
#     line_by_line = starwars_file.readlines()
#     # print(line_by_line[5])
#     # for line in starwars_file:
#     #     print(line.strip())
#     # print(f"The fifth line is {line_by_line[5]}")

#     for line in line_by_line:
#         words = line.strip().split()
#         print(words)
#         names = ["Skywalker\n"]
#         if "luke" in line:
#             starwars_file.writelines(names)
#         print("names added successfully")


# open(r"/Users/emilypeng/Desktop/DI-BOotcamp/week2/day4/pythonfileio.py", encoding = "utf-8") as file_obj:
#     output =file_object.readline()
#     print(output)

# with open(f"{dir_path}/secrets.txt", "a", encoding = "utf -8") as file_object:
#     # file_object.writelines("Hello pythonI/O")
#     # file_object.writelines("Hello Python I/O. \n Today is Wed")
    
#     names = ["Skywalker\n"]
#     file_object.writelines(names)
#     print ("names added successfully")


#exercise
#bullet 4 
# with open(f"{dir_path}/starwars.txt","a+", encoding = "utf -8") as sw_f:

#     list_str = sw_f.readlines()
# # splited_list = [] 
# # for line in list_str:
# #     splited_list.append(line.split())
# # print(splited_list)

#     for line in list_str:
#         clean_line = line.split()
#         print(clean_line)
#         if clean_line == "luke":
#             print(f"{clean_line} SkyWalker")
#     print(line)

