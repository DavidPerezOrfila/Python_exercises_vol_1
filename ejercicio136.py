# Exercise 136
"""
Implement a generator called enum() that works just like the enumerate() built-in function.

For simplicity, the function gets an iterable object and returns a tuple (index, element).
"""


def enum(items):
    i = 0
    for item in items:
        yield (i, item)
        i += 1
