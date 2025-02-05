# Create a program that does the following:
#
# 1. Keeps asking for names, one at a time. Stop asking for names when user's input is "end".
# 2. When the user is done adding names, the program should show two lines for each name:
#    - A line with a greeting: "Hello, {name}!"
#    - A line with the first letter of the user's name: "Your initial is {initial}."
#
# Use at least one function. Extra points if you use two and call a function from another function.

def greet_user(name):

    initial = name[0].upper()
    print(f"Hello, {name}!")
    print(f"Your initial is {initial}.")


names = []

while True:
    name = input("Enter your name (or type 'end' to stop):  ")
    if name.lower() == 'end':
        break
    names.append(name)

for name in names:
    greet_user(name)
