# *Args and **Kwargs

# def say_hello(user_name):
    
#     print(f'Hello, {user_name}')

# say_hello()

def print_names(*args):
    for name in args:
        print(f'Hello, {name}')
    if not args:
        print('please add a name to say hello')

print_names()

def user_info(**kwargs):
    for info in kwargs.values():
        print(info)

user_info(name = 'Juliana', age = 35, address = 'Ramat Gan')

# create a function called tasks_manager that accepts tasks 
# and prints for each task "today I need to do:  {task}"

def tasks_manager(*args):
    if args:
        for arg in args:
            print(f'Today I need to do {arg}')
    else:
        print('please pass a task as argument')

tasks_manager('finish Daily Challenge', 'buy bread', 'call my mom')

#using *args and **kwargs together:

def party_planner(*args, **kwargs):
    if args:
        print('You need to buy: ')
        for arg in args:
            print(arg)
    else:
        print('there is no food to buy' )

    if kwargs:
        print('Party details: ')

        for key, value in kwargs.items():
            print(f' {key} : \n {value}')
    else:
        print('there is no details for this party' )

#exercise: 
# 1 - Call this function and pass the food and the party details.
# 2 - Call it only with food info
# 3 - Call it with only the details

party_planner('pizza', 'chips', 'drinks', 'coxinha',  time = '7PM', ticket_price = [200, 250, 100])