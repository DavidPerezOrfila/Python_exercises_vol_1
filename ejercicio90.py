# Exercise 90
"""
The list of names is given (one is missing):
names = ['Jack', 'Leon', 'Alice', None, 'Bob']
Using the continue statement, print only the correct names to the console as shown below.
Expected result:
Jack
Leon
Alice
Bob
"""
names = ['Jack', 'Leon', 'Alice', None, 'Bob']
for name in names:
    if not isinstance(name, str):
        continue
    print(name)
