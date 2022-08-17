# Exercise 49
"""
The following list represents order ids for a given day:
day1 = ['3984', '9042', '4829', '2380']
Using the appropriate method, extend this list to the next day:
day2 = ['4231', '5234', '1345', '2455']
Print the result to the console.
Expected result:
['3984', '9042', '4829', '2380', '4231', '5234', '1345', '2455']
"""
day1 = ['3984', '9042', '4829', '2380']
day2 = ['4231', '5234', '1345', '2455']
# print(day1+day2)
# solution 2
day1.extend(day2)
print(day1)
