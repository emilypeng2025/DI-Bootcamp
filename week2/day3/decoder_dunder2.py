from datetime import datetime, date

class Person:

    def __init__(self, name, last_name, birth_date):
        self.name = name
        self.last_name = last_name
        self.birth_date = self.parse_birthdate(birth_date)

    @classmethod
    def from_age(cls, name, last_name, age):
        current_year = datetime.today().year
        birth_year = current_year - age
        birth_date = f'{birth_year}-1-1'
        return cls(name, last_name, birth_date)

    @staticmethod
    def parse_birthdate(date_string):
        return datetime.strptime(date_string, '%Y-%m-%d').date()
    
    @property
    def age(self):
        today = date.today()
        age = today.year - self.birth_date.year
        return age

    @staticmethod
    def format_name(name, last_name):
        if not name[0].isupper():
            return name.capitalize()
        if not last_name[0].isupper():
            return last_name.capitalize()
        

p1 = Person('Alice', 'Wonder', '1990-02-05')
print(type(p1.birth_date))
print(p1.age) #because I have @property method, the age can be accessed as an atribute

p2 = Person.from_age('Bob', 'Smith', 30)
print(p2.birth_date)

# print(datetime.today().year)

#create a static method that format the name and last name 
# in case the first letter is not upper case
#usage example: 
p3 = Person('juliana', 'schmidt', 35)
#the static method will change it to capital case.









