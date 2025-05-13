#Challenge 1: Letter Index Dictionary

word_of_input = input("Enter a word: ")
char_positions = {}

for i, char in enumerate(word_of_input):
    if char in char_positions:
        char_positions[char].append(i)
    else:
        char_positions[char]=[i]
print(char_positions)

#Challenge 2: Affordable Items

# items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
# wallet = "$300"
purchasable = []

items_purchase = {"Apple": "$4", "Honey": "$3", "Fan": "$14", "Bananas": "$4", "Pan": "$100", "Spoon": "$2"}
wallet = "$100"

# items_purchase = {"Phone": "$999", "Speakers": "$300", "Laptop": "$5,000", "PC": "$1200"}
# wallet = "$1"

#in order to compare the numbers, change price to integers
wallet_amount = int(wallet.replace("$","").replace(",",""))

for item, price in items_purchase.items():
    price_amount = int(price.replace("$","").replace(",",""))
    if price_amount < wallet_amount:
        purchasable.append(item)

if len(purchasable) > 0:
    print(purchasable)
else:
    print("Nothing")

    
