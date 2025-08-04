#
import datetime
class Person:

    def __init__(self, name, last_name, birth_date):
        self.name = name
        self.last_name = last_name
        self.birth_date = self.parse_birthday(birth_date)

    staticmethod
    def parse_birthday(date_string):
        return datetime.strptime(date_string, "%Y-%m-%d").date()

    @classmethod
    def from_age(cls, name, age):
        current_year = datetime.today().year
        birth_year = current_year - age
        birth_date = date(birth_year, 1, 1)
        return cls(name, last_name, birth_date)

p1 = Person("alice", "wonder", "1990-02-20")
print(p1.name)
print(type(p1.birth_date))

p2 = Person.from_age("Bob","Smith",)

#exercise 1 currencies
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount
    
    def __str__(self):
        if self.amount > 1:
            return f"amount: {self.amount} \n currency {self.currency}s"
        else:
            return f"{self.amount} {self.currency}"

c1 = Currency('dollar', 5)
print(type(c1))

c2 = Currency('real', 15)
print(c2.amount) #access an attribute of an object

dollar_info = {'amount': 5, 'currency': 'dollar'}
dollar_info['amount']# access a key of a dictionary







