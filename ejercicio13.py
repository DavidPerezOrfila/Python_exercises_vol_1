# Exercise 13
"""
From the given file name:
filename = 'view.jpg'
extract extension and print it to the console.
Expected result:
jpg
"""
filename = 'view.jpg'
# Solution 1 using split method
# filename = filename.split(".")
# print(filename[1])
# Solution 2 using slices
print(filename[-3:])
