class Text:
    def __init__(self, text):
        self.text = text

    def word_frequency(self, word):
        word_list = self.text.split()
        if word:
            return word_list.count(word)
        else: 
            return None

    def most_common_word(self):
        word_frequency_list = self.text.split()
        word_dict = {}
        for word in word_frequency_list:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
            #or more neat: word_dict[word] = word_dict.get(word, 0) + 1
        most_common_word = max(word_dict, key = word_dict.get)
        return most_common_word, word_dict[most_common_word]

    def unique_word(self):
        words = self.text.split()
        unique = set(words)
        return list(unique)
    
    @classmethod
    def from_file(cls, file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        return cls(content)

import string 
class TextModification(Text):
    def remove_punctuation(self):
        translator = str.maketrans(",", string.punctuation)
        no_punct = self.text.translate(translator)
        return no_punct




    