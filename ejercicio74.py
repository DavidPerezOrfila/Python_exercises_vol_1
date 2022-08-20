# Exercise 74
"""
Write a program that finds all two-digit numbers divisible by 11 (use a for loop). Print the result to the console as comma-separated values as shown below.
Expected result:
11,22,33,44,55,66,77,88,99
"""
numbers = []
for i in range(10, 100):
    if i % 11 == 0:
        numbers.append(str(i))
print(','.join(numbers))
