# Exercise157
"""
Using the built-in module for regular expressions, find all alphanumeric
characters in the following text:
string = '!@#$%^&45wc'
Print the result to the console.
Tip: Use the findall() function and the regular expression that find only
alphanumeric chars
Expected result:
['4', '5', 'w', 'c']
"""
import re

string = "!@#$%^&45wc"
result = re.findall(pattern=r"\w", string=string)
print(result)
