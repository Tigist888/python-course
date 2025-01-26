# Get input from the user
user_input = input('Give me a phrase')

# Split user input into words
words = user_input.split()
print(words)

# Reverse the list and print it
reversed_words = " ".join(reversed(words))
print(reversed_words)

# Print the length of the words list
print(len(words))