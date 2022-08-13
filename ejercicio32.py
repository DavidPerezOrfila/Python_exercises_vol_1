# Exercise 32
"""
Using the appropriate method, split the text into sentences.
Print the result as a list to the console.
Expected result:
['Python is a general-purpose language.', 'Python is popular.']
"""
text = """Python is a general-purpose language.
Python is popular."""
# Solution 1
# print(list(text.split('\n')))
print(text.splitlines())
