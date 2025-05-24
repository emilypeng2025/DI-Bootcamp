

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