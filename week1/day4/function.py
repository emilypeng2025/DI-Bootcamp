#function
#syntax

# def func_name():
#     '''prints a phrase on the console''' #doc strings
#     print("I am a function")

#this is to call it
# func_name()
# print(print.__doc__)

# def greetings():
#     print("nǐ hǎo")


#passing the arguements to the function
# def greetings(language):
#     if language == 'PT':
#         print('Ola')
#     elif language == 'Ru':
#         print('Priviet')
    
def greetings(language, user_name):
    if language == 'Hebrew':
        print(f'Shalom!{user_name}')
    elif language == 'Chinese':
        print(f'Ni Hao!{user_name}')
    elif language == 'Russian':
        print(f'Priviet!{user_name}')
    else:
        print("undefined language")
    
#greetings('Chinese','Jingwen')
greetings(user_name="Elya",language="Russian")

def country_info(country="China"):
    if country == "Israel":
        print("Jerusalem")
    elif country == "China":
        print("Beijing")
    elif country == ("Japan"):
        print("Tokyo")
    else:
        print("Country not in the system or misspelled, so printed capital of China")

country_info("JapaN")

#return keyword
def calculation(num1, num2):
    result = num1 + num2
    return result
calculation_result = calculation(5,4)