#FUNCTIONS
#syntax

# def func_name():
#     '''prints a phrase on the console''' #doc strings
#     print('I am a function')

# func_name()
# print(func_name.__doc__)

# create a function called greetings that prints "hello" in your mother tongue
#then call the function and run the file

# def greetings():
#     '''prints hello in portuguese on the console'''
#     print('Ola')

# greetings()

#Passing arguments to the function
# def greetings(language):
#     '''prints hello in the defined language on the console'''
#     if language == 'ES':
#         print('Hola')
#     elif language == 'RU':
#         print('Priviet')

# greetings('RU')

# def greetings(language = 'EN', user_name = 'Joe'):
#     '''prints hello in the defined language on the console'''
#     if language == 'ES':
#         print(f'Hola, {user_name}')
#     elif language == 'RU':
#         print(f'Priviet, {user_name}')
#     elif language == 'PT':
#         print(f'Ola, {user_name}')
#     elif language == 'EN':
#         print(f'Hello, {user_name}')    
#     else:
#         print('undefined language')

# #keyword arguments
# # greetings(user_name = 'Joel') #TypeError: greetings() missing 1 required positional argument: 'language'

# greetings()

# create a function called country_info that receives a country name as argument
# and prints the capital of that country. Make the country name argument default
# Naboo (star wars planet). Its capital is Theed

def country_info(country_name = 'Naboo'):
    if country_name == 'France':
        print(f'The capital of {country_name} is Paris')
    elif country_name == 'Italy':
        print(f'The capital of {country_name} is Rome')
    elif country_name == 'Naboo':
        print(f'The capital of {country_name} is Theed')    
    else:
        print('country name not found')

# country_info('Patati')

#return keyword

def calculation(num1, num2):
    result = num1 + num2
    return result

# print(calculation(5, 4))
# calculation_result = calculation(5, 4)
# print(calculation_result + 10)

countries = ['Brazil', 'Israel', 'China']

def country_info(countries):
    for country in countries:
        print(f'hello {country}')
        if country == 'Israel':
            return country

print(country_info(countries))


#SCOPES
#global scope: on the file, in general
#local scope: indented block (if statement, a for loop, a function...)


scope_var = 100

def calculation(a, b):
    addition = a+b
    substraction = a-b
    global scope_var
    scope_var += 50
    return addition, substraction, scope_var

aditional, substract, scope_var_func = calculation(5, 7)
# print(aditional, substract, scope_var_func) #scope_var = 50 if we dont use the global keyword
# print(scope_var) #100 if we dont use the global keyword

####### run the code bellow after you added the keyword "global" and incremented (+=) 50 on the scope_var

print(aditional, substract, scope_var_func) #scope_var = 150 because the 50 was added to 100 in the global scope
print(scope_var) #150 because of the same reason



