import os

dir_path = os.path.dirname(os.path.realpath(__file__))

class AnagramChecker:

    def __init__(self, path = dir_path): #make the default attributs as the sowpods file
        self.words_file = [] # create an empty list to be added words on from the file #need the self otherwise the coming two steps i cannot refer to here

        with open(f'{dir_path}/sowpods.txt', 'r', encoding='utf-8') as file:
            for word in file:
                clean_words = word.strip().lower()
                self.words_file.append(clean_words)

    def is_valid_word(self, word):
        return word.lower() in self.words_file
    
    def get_anagrams(self, word):
        word = word.lower()

        if word not in self.words_file:
            print("Word not found in dictionary. ")
            return [] 
        
        #2 steps:
        #1. get into each character and put each letter in all positions
        from itertools import permutations
        chars = list(word)
        all_combinations = set("".join(p) for p in permutations(chars)) #permutations is to check all possible combinations, creating a tuple of characters, change to set so no double results
        # print(all_combinations)

        # 2. check if word is_valid_word
        valid_anagrams = []
        for w in all_combinations:
            if w in self.words_file and w != word:
                valid_anagrams.append(w)   

        return valid_anagrams
    

# word = AnagramChecker()
# word.get_anagrams("meat")

        