# Exercise161
"""
Using the collections built-in package, create a Counter class object that
counts the frequency of items in the following list:
items = ['YES', 'NO', 'NO', 'YES', 'EMPTY', 'YES', 'NO']
Print the result to the console.
Expected result:
Counter({'YES': 3, 'NO': 3, 'EMPTY': 1})

"""
from collections import Counter

counter = Counter()
items = ['YES', 'NO', 'NO', 'YES', 'EMPTY', 'YES', 'NO']
for item in items:
    counter[item] += 1
print(counter)
