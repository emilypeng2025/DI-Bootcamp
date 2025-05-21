import os
import random

dir_path = os.path.dirname(os.path.realpath(__file__))

def get_words_from_file(dir_path):
    with open(f"{dir_path}/words.txt", "r", encoding="utf-8") as f:
        content = f.read()
        words = content.split()
        return words
   
def random_sentence(length):
    words = get_words_from_file(dir_path)
    selected_words = random.choices(words, k=length)
    sentence = " ".join(selected_words)
    sentence = sentence.lower()
    return sentence 
# print(random_sentence(5))

def main():
    print("This program is generating a sentence from a list randomly at your choice of length." )
    length = input("How many words do you want the sentence to be(2-20)? ")
    try:
        length = int(length)
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
        exit()
    if length <2 or length > 20:
        print("Please enter a number between 2 and 20")
        exit()

    sentence = random_sentence(length)
    print("Here is your random sentence: ")
    print(sentence)

main()


#exercise 2
import json
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}
"""
new_dict= json.loads(sampleJson)
print(type(sampleJson))

print(new_dict["company"]["employee"]["payable"]["salary"])
new_dict["company"]["employee"]["birth_date"] = "1990-01-20"

with open(f"{dir_path}/company.json", "w") as f:
    json.dump(new_dict, f, indent = 3)