# Exercise 139
"""
The following text is given:
desc = "Playway: Playway is a producer of computer games."
Change all characters to lowercase, remove the colon, period and then split the text into words.
Create a set of unique words and print the length of this set to the console.
Expected result:
7
"""
desc = "Playway: Playway is a producer of computer games."
word_list = desc.lower().replace(':', '').replace('.', '').split()
word_unique = {word for word in word_list}
print(len(word_unique))
