# week 2 OOP QUIZZ

#exercise 1
# Answer the following questions:

#1. What is a class? 
    # A class is a blueprint or template for objects. It defines properties (variables) and behaviors (methods), but does not create an object itself.
    # #answer: a class is the blueprint/template of structure for a group of objects that share the same properties(variables/ attributes), use "class Uppercase first letters for each word" to start a class. 

#2. What is an instance?
    #An instance is a concrete object created from a class. Every time you use a class to create an object, that object is an instance.
    #how to create an instance? 
    #my_dog = Dog()  # my_dog is an instance of Dog #creating an instance (object) of the class Dog #Dog() calls the class’s __init__() method (the constructor)
    #give a name for the instance = the Class(arguments/variables unless default or that you are referring to a class or function/ not calling it yet, or you're passing it around eg to another funciton)

#3. What is encapsulation?
# Encapsulation means bundling data (attributes) and methods together while hiding the internal details from outside access.

# 封装是将数据（属性）和操作数据的方法（行为）绑定在一起，并隐藏内部实现的细节，只暴露必要的接口给外部使用。
# ✅ 作用：保护数据、简化使用、提高代码安全性。benefits: protect data; control access; improve code safety
# ✅ Python 实现方式：使用 _ 或 __ 前缀来标识私有属性/方法。#Python uses _ or __ to indicate private memebers
#example 
class Person:
    def __init__(self):
        self.__age = 30  # private

    def get_age(self):
        return self.__age
    
#4. What is abstraction? 🇺🇸 Abstraction shows only the necessary details and hides the complex implementation.
#✅ Python uses abstract base classes (ABC) and @abstractmethod.
#example:
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

#5. What is inheritance? 🇺🇸 Inheritance allows a class to inherit attributes and methods from another class.

#6.What is multiple inheritance?🇺🇸 Multiple inheritance allows a class to inherit from more than one parent class.

#7.What is polymorphism?
#🇨🇳 多态指的是使用相同的方法名来表示不同类中的行为。
#🇺🇸 Polymorphism allows different classes to define methods with the same name but different implementations.

#8. What is method resolution order or MRO? #🇨🇳 方法解析顺序（MRO）是在多重继承中确定调用哪个方法的规则。
# MRO (Method Resolution Order) determines the order in which classes are searched for a method or attribute in multiple inheritance.
# print(SomeClass.__mro__) #this is how to check MRO #python uses the C3 linearization algorithm


# Exercise 2: Create a deck of cards class
# The Deck of cards class should NOT inherit from a Card class.

# The requirements are as follows:

# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
# The Deck class :
# should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# should have a method called deal which deals a single card from the deck. After a card is dealt, it should be removed from the deck.

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value 
    #if i want to show the object, use __str__
    def __str__(self):
        return f"{self.value} of {self.suit}"

import random

class Deck:
    def __init__(self):
        self.cards = []
        self.suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    
    def shuffle(self):
        self.cards = [Card(suit, value) for suit in self.suits for value in self.values]
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) == 0:
            return "No cards left to deal."
        return self.cards.pop()

deck = Deck()
deck.shuffle()
card = deck.deal()
# print(card)

# 发 5 张牌看看
# for _ in range(5):
#     print(deck.deal())