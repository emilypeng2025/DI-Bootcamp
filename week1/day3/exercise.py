# Exercise 1: Converting Lists into Dictionaries

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

first_dictionary = dict (zip(keys, values))
print(first_dictionary)

# Exercise 2: Cinemax #2

family = {"rick": 42, 'beth': 13, 'morty': 5, 'summer': 8}

#start the calculation from 0
total_cost = 0
for i in family.values(): #get the ages from the dictionary
    if i < 3:
        total_cost += 0
    elif i <12:
        total_cost += 10
    else:
        total_cost += 15
print(total_cost)
print("The total price is $")

#Print the ticket price for each family member.
for key,value in family.items():
    if value < 3:
       family[key] = 0
       print(f"The price for {key} is $0")  
    elif value < 12:
       family[key] = 10
       print(f"The price for {key} is $10") 
    else:
        family[key] = 15
        print(f"The price for {key} is $15") 

#exercise 3 Zara
brand_dic = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {"France": "blue", "Spain": "red", "US": ["pink", "green"]}
}
#Change the value of number_stores to 2.
brand_dic["number_stores"] = 2
print(brand_dic)

# Print a sentence describing Zara’s clients using the type_of_clothes key.
print("Zara's clients including those who wear", brand_dic["type_of_clothes"], "clothing")

#Add a new key country_creation with the value Spain.
brand_dic.update({
    "country_creation": "Spain"
})
#Check if international_competitors exists and, if so, add “Desigual” to the list.
if "international_competitors" in brand_dic:
    brand_dic["international_competitors"].append("Desigual")

# Delete the creation_date key.
del brand_dic["creation_date"]

# Print the last item in international_competitors.
print(brand_dic["international_competitors"][-1])

# Print the major colors in the US.
print(f"the major colors in the US are: {" and ".join(brand_dic["major_color"]["US"])}")

# Print the number of keys in the dictionary.
print(len(brand_dic.keys()))

# Print all keys of the dictionary.
print(brand_dic.keys())

# Bonus:
# Create another dictionary called more_on_zara with creation_date and number_stores. Merge this dictionary with the original brand dictionary and print the result.
more_on_zara = {
    "creation_date": 1975,
    "number_of_stores": 2047
}
merge = brand_dic|more_on_zara #or brand_dic.update(more_on_zara)
print(merge)

# Exercise 4: Disney Characters
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
indices = [0,1,2,3,4] #create a list, then use zip

user_indices = dict(zip(users,indices))
print(user_indices)

#2. Create a dictionary that maps indices to characters:

user_indices = dict(zip(indices, users))
print(user_indices)

#3. Create a dictionary where characters are sorted alphabetically and mapped to their indices:
sorted_users = sorted(users)
user_indices = dict(zip(sorted_users,indices))
print(user_indices)