# Exercise 118
"""
Implement a function called factorial() that calculates the factorial for a given number.
Example:
[IN]: factorial(6)
[OUT]: 720
[IN]: factorial(10)
[OUT]: 3628800
Note! You only need to define the function.
"""


def factorial(number):
    """calculates the factorial for a given number"""
    return 1 if number == 0 else number * factorial(number-1)


print(factorial(6))
