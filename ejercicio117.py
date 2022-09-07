# Exercise 117
"""
Implement a function called filter_ge_6() that takes a list of words and
returns list of words with the length greater than or equal to 6 characters.
Example:
[IN]: filter_ge_6(['programming', 'python', 'java', 'sql'])
[OUT]: ['programming', 'python']
[IN]: filter_ge_6(['java', 'sql'])
[OUT]: []
Note! You only need to define the function.
"""


def filter_ge_6(a_list):
    """
    takes a list of words and returns list of words with the length greater
    than or equal to 6 characters
    """
    items_length = [i for i in a_list if len(i) >= 6]
    return items_length


print(filter_ge_6(['programming', 'python', 'java', 'sql']))
print(filter_ge_6(['java', 'sql']))
