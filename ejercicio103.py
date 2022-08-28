# Exercise 103
"""
Generate all even numbers from 2 to 18 inclusive.
Then write each number on a separate line to the file called num.txt.
"""

numbers = list(range(1, 20))
even = [number for number in numbers if number % 2 == 0]

with open('num.txt', 'w') as file:
    for num in even:
        file.write(str(num) + '\n')
