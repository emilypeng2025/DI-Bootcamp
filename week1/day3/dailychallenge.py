#Challenge 1: Letter Index Dictionary

word_of_input = input("Enter a word: ")
char_positions = {}

for i, char in enumerate(word_of_input): #(i is an index/ the creation of(0,"d") is one tuple)
    if char in char_positions:
        char_positions[char].append(i)
    else:
        char_positions[char]=[i]
print(char_positions)



#step one to create only one tuple (0:'d') 
# for i, char in enumerate(uer_word):
#    out_dict.update({char:i})
#step 2 check in the dictionary


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
    purchasable.sort()
    print(purchasable)
else:
    print("Nothing")

##step 1
##the logic for loop, give name for key and value, get into both of them
#for item_name, price in item_purchase.items()
##dictionary.keys dictionary.value only access one part of them
##convert the string to interger
    
