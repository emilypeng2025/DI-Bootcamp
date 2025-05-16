#what we learned yesterday:

# def say_hello(user_name):
#     print(f"Hello,{user_name}")
# say_hello("Anne")

## but using *args 

#def print_names(*args):

# how args work?


# def user_info(**kwargs):
#     for info in kwarg.values():
#         print(info)
# user_info(name='Juliana', age=35, address= 'Tel Aviv')



# def tasks_manager(*MayToDoList):
#     for MayToDoList in MayToDoList:
#         print(f"Today I need to do {MayToDoList}")

# tasks_manager("landary" ,"afternoontask")

# def tasks_manager(*args):
#     if args:
#         for arg in args:
#             print(f"today i need to {arg}")
    
# tasks_manager("go shopping")

def party_planner(*food,**party_information):
    if food:
        print(f"You need to bring{food}")
    else:
        print("No need to bring any food.")
    
    if party_information:
        print("Party details: ")

        for key,value in party_information.items():
            print(f"{key} is {value}")

# party_planner("avocado", "tomato", "sweet drinks")
#party_planner()
#party_planner(Address="Habima Square",Time=1900,)
party_planner("avocado", "tomato", "sweet drinks", Address="Habima Square",Time=1900,)


# print(f"We will provide{food}, and please pay attention that)
# party_planner(address=)
# address:
# hour:
