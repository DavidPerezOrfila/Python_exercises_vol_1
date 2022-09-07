# Exercise 116
"""
Implement a function map_longest() that accepts the list of words and return
the length of the longest word in this list.
Example:
[IN]: map_longest(['python', 'sql'])
[OUT]: 6
[IN]: map_longest(['java', 'sql', 'r'])
[OUT]: 4
Note! You only need to define the function.
"""


def map_longest(a_list):
    """accepts the list of words and return
the length of the longest word in this list"""
    items_length = [len(i) for i in a_list]
    return max(items_length)


print(map_longest(['java', 'sql', 'r']))
