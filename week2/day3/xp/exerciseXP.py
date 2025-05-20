#exercise 1 currencies
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount
    
    def __str__(self):
        if self.amount > 1:
            return f"{self.amount} {self.currency}s"
        else:
            return f"{self.amount} {self.currency}"
    def __int__(self):
        return self.amount
    def __repr__(self):
        return f"Currency('{self.currency}', {self.amount})"

    def __add__(self, other):
        if isinstance(other, int):
            return Currency(self.currency, self.amount + other)
        elif isinstance(other, Currency):
            if self.currency != other.currency:
                    raise TypeError("Cannot add two differnt currencies.")
            return Currency(self.currency, self.amount + other.amount) 
        else: 
            raise TypeError("Unsupported action")
        

    def __iadd__(self, other):
        if isinstance(other, int):
            self.amount += other
        elif isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError ("Cannot add two different currencies")
            self.amount += other.amount 
        else: 
            raise TypeError("Unsupported type for addition.")
        return self 

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1)) #or print(c1)
print(int(c1))
print(repr(c1))
print(c1 + 5)
print(c1 + c2)
c1 += 5
print(c1)
c1 += c2
print(c1)

try:
    print(c1+c3)
except TypeError as e:
    print(f"Error: {e}")





