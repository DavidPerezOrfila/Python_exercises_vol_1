# Exercise 81
"""
Write a program that creates a histogram as a dictionary of the following values:
items = ['x', 'y', 'z', 'y', 'x', 'y', 'y', 'z', 'x']
In response print histogram to the console.
Expected result:
{'x': 3, 'y': 4, 'z': 2}
"""
items = ['x', 'y', 'z', 'y', 'x', 'y', 'y', 'z', 'x']
histogram = {}
for i in items:
    if i not in histogram.keys():
        histogram[i] = 1
    else:
        histogram[i] += 1
print(histogram)
