# Exercise 14
"""
From the following text:
string = 'PKV-89415-PLN'

extract the code containing the first three and last three characters. Print the result to the console.

Expected result:
PKVPLN

"""
string = 'PKV-89415-PLN'
print(string[:3] + string[-3:])
