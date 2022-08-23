# Exercise 85
"""
A list of names entered by users into the system is given below (without validation process):
names = ['Jack', 'Leon', 'Alice', '32-3c', 'Bob']
Iterate through the names list and check if each name is correct (contains only letters). If so, print to the console following message: f'Hello {name}!' otherwise do nothing.
Tip: Use the str.isalpha() method.
Expected result:
Hello Jack!
Hello Leon!
Hello Alice!
Hello Bob!
"""
names = ['Jack', 'Leon', 'Alice', '32-3c', 'Bob']
names = [print(f'Hello {name}!') for name in names if name.isalpha()]
