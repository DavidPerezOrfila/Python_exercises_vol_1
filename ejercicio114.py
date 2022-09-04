# Exercise 114
"""
Implement a function called maximum() that returns the maximum of three numbers.
Use conditional statement.
Example:
[IN]: maximum(4, 2, 1)
[OUT]: 4
[IN]: maximum(-3, 2, 5)
[OUT]: 5
Note! You only need to define the function.
"""


def maximum(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
