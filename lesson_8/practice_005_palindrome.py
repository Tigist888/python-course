# Create a program that prints whether a given word is a palindrome.
# Palindrome: A word that is the same both ways, like tacocat, racecar, madam.

# The word should be provided by the user using input()
# Your function should take one argument.
# Your function should return True / False.
# You should use the return value of the function to print out if the word
# is a palindrome or not.

# Hint: The following code might be useful to determine if a word is a palindrome.

def is_word_palindrome(word):

   reversed_word = word[::-1]

   if word == reversed_word:
     return True
   else:
     return False
word = input("Enter a word: ")
if is_word_palindrome(word):
    print("Word is a palindrome")
else:
    print("Word is not a palindrome")