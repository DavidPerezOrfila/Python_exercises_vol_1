# Exercise156
"""
Using the built-in module for regular expressions, find all digits in the
following text:
string = 'Python 3.8'
Print the result to the console.
Tip: Use the findall() function and the regular expression for find only
digits"""
import re

string = "Python 3.8"
result = re.findall(pattern=r"\d", string=string)
print(result)
