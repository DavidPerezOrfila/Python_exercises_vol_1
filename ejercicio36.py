# Exercise 36
"""
The following text is given:
text = 'Programming in python.'
Follow the next steps:
-Change all letters to lowercase.
-Delete spaces and period.
-Create a set consisting of all letters in the text and assign to letters variable
-Using the appropriate method for sets, remove all vowels from letters set:
vowels = {'a', 'e', 'i', 'o', 'u'}
-Print the number of items in the letters set as shown below.
Expected result:
Number of items: 8
"""
text = "Programming in python."
text = text.lower()
text = text.replace(" ", "")
text = text.replace(".", "")
vowels = {"a", "e", "i", "o", "u"}
letters = set(text)
consonants = letters.difference(vowels)
print(f"Number of items: {len(consonants)}")
