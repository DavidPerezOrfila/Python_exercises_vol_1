# Exercise 119
"""
Implement a function count_str(), which returns the number of str objects in an
iterable object (list, tuple, set).
Example:
[IN]: count_str(['p', 2, 4.3, None])
[OUT]: 1
[IN]: count_str({'p', 2, 4.3, True, 'True', None})
[OUT]: 2
Note! You only need to define the function.
"""


def count_str(iterable):
    """returns the number of str objects in an
iterable object (list, tuple, set)"""
    total = 0
    for i in iterable:
        if isinstance(i, str):
            total += 1
    return total


print(count_str(['p', 2, 4.3, None]))
