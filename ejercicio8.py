# Exercise 8
'''
Calculate the distance of two points A = (3, 2), B = (- 1, -1)
and print result to the console as shown below.
Expected result:
The distance between points A and B: 5.0
'''
A = (3, 2)
B = (- 1, -1)
a1 = A[0]
a2 = A[1]
b1 = B[0]
b2 = B[1]
distance = ((((b1-a1)**2) + ((b2-a2)**2))**0.5)
print(f'The distance between points A and B: {distance}')