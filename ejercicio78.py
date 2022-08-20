# Exercise 78
"""
The following text is given:
text = 'Python is a very popular programming language'
Write a program which extracts exactly the first four words as a list. Standardize each word, i.e. replace uppercase letters with lowercase. Present the result in a list and print to the console as shown below.
Expected result:
['python', 'is', 'a', 'very']
"""
text = 'Python is a very popular programming language'
result = []
spplitted_text = text.split(' ')
for i, word in enumerate(spplitted_text):
    if i < 4:
        result.append(word.lower())
print(result)
