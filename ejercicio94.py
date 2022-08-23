# Exercise 94
"""
Write a program that checks if the given element (target) is in the sorted list (numbers). We have given:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 7
Algorithm:
1. We set the start and end index as well as the flag = None.
2. As long as the start index is not greater than the end index, select the middle index (mid) of the list (arithmetic average of the start and end index -> remember to convert the result with the int() function). If the start index is greater than the end index, we end the algorithm.
3. Check if the element for the index calculated in this way is our target. If so, we set the flag to True and terminate the algorithm. If not -> step 4.
4. We check if the element of the list for the index mid is less than the target. If so, we increase the start index by 1. If not, we reduce the end index by 1 and go to step 2.
After while loop, depending on the value of the flag, print to the console:
'Found' or 'Not found'.
Expected result:
Found
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 7
start = 0
end = len(numbers) - 1
flag = None

while start <= end:
    mid = int((start + end) / 2)
    if numbers[mid] == target:
        flag = True
        break
    if numbers[mid] < target:
        start = mid + 1
    else:
        end = mid - 1

if flag:
    print('Found')
else:
    print('Not found')
