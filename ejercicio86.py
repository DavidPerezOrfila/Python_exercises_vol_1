# Exercise 86
"""
Exercise 1
Write a program that compares two lists and returns True if the lists contain at least one of the same element. Otherwise, it will return False.
Use break statement in the solution and print result to the console.
Lists:
list1 = [1, 2, 0]
list2 = [4, 5, 6, 1]
Expected result:
True
"""
list1 = [1, 2, 0]
list2 = [4, 5, 6, 1]
# Solution1
# for i in list1:
#     for j in list2:
#         if j == i:
#             print(True)
#             break
# Solution 2
result = False

for item1 in list1:
    if item1 in list2:
        result = True
        break
print(result)
