# Exercise 121
"""
Implement a function remove_duplicates() that removes duplicates from the list (the order of the items in the list does not have to be kept).
Example:
[IN]: remove_duplicates([1, 5, 3, 2, 2, 4, 2, 4])
[OUT]: [1, 2, 3, 4, 5]
[IN]: remove_duplicates([1, 1, 1, 1])
[OUT]: [1]
Note! You only need to define the function.
"""

def remove_duplicates(a_list):
    result = list(set(a_list))
    return result

print(remove_duplicates([1, 5, 3, 2, 2, 4, 2, 4]))
print(remove_duplicates([1, 1, 1, 1]))
