# Even/Odd Checker Function
# Your task is to write a function that determines if a given integer is even or odd. The function should
# print Even for even numbers and Odd for odd numbers.

# What You Need to Check
# - Determine whether the input number is even or odd.
# - An even number can be exactly divided by 2 without a remainder.
# - An odd number leaves a remainder of 1 when divided by 2.

# Define a function is_even_odd(number) here
def is_even_odd(number):
    if not isinstance(number, int):  # Check if the number is an integer
        print("Please provide an integer.")
        return
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")
print(is_even_odd(5))
# Test the function calling it using a variety of numbers like: 1, 10, 5.5, 9