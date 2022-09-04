# Exercise 113
"""
Implement a function called maximum() that returns the maximum of two numbers.
Use conditional statement.
Example:
[IN]: maximum(4, 2)
[OUT]: 4
[IN]: maximum(-4, 2)
[OUT]: 2
Note! You only need to define the function.
"""


def maximum(a, b):
    return a if a >= b else b


print(maximum(-4, 2))
