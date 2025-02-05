# Create a function that takes two arguments and prints a greeting.
# The first argument should be the name of the person being greeted,
# the second argument are the words used for the greeting.

def greeting(name,message ):
    print(f'{message} {name}')

# Examples of the output expected for each function call.
greeting('Joseph','hello') # Prints: Hello, Joseph!
greeting("Joseph", "Howdy") # Prints: Howdy, Joseph!
greeting("Joseph", "Good morning") # Prints: Good morning, Joseph!
