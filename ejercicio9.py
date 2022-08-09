# Exercise 9
"""
Find the roots of the quadratic equation:
x2 + 5x +4 = 0
Print the result to the console as shown below.
Expected result:
x1 = -4.0
x2 = -1.0
"""
a = 1
b = 5
c = 4
discriminant = b ** 2 - 4 * a * c
disc_square = discriminant ** 0.5
x1 = (-b - disc_square) / (2 * a)
x2 = (-b + disc_square) / (2 * a)

print(f'x1 = {x1}')
print(f'x2 = {x2}')
