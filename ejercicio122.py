# Exercise 122
"""
Implement a function is_distinct() to check if the list contains unique values.
Example:
[IN]: is_distinct([1, 2, 3])
[OUT]: True
[IN]: is_distinct([1, 2, 3, 3])
[OUT]: False
Note! You only need to define the function.
"""

def is_distinct(items):
    return len(items) == len(set(items))

print(is_distinct([1, 2, 3]))
print(is_distinct([1, 2, 3, 3]))