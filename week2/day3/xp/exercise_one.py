from func import sum_numbers

print(sum_numbers(5, 4))

#exercise 3 String Module
import string
import random

all_letters = string.ascii_letters
random_string = ""

for _ in range(5):
    random_char = random.choice(all_letters)
    random_string += random_char

print("This random string is: ", random_string)

#exercise 4 current date
from datetime import date

def show_current_date():
    today = date.today()
    print("Today's date is: ", today)
show_current_date()

#exercise 5  Amount of time left until January 1st
from datetime import datetime
now = datetime.now()
print("The time now is:", now)

next_year = now.year + 1
jan_first = datetime(next_year, 1, 1)
time_difference = jan_first - now

print("This is the time left until January 1st of the next year: ", time_difference)

#exercise 6 birthday and minutes
from datetime import datetime
def minutes_lived(birthdate_str):
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
    now = datetime.now()

    #calculate the time difference
    time_difference = now - birthdate
    minutes = int(time_difference.total_seconds()/60)
    print(f"You have lived for {minutes: ,} minutes.")

minutes_lived("1962-11-09")




#exercise 7

from faker import Faker


fake = Faker("zh_CN")

print(fake.name())
print(fake.address())