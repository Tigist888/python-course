# Create a program, that takes a word input from the user, and prints out a
# dictionary showing the letter count for each letter in the word.

# Examples:
#   cat  -> {"c" : 1, "a" : 1, "t" : 1}
#   call -> {"c" : 1, "a" : 1, "l" : 2}

# Use as many of the following concepts as you can:
# - Functions
# - Dictionaries
# - Asking for user input
# - Loops

# Bonus: Keep asking for words until the user types "end" OR an empty word.

def count_letters(word):
    letter_count = {}
    for letter in word:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count



while True:
    word = input("Enter a word (or type 'end' to stop): ").strip().lower()

    if word == "end" or not word:  # Stop if the word is "end" or empty
        print("Goodbye!")
        break

    letter_count = count_letters(word)
    print(f"Letter count for '{word}': {letter_count}")