#loop

#for loop

# fruits = ['apple','banana','kiwi','pear']
# for each_fruit in fruits:
#     print(f"i love {each_fruit}")

# for i in range(1,11): #if want 1-10, 1,10+1
#     print(i)

# for i in range(len(fruits)+1):
#     print(i)


# odd_nums = list(range(1,11,2))
# print(min(odd_nums))
# print(max(odd_nums))
# print(sum(odd_nums))

#for loops takes longer time 知道要循环几次时用

#while loop 不知道要循环几次，只要条件为真就循环

# num = 0
# while num <= 10:
#     print(num)
#     num += 1
# print("finished")

#game to let user keep guessing using while loop
secret_numb = 77
user_number = int(input("try a number "))

while user_number != secret_numb:
    print("not the number, try again")
    user_number = int(input("try a number "))
else:
    print("congrats!you won!")