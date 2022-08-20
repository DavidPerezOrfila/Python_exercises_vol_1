# Exercise 79
"""
Write a program that returns a list of values above the given threshold = 0.5 from the following list:
probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]
Expected result:
[0.91, 0.55, 0.76]
"""

probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]
result = [i for i in probabilities if i > 0.5]
print(result)
