from anagram_checker import AnagramChecker

checker = AnagramChecker()

print("Welcome aboard!" "This is an anagram checker." "If you wish to exit, print 'exit': ")

while True:
    word = input("Please type a word: ").strip()

    if word.lower() == "exit":
        print("Goodbye!")
        break 

    if not word.isalpha():
        print("Invalid input: use only letters please")
        continue

    if "  " in word:
        print("Please enter only one word.")
        continue

    if not checker.is_valid_word(word):
        print("Not a valid word.")
        continue

    anagrams = checker.get_anagrams(word)
    print(f"Anagrams:{anagrams}")

